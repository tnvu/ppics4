# Extend the previous program to censor all of the .txt files in a directory
# and place the censored versions into a subdirectory called censored.

import pathlib

def main():
    inDir = pathlib.Path(input("Enter directory name: "))

    censorFile = input("Enter censor filename: ")
    censorWords = []
    with open(censorFile, 'r') as f:
        for l in f:
            censorWords.append(l.strip())

    for inFile in inDir.glob("*.txt"):
        outDir = pathlib.Path(inDir.joinpath("censored"))
        if not outDir.exists():
            outDir.mkdir()
        outFile = pathlib.Path(outDir.joinpath(inFile.name))
        with inFile.open() as f, outFile.open('w') as out:
            for l in f:
                for w in l.split():
                    if w in censorWords:
                        out.write('*' * len(w))
                    else:
                        out.write(w)
                out.write('\n')

main()