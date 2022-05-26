import random
from art import logo

price_money = "1Million dollars"
print(logo)
print("Welcome to Guess the Number challenge!")

easy_level_atempts = 10
hard_level_atempts = 5

number = random.randint(1, 101)
atempts = 0
print("You must guess number between 1 to 100")
level = input("What level do u want 'easy' or 'hard': ").lower()

if level == "easy":
  print("You have 10 atempts to guess the number")
  atempts = easy_level_atempts
else:
  print("You have 5 atempts to guess the number")
  atempts = hard_level_atempts

while atempts != 0:
  user_number = int(input("What did u guess: "))
  
  if user_number > number:
    atempts -= 1
    print("Too Big.try lower")
    print(f"Still {atempts} atempts left.")
    print("--------------------------------------------------------")
  elif user_number < number:
    atempts -= 1
    print("Too Lower.try bigger")
    print(f"Still {atempts} atempts left.")
    print("--------------------------------------------------------")
  elif user_number == number:
    print(f"You got it its {number}")
    print(f"You won {price_money}")
    print("--------------------------------------------------------")
    atempts = 0
  else:
    print(f"Sorry you lost this game and losed 🎉{price_money}🎉")