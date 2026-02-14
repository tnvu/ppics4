# Write a program that translates an English text file into an LF language
# text file (see Exercise 15 from Chapter 8).

VOWELS = 'AEIOUY'
def firstVowel(word):
    for i in range(len(word)):
        if VOWELS.find(word[i].upper()) > -1:
            return i
    return -1

def translateWordToLF(word):
    # First vowel
    if word[0].upper() == 'Y':
        vowel = firstVowel(word[1:]) + 1
    else:
        vowel = firstVowel(word)
    # Translate word
    lfWord = word[:vowel] + word[vowel] + 'lf' + word[vowel:]
    # Capitalize
    if word[0].isupper():
        lfWord = lfWord.capitalize()
    return lfWord

def translatePhraseToLF(phrase):
    lfPhrase =  ''
    for w in phrase.split():
        lfPhrase = lfPhrase + translateWordToLF(w) + ' '
    return lfPhrase[:-1]

def main():
    inFile = input("Enter a filename: ")
    with open(inFile, 'r') as f:
        for l in f:
            print(translatePhraseToLF(l))

main()