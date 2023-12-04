from django.test import TestCase
from .utils.transcription_validators import *
# Create your tests here.

class TestStringValidators(TestCase):
    
    def test_charset_validation(self):
        self.assertEqual(validate_string_charset("Hello 2024"), False)
        self.assertEqual(validate_string_charset("Hello! What's up?"), True)
        
        
    def test_capitals_letters_check(self):
        self.assertEquals(check_capital_letters('HELLO THIS IS AN AWesOME APP'), False)
        self.assertEquals(check_capital_letters('HELLO THIS IS AN app.'), True)
        
    def test_spaces_check(self):
        self.assertEquals(check_spaces("Hello    everyone"), False)
        self.assertEquals(check_spaces("He ll o ev er yo ne"), True)
        
    def test_punctuation_check(self):
        self.assertEquals(check_punctuation("Hello the team, how are you?"), True)
        self.assertEquals(check_punctuation("Hello the team, how are you?  "), False)
        self.assertEquals(check_punctuation("Hello the ?team, how are you?"), False)
        self.assertEquals(check_punctuation("Hello the ? Team, how are you?"), True)
        self.assertEquals(check_punctuation("Hello the ? team, how are you?"), False)