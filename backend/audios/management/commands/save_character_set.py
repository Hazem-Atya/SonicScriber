from ...models import CharacterSet
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Uploads files'
    
    def handle(self, *args, **kwargs):
        your_character_set = "()'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ "
        character_set_instance = CharacterSet(characters=your_character_set)
        character_set_instance.save()