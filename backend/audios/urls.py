from django.urls import path
from . import views 

urlpatterns = [
    path('', views.get_all_audios),
    path('<int:id>', views.get_audio_by_id),
    # path('add', views.add_audio),
    path('transcribe/<int:id>', views.add_transcription),
    
]