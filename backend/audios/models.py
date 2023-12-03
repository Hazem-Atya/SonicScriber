from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    duration = models.IntegerField(default=8)
    azure_blob_name = models.TextField(max_length=1024)
    transcription = models.TextField(null=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class CharacterSet(models.Model):
    characters = models.TextField()

    def __str__(self):
        return f"Character set {self.pk}"