student_heights = input("Input a list of student heights ").split()
length = 0
sum = 0
for n in range(0, len(student_heights)):
    length += 1
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    average = round(sum/length)
print(average)
