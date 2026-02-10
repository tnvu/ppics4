# Pig Latin is a silly made-up language. A word in English is translated into
# Pig Latin by moving its initial consonant cluster to the end of the word
# and adding “ay.” If the English word starts with a vowel, then “way” is
# appended to the word. A sentence is translated into Pig Latin by translating
# each word. So, for example, the sentence, “Don’t talk in front of the
# kids,” becomes “On’tday alktay inway ontfray ofway ethay idskay.” Write
# a program that gets phrases from the user and translates them into Pig
# Latin.
# To help structure the program, write and test the following set of helper
# functions.
#       def firstVowel(word):
#           # returns the index of the first vowel in word
#       def translateWordToPL(word):
#           # returns the Pig Latin translation of a single word
#       def translatePhraseToPL(phrase):
#           # returns translation of a phrase
# For this program, treat “y” as a consonant if it is the first letter of a word
# and a vowel if it appears elsewhere.

VOWELS = 'AEIOUY'
def firstVowel(word):
    for i in range(len(word)):
        if VOWELS.find(word[i].upper()) > -1:
            return i
    return -1

def translateWordToPL(word):
    plword = None
    # Find first vowel
    if word[0].upper() == 'Y':
        # word starts with 'y', treat as consonant
        vowel = 1 + firstVowel(word[1:])
    else:
        vowel = firstVowel(word)
    # Transform word
    if vowel == 0:
        # starts with a vowel
        plword = word + "way"
    else:
        plword = word[vowel:] + word[:vowel] + "ay"
    # Capitalize
    if word[0].isupper():
        plword = plword.capitalize()
    return plword

def translatePhraseToPL(phrase):
    plphrase = ''
    for w in phrase.split():
        plphrase = plphrase + translateWordToPL(w) + ' '
    return plphrase[:-1]

def main():
    phrase = input("Enter a phrase: ")
    print(f"Pig Latin = '{translatePhraseToPL(phrase)}'")

main()
