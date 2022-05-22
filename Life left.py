#welcome code
print("##################|How many days you have|##################") 

#inputing age
age = input("What is your current age: ")
print(age)

#converting
age_int = int(age)
years_remaining = 70 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

#printing
life_left = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months remaining"
print(life_left)  



