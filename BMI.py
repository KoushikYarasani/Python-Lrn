#tilte of code
print("####################|BMI CALCUTATER|####################")

#input height and weight
height = input("What is your height in metres: ")
weight = input("What is your weight in kilograms: ")

#converting datatypes
final_height = float(height)
final_weight = int(weight)

#calculating BMI
BMI = final_weight / final_height ** 2
final_bmi = int(BMI)

#printing BMI
print(final_bmi)

#ranging BMI
if final_bmi > 18 and final_bmi < 25:
    print("Your bmi is in normal range")
elif final_bmi < 30 and final_bmi > 25:
    print("Your bmi is in overweight range")
elif final_bmi > 30:
    print("You got obesity")
elif final_bmi < 18:
    print("Your bmi is in underweight range")
else:
    print("Information not valid")