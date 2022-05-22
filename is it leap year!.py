#welcome code
print("#####################################################")
print("##########|Welcome to know it is leap year|##########")
print("#####################################################")

#code
year = int(input("Write the year u want to know: "))

#conditional
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
