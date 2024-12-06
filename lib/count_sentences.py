import re
import sys

class MyString:
    def __init__(self, value=''):
        # Ensure the value is a string, and print a message if it isn't.
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ''  # Set value to empty string if it's not valid.
        else:
            self.value = value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ''  # Set value to empty string if it's not valid.
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self.value.strip())
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)
