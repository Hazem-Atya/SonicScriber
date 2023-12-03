from rest_framework import serializers
from .models import Audio
from .utils.transcription_validators import *

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id','name','azure_blob_name','duration','description','user_id','transcription','created_at','updated_at')
        
    def validate_transcription(sef, value):
        if value is not None:
            if not validate_string_charset(value):
                raise serializers.ValidationError("Unauthorized characters in transcription.")
            if not check_capital_letters(value):
                raise serializers.ValidationError("Capital letters are allowed only as a first word letter or if all the letters in the word are upper case.")
            if not check_spaces(value):
                raise ValidationError("There can be only zero or one space between two characters.")           
        return value