#import
import random

#welcome code
print("#########################################################")
print("####################|Heads and Tails|####################")
print("#########################################################")

#Code random
choose = input("Choose Heads or Tails: ").lower()
random_side = random.randint(0, 1)
if random_side == 1:
  coin ="heads"
else:
  coin = "tails"
if choose == coin:
    print(f"{coin} Wins")
else:
    print(f"{coin} Wins")
    
