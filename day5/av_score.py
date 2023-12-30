student_scores = input("Input a list of student scores").split()
max = 0

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n]>max:
        max = student_scores[n]
print(max)
