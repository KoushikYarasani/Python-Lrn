#welcome code
print("#############################################")
print("#################|Max Score|#################")
print("#############################################")

#inputing
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

#Code
max_score = 0
for i in student_scores:
    if i > max_score:
        max_score = i
print(f"The highest score in the class is: {max_score}")