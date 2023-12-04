from .models import Audio
from .serializer import AudioSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .blob_storage import blob_storage_handler
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_audios(request):
    paginator = CustomPageNumberPagination()

    audios_data = Audio.objects.all()
    result_page = paginator.paginate_queryset(audios_data, request)
    
    serializer = AudioSerializer(result_page, many = True)
    return paginator.get_paginated_response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_audio_by_id(request,id):
    try:
        audio = Audio.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AudioSerializer(audio)
    audio_data = serializer.data
    try:
        audio_url = blob_storage_handler.create_service_sas_blob(audio_data["azure_blob_name"])
        audio_data["audio_url"] = audio_url
        return Response(audio_data)
    except:
        return Response({"message": "Audio file Not found"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_users_audios(request):
    
    paginator = CustomPageNumberPagination()

    audios = Audio.objects.filter(user_id=request.user.id)
    result_page = paginator.paginate_queryset(audios, request)

    serializer = AudioSerializer(result_page, many = True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_transcription(request,id):
    
    try:
        audio = Audio.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if 'transcription' not in request.data:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    if audio.user_id is not None:
        return Response({  "message": "This audio has already been transcribed by another user."},status=status.HTTP_409_CONFLICT)
    transcription = {"transcription": request.data["transcription"], "user_id": request.user.id}
    serializer = AudioSerializer(audio, data=transcription, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)