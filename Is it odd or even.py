#welcome code
print("###########################################")
print("###############|odd or even|###############")
print("###########################################")

#Input
number = int(input("Type the number to know wheather it is odd or even: "))

#conditional statements
number = number % 2
if number == 0:
    print("It is even number")
else:
    print("It is odd number")