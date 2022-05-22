#imports
import random

#welcome code
print("##########################################################")
print("###############|WELCOME TO HAKY RESTUARANT|###############")
print("##########################################################")

#input
names = input("What are u your names write here and we will randomly select use ,  and separate each one: ")
names = names.split(", ")

#random
names_numbers = len(names)
name = random.randint(0, names_numbers -1)
name = names[name]
name = name[0].upper() + name[1:].lower()
print(f"{name} have to pay the bill!")
