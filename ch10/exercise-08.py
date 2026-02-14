# Extend either of the above programs so that it translates every text file in
# the current directory. Use an extension such as .pgl or .1f to distinguish
# the translated files from the original.

import pathlib

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
    path = pathlib.Path('.')
    for filepath in path.glob("*.txt"):
        with open(filepath, 'r') as f:
            for l in f:
                print(translatePhraseToLF(l))

main()