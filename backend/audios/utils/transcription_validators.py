from ..models import CharacterSet  
import re 
import unicodedata

character_set = CharacterSet.objects.latest('pk')


def validate_string_charset(input_string):    
    valid_characters = set("() 'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ")
    input_set = set(input_string)    
    return all(char in valid_characters or char.isspace() for char in input_set)


def check_capital_letters(input_string):
    '''Checks that capital letter are only as a first word letter or if all the letters in the word are upper case'''
    pattern = re.compile(r'([A-Z][a-z]*|[A-Z]+|[a-z]+)')
    nfkd_form = unicodedata.normalize('NFKD', input_string)
    input_string =  ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    return all(pattern.fullmatch(word) for word in input_string.split())


def check_spaces(input_string):
    '''Returns true if there is only zero or one space between two characters, false otherwise'''
    pattern = re.compile(r'^\S+(\s?\S+)*$')
    return bool(pattern.match(input_string))