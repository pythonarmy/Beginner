#get the number of student
NUMBER_OF_STUDENT = int(input())
#list to hold the student names and grades
STUDENT = []
#list to hold student scores
STUDENT_SCORE = []


for i in range(NUMBER_OF_STUDENT):
    """
    get student names, scores and adds them to the list
    """
    names = input()
    score = float(input())
    STUDENT_SCORE.append(score)
    STUDENT.append([names, score])

#sorts student details alphabetically
SORT_STUDENT = sorted(STUDENT)
#gets the second lowest mark from the student score
SECOND_LOWEST = sorted(list(dict.fromkeys(STUDENT_SCORE)))[1]
#compares the score with the second lowest score 
#prints the name of student if score equals second lowestscore
for name, score in SORT_STUDENT:
    if SECOND_LOWEST == score:
        print(name)
