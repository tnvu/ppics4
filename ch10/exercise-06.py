# Write a program that translates an English text file into a Pig Latin text
# file (see Exercise 14 from Chapter 8).

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
    inFile = input("Enter filename: ")
    with open(inFile, 'r') as f:
        for l in f:
            print(translatePhraseToPL(l))

main()