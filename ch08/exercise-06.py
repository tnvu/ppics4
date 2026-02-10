# A Caesar cipher is a simple substitution cipher based on the idea of shifting
# each letter of the plaintext message a fixed number (called the key) of
# positions in the alphabet. For example, if the key value is 2, the word
# “Sourpuss” would be encoded as “Uqwtrwuu.” The original message can
# be recovered by “reencoding” it using the negative of the key.
# Write a program that can encode and decode Caesar ciphers. The input to the
# program will be a string of plaintext and the value of the key.
# The output will be an encoded message where each character in the original
# message is replaced by shifting it key characters in the Unicode character
# set. For example, if ch is a character in the string and key is the amount to
# shift, then the character that replaces ch can be calculated as:
#       chr(ord(ch) + key).

def shift_character(c, amount):
    d = c
    if c.isalpha():
        base_a = 'A'
        if c.islower():
            base_a = 'a'
        # offset is the number of characters from base_a shifted by amount
        # and limited to the 26 alphabet characters (wraparound 'Z' -> 'A')
        offset = (ord(c) - ord(base_a) + amount) % 26
        d = chr(ord(base_a) + offset)
    return d

def caesar_cipher(plaintext, key):
    encoded_text = ''
    for c in plaintext:
        encoded_text = encoded_text + shift_character(c, key)
    return encoded_text

def main():
    plaintext = input("Input plaintext: ")
    key = int(input("Input key: "))
    encoded_text = caesar_cipher(plaintext, key)
    print("Encoded text =", encoded_text)
    
main()
