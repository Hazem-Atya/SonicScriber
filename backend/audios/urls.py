from django.urls import path
from . import views 

urlpatterns = [
    path('', views.get_all_audios),
    path('<int:id>', views.get_audio_by_id),
    path('transcribe/<int:id>', views.add_transcription),
    path('usersAudios/', views.get_users_audios),
    
]