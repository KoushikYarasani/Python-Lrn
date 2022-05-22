#welcome code
print("Welcome to Python Pizza Deliveries!")

#inputs
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#pizza,pepperoni,cheese rates
bill = 0
pepperoni_bill = 0
cheese_bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        pepperoni_bill += 2
    if extra_cheese == "Y":
        cheese_bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        pepperoni_bill += 3
    if extra_cheese == "Y":
        cheese_bill += 1
else:
    bill += 25
    if add_pepperoni == "Y":
        pepperoni_bill += 3
    if extra_cheese == "Y":
        cheese_bill += 1

#billing
total_bill = bill + pepperoni_bill + cheese_bill
print(f"Your final bill is: ${total_bill}")