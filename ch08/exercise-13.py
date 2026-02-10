# Write a program to plot a horizontal bar chart of student exam scores.
# First prompt the user to enter the number of scores. Then use a counted
# loop to get input from the user. Each line of input contains a student’s
# last name followed by a score in the range 0-100. Your program should
# draw a horizontal rectangle for each student where the length of the bar
# represents the student’s score. The bars should all line up on their
# lefthand edges. Hint: Use the number of students to determine the size of
# the window and its coordinates. Bonus: Label the bars at the left end with
# the students’ names.

def main():
    nscores = int(input("Number of scores: "))
    table = ""
    max_name_length = 0
    for i in range(nscores):
        s = input("Last name & score: ")
        (lastname, score) = s.split(maxsplit=2)
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