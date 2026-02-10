# One problem with the previous exercise is that it does not deal with the
# case when we “drop off the end” of the alphabet. A true Caesar cipher
# does the shifting in a circular fashion where the next character after “z”
# is “a.” Modify your solution to the previous problem to make it circular.
# You may assume that the input consists of only letters and spaces.
# Hint: Make a string containing all the characters of your alphabet
# (uppercase letters, lowercase letters, and space) and use positions in your
# alphabet as the numbers for your code. You do not have to shift “z” into
# “a”; just make sure to use a circular shift over the entire sequence of 
# characters in your alphabet string. You can use the remainder operator to
# achieve the necessary wraparound ((oldpos + key) % len(alphabet)).

def caesar_cipher(plaintext, key):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHABET = ALPHABET + ALPHABET.lower() + ' '
    encoded_text = ''
    for c in plaintext:
        oldpos = ALPHABET.find(c)
        newpos = (oldpos + key) % len(ALPHABET)
        encoded_text = encoded_text + ALPHABET[newpos]
    return encoded_text

def main():
    plaintext = input("Enter plaintext: ")
    key = int(input("Amount to shift: "))
    encoded_text = caesar_cipher(plaintext, key)
    print(f"Encoded text = '{encoded_text}'")

main()
