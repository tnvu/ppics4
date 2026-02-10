# Write a program that calculates the average word length in a sentence
# entered by the user.

def main():
    s = input("Enter sentence: ")

    num_words = 0
    total_word_length = 0
    for w in s.split():
        num_words = num_words + 1
        total_word_length = total_word_length + len(w)
    print(f"Average word length = {total_word_length / num_words}")

main()