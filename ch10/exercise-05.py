# Redo Exercise 13 from Chapter 8 to get its input from a file.

def main():
    inFile = input("Enter filename: ")
    with open(inFile, 'r') as f:
        table = ""
        max_name_length = 0
        for l in f:
            (lastname, score) = l.split(maxsplit=2)
            table = table + f"{lastname}\t{score}\n"
            if len(lastname) > max_name_length:
                max_name_length = len(lastname)
            for entry in table.split("\n"):
                if entry:
                    (lastname, score) = entry.split("\t", maxsplit=2)
                    score = int(score)
                    print(f"{lastname:>{max_name_length}} |", end='')
                    print("=" * (score // 10))
main()