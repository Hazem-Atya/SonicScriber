from ...models import CharacterSet
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Uploads files'
    
    def handle(self, *args, **kwargs):
        your_character_set = "()'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
        # Create an instance of the CharacterSet model
        character_set_instance = CharacterSet(characters=your_character_set)
        # Save the instance to the database
        character_set_instance.save()