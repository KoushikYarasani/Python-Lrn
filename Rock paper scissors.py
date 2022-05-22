#imports
from ast import Break
import random
import os
from time import *

#Rock,Paper and SCISSORS
rock = '''
    _______
---'   ____)
      (_____)
      (_____) ROCK🗿
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______) PAPER📃
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________) SCISSORS✂️
      (____)
---.__(___)
'''

#Main code
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
variable = [rock,paper,scissors]
User_points = 0
Comp_points = 0
Best_of = int(input("How much best u want this game: "))

while User_points != Best_of and Comp_points != Best_of:
    
    #User_Input
    User_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    print(variable[User_choice])

    #line print
    print("            Player            ")
    print("_____________\VS/_____________")
    print("           Computer           ")

    #Computer_Randomization
    int_comp_choice = len(variable)
    random_comp_choice = random.randint(0, int_comp_choice - 1)
    print(variable[random_comp_choice])

    #conditional statements
    if User_choice == 0 and random_comp_choice == 0:
        print("Its a draw.")
    elif User_choice == 1 and random_comp_choice == 1:
        print("Its a draw.")    
    elif User_choice == 2 and random_comp_choice == 2:
        print("Its a draw.")
    elif User_choice == 0 and random_comp_choice == 1:
        print("Computer Wins.")
        Comp_points += 1
    elif User_choice == 1 and random_comp_choice == 0:
        print("You Wins.")
        User_points += 1
    elif User_choice == 1 and random_comp_choice == 2:
        print("Computer Wins.")
        Comp_points += 1
    elif User_choice == 2 and random_comp_choice == 1:
        print("You Wins.")
        User_points += 1
    elif User_choice == 0 and random_comp_choice == 2:
        print("You Wins.")
        User_points += 1
    else:
        print("Computer Wins.")
        Comp_points += 1
    
    sleep(3.00)
    cls()

#Winner message
points_display = (f"Player Points:   {User_points} |\n|Computer Points: {Comp_points}") 
print("---------------------")
print("|"+points_display+" |")
print("---------------------")

if User_points == Best_of:
    print("###########################################################################")
    print("###########################################################################")
    print("##########################🥳🥳Player Wins🥳🥳#############################")
    print("###########################################################################")
    print("###########################################################################")
elif Comp_points == Best_of:
    print("###########################################################################")
    print("###########################################################################")
    print("###########################🥳🥳Computer Wins🥳🥳#########################")
    print("###########################################################################")
    print("###########################################################################")   
else:
    print("👎👎👎Game is Draw!!!👎👎👎")

   

