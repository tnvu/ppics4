# Extend the program from the previous exercise to accept a file of words to
# be censored as another input. The words in the original file that appear in
# the censored words file are replaced by a string of "x"s with length equal
# to the number of characters in the censored word.

def main():
    txtFile = input("Enter text filename: ")

    censorFile = input("Enter censor filename: ")
    censorWords = []
    with open(censorFile, 'r') as f:
        for l in f:
            censorWords.append(l.strip())
    with open(txtFile, 'r') as f:
        for l in f:
            for w in l.split():
                if w in censorWords:
                    print('*' * len(w), end='')
                else:
                    print(w, end='')
            print()

main()