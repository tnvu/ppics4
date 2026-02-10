# LF is another made-up language (see previous problem). In LF, the
# letters “lf” are added after the first vowel in a word, and then that vowel
# is repeated. The sentence “Don’t talk in front of the kids” becomes
# “Dolfon’t talfalk ilfin frolfront olfof thelfe kilfids.” Write a program to
# translate phrases into LF. You should use the same ideas as outlined in the
# previous exercise.

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
    phrase = input("Enter a phrase: ")
    print(f"Translation = {translatePhraseToLF(phrase)}")

main()