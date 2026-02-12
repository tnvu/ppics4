# Write a program to draw a quiz score histogram. Your program should get
# the numbers from the user on a single line of input. Each number is a score
# in the range 0-10. Your program must count the number of occurrences of
# each score and then draw a vertical bar chart with a bar for each possible
# score (0-10), with a height corresponding to the count of that score. For
# example, if 15 students got an 8, then the height of the bar for 8 should
# be 15. Hint: Use a list that stores the count for each possible score. An
# example histogram is shown below:

### COPIED FROM CH09 EXERCISE 06 ###
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def main():
    scores = input("Enter the list of scores: ").split()
    toNumbers(scores)

    histogram = [0] * 11
    max_height = 0
    for s in scores:
        histogram[s] = histogram[s] + 1
        if histogram[s] > max_height:
            max_height = histogram[s]

    print()
    for i in range(max_height, 0, -1):
        for j in histogram:
            c = ""
            if j >= i:
                c = "#"
            print(f'{c:^3}', end='')
        print()
    for i in range(len(histogram)):
        print(f"{i:^3}", end='')
    print()

main()