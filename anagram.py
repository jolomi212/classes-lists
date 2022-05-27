# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
word= input("Enter the first word here \n")
word2= input("Enter the second word here \n")

word = word.lower()
word2 = word2.lower()


def find_anagrams(word, anagram):
    # [assignment] Add your code here
   
    word_check = sorted(word)
    word2_check = sorted(word2)

    if len(word.split())==len(word2.split()) and word_check==word2_check:
        print("The given words are anagrams")
        return True
    else:
        print("The given words are not anagrams")
        return False 


find_anagrams(word, word2)
