# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    first_word = input ('String1: ')
    second_word = input ('String2: ')
    
    sorted_first_word = sorted(first_word)
    sorted_second_word = sorted (second_word)
    # conditions
    if sorted_first_word == sorted_second_word:
        return True
    else:   
        return False

find_anagram("below", "elbow")
