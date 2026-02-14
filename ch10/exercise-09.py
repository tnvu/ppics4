# Write an automated censor program that reads in the text from a file and
# creates a new file where all of the four-letter words have been replaced by
# "****". You can ignore punctuation, and you may assume that no words in the
# file are split across multiple lines.

def main():
    inFile = input("Enter a filename: ")
    with open(inFile, 'r') as f:
        for l in f:
            words = l.split()
            for w in words:
                if len(w) == 4:
                    print('****', end=' ')
                else:
                    print(w, end=' ')
            print()

main()