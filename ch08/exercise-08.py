# A Caesar cipher (see previous exercise) is easy to break because it shifts
# each letter by the same amount. A Vingenére cipher is more secure, as it
# shifts different letters by differing amounts.
# The idea is to use a secret passphrase where the letters in the passphrase
# provide the shift amount for successive letters of the message. For example,
# if the passphrase is “cat” and the message is “Feed me,” The “F will be
# shifted three letters because “c” is the third letter of the alphabet, the 
# first ‘e” will be shifted one letter because “a” is the first letter of the
# alphabet, and the second “e” will be shifted 20 letters because “t” is the
# 20th letter of the alphabet. The passphrase is repeated as many times as 
# necessary to cover the entire message, thus the “d” will be shifted three 
# letters, the space one letter, the “m” 20 letters, etc.
# Write a program that implements encoding and decoding using a Vingenere
# cipher.

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET = ALPHABET + ALPHABET.lower() + ' '
    
def vingenere_encrypt(plaintext, passphrase):
    ciphertext = ''
    for i in range(len(plaintext)):
        m = ALPHABET.find(plaintext[i])
        k = ALPHABET.find(passphrase[i % len(passphrase)])
        c = (m + k) % len(ALPHABET)
        ciphertext = ciphertext + ALPHABET[c]
    return ciphertext

def vingenere_decrypt(ciphertext, passphrase):
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ALPHABET.find(ciphertext[i])
        k = ALPHABET.find(passphrase[i % len(passphrase)])
        m = (c - k) % len(ALPHABET)
        plaintext = plaintext + ALPHABET[m]
    return plaintext

def main():
    text = input("Enter text: ")
    passphrase = input("Enter passphrase (precede with '-' to decrypt): ")
    if passphrase[0] == '-':
        print(f"Plain Text = '{vingenere_decrypt(text, passphrase[1:])}'")
    else:
        print(f"Cipher Text = '{vingenere_encrypt(text, passphrase)}'")

main()