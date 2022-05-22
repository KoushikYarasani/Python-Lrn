#welcome code
print("##############################################################################")
print("##################|WELCOME to students average height check|##################")
print("##############################################################################")

#inputing
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] =   int(student_heights[n])

#code loop
#total heights
total_height = 0
for i in student_heights:
  total_height += i

#no of students
total_students = 0
for f in student_heights:
  total_students += 1

#final_printing
average = total_height / total_students
print(round(average))