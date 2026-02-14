# Write a program to administer a multiple-choice quiz. The questions for
# the quiz are stored in a text file. Each question comprises five lines of
# text. The first line is the question, and the following four lines are the
# possible answers. The line with the correct answer starts with an asterisk
# (“*”). One or more blank lines separate one question from the next.
# Your program should prompt the user for the path to the file containing
# the quiz and should then display the questions one at a time. The displayed
# answers should be labeled with a, b, c, d. Obviously, the asterisk that
# marks the correct answer should not be shown. The user types in the label
# to answer the question.
# The program should keep track of how many answers the user gets
# correct and show the score when the quiz has been completed.

import pathlib

def getQuestionLines(f):
    lines = []
    for line in f:
        line = line.strip()
        if line != "":
            lines.append(line.strip())
        if len(lines) == 5:
            return lines
    return None

def correctAnswer(choices):
    answer = None
    for i in range(len(choices)):
        choice = choices[i]
        if choice[0] == '*':
            choice = choice[1:]
            answer = i
        print(f'{chr(ord('a') + i)}) {choice}')
    response = input("Enter response: ")
    response = response.strip()
    response = ord(response[0].lower()) - ord('a')
    return answer == response

def main():
    inFile = pathlib.Path(input("Enter quiz filename: "))
    nQuestions = 0
    nCorrect = 0
    with inFile.open() as f:
        while True:
            questionLines = getQuestionLines(f)
            if questionLines is None:
                break
            print(questionLines[0])
            nQuestions = nQuestions + 1
            if correctAnswer(questionLines[1:]):
                nCorrect = nCorrect + 1
    print(f"Number of correct responses: {nCorrect} out of {nQuestions}")

main()