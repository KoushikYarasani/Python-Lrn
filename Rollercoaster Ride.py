#Welcome code
from ast import Break


print("#####################|Welcome to Rollercoaster Ride|#####################")

#input
height = int(input("What is your height in centemetres: "))
bill = 0

#conditional statements
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? : "))
    if age <= 12:
        bill = 5
        print("Child ticket $5")
    elif age < 18:
        bill = 7
        print("Teen ticket $7")
    elif age > 45 and age < 60:
        bill = 0
        print("Senior citizen Free ticket")
    elif age < 45:
        bill = 12
        print("Adult ticket $12")
    elif age == 69:
        print("Ayy ayyy!! masthu shades ni la")
        Break
    else:
        print("Pakkakipora musaloda!")
        Break 
    want_photo = input("If you want photos type 'Y',if dont want type 'N': ")
    if want_photo == "Y" or want_photo == "y":
        bill += 3
        print(f"Your total bill is: ${bill}")
    else:
        print(f"Your total bill is: ${bill}")

else:
    print("Sorry, You have to grow taller to ride")