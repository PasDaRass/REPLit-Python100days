import random

sides = int(input("How many sides? "))

def roll_dice(sides):
  print("You rolled", random.randint(0, sides))

roll_dice(sides)

answer = "yes"

while answer != "n":
  answer = input("Roll again? ").lower()
  if answer != "y" and answer != "n":
    print("Only reply with Y for yes, or N for no")
  elif answer == "n":
    break
  else:
    roll_dice(sides)
