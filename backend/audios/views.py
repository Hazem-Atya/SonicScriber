from django.http import JsonResponse
from .models import Audio
from .serializer import AudioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .blob_storage import blob_storage_handler

@api_view(['GET'])
def get_all_audios(request):
    
    audios_data = Audio.objects.all()
    serializer = AudioSerializer(audios_data, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
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


@api_view(['PATCH'])
def add_transcription(request,id):
    
    try:
        audio = Audio.objects.get(pk = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if 'transcription' not in request.data:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    transcription = {"transcription": request.data["transcription"]}
    serializer = AudioSerializer(audio, data=transcription, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)