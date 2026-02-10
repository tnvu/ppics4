# Write a program that counts the number of words in a sentence entered
# by the user.

def main():
    s = input("Enter sentence: ")
    print("Number of words =", len(s.split()))

main()