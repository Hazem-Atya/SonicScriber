from ..models import CharacterSet  
import re 
import unicodedata

try:
    character_set = CharacterSet.objects.latest('id')
    valid_characters = set(character_set.characters)
except:
    valid_characters  = set("")


def validate_string_charset(input_string):
    input_set = set(input_string)    
    return all(char in valid_characters or char.isspace() for char in input_set)


def check_capital_letters(input_string):
    '''Checks that capital letter are only as a first word letter or if all the letters in the word are upper case'''
    pattern = re.compile(r"([A-Z][a-z()'-?,.;:!]*|[A-Z()'-?,.;:!]+|[a-z()'-?,.;:!]+)")
    nfkd_form = unicodedata.normalize('NFKD', input_string)
    input_string =  ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    return all(pattern.fullmatch(word) for word in input_string.split())


def check_spaces(input_string):
    '''Returns true if there is only zero or one space between two characters, false otherwise'''
    pattern = re.compile(r'^\S+(\s?\S+)*$')
    return bool(pattern.match(input_string))

def check_punctuation(text):
    pattern = re.compile(r'[?!\.](?:\s[A-Z]|$)')

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # If the number of matches is equal to the number of punctuation occurrences, return True
    return len(matches) == text.count('?') + text.count('!') + text.count('.')
