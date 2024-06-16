


import unicodedata

def count_letters(input_string):
    if not isinstance(input_string, str):  ## first we check if the input string is not an instance of str u.e its not a string.
        return "Please enter a valid input"

    # Set of target letters to count, including their variations
    letters_to_count = {'S', 'K', 'Y'}
    
    # Create a dictionary to hold the counts
    count_dict = {letter: 0 for letter in letters_to_count}

    # Normalize the input string to NFD, the function uses unicodedata.normalize function to normalize input string into its unicode normalization for 'NFD'. this form decomposes characters into base characters and combining characters.
    normalized_string = unicodedata.normalize('NFD', input_string)
    
    # Iterate over each character in the normalized string
    for char in normalized_string:
        # Normalize the character for comparison
        normalized_char = unicodedata.normalize('NFD', char)
        
        # Check if the normalized character (in uppercase) is one of the target letters
        if normalized_char.upper() in letters_to_count:
            count_dict[normalized_char.upper()] += 1
    
    return count_dict


count_letters("This is a sentence")


## below we apply unit testing

import unittest

class TestCountLetters(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_letters(""), {'S': 0, 'K': 0, 'Y': 0})
    
    def test_no_target_letters(self):
        self.assertEqual(count_letters("This is a sentence"), {'S': 3, 'K': 0, 'Y': 0})
    
    def test_all_target_letters(self):
        self.assertEqual(count_letters("SKY"), {'S': 1, 'K': 1, 'Y': 1})
    
    def test_mixed_case(self):
        self.assertEqual(count_letters("Sky's the limit"), {'S': 2, 'K': 1, 'Y': 1})
    
    def test_repeated_letters(self):
        self.assertEqual(count_letters("SSSSKKKKYYYY"), {'S': 4, 'K': 4, 'Y': 4})
    
    def test_other_letters(self):
        self.assertEqual(count_letters("ABCDE"), {'S': 0, 'K': 0, 'Y': 0})
    
    def test_large_input(self):
        large_input = "S" * 1000 + "K" * 1000 + "Y" * 1000
        self.assertEqual(count_letters(large_input), {'S': 1000, 'K': 1000, 'Y': 1000})
        
    def test_float_input(self):
        self.assertEqual(count_letters(123.45), "Please enter a valid input")
    
    def test_dict_of_sentences(self):
        input_dict = {"sentence1": "This is a sentence.", "sentence2": "Another sentence."}
        self.assertEqual(count_letters(input_dict), "Please enter a valid input")
    
    def test_array_of_sentences(self):
        input_array = ["This is a sentence.", "Another sentence."]
        self.assertEqual(count_letters(input_array), "Please enter a valid input")
    
    def test_none_input(self):
        self.assertEqual(count_letters(None), "Please enter a valid input")
    
    def test_integer_input(self):
        self.assertEqual(count_letters(12345), "Please enter a valid input")
    
    def test_special_characters(self):
        self.assertEqual(count_letters("!@#$%"), {'S': 0, 'K': 0, 'Y': 0})
    
    def test_unicode_characters(self):
        self.assertEqual(count_letters("SḰY"), {'S': 1, 'K': 1, 'Y': 1})
    
    def test_single_character(self):
        self.assertEqual(count_letters("S"), {'S': 1, 'K': 0, 'Y': 0})
    
    def test_maximum_length(self):
        max_length_input = "S" * (10**6)  # Adjust to maximum limit if known
        self.assertEqual(count_letters(max_length_input), {'S': len(max_length_input), 'K': 0, 'Y': 0})
    
    def test_multiple_sentences(self):
        self.assertEqual(count_letters("This is a sentence. Another sentence."), {'S': 4, 'K': 0, 'Y': 0})
    
    def test_non_alphanumeric(self):
        self.assertEqual(count_letters("!!SKY??"), {'S': 1, 'K': 1, 'Y': 1})
    
    def test_different_language(self):
        self.assertEqual(count_letters("SKY こんにちは"), {'S': 1, 'K': 1, 'Y': 1})

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
