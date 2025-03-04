import random


def roll_dice(sides):
  return random.randint(1, sides)


def roll6_and_roll8():
  return roll_dice(6) * roll_dice(8)


generate_stats = True
while generate_stats == True:
  player_name = input("Name your character: ")
  health_stats = roll6_and_roll8()
  print("Their health is", str(health_stats) + "hp")
  reroll = ""
  while reroll != "Y" and reroll != "N":
    reroll = input("Try a new character? Y or N : ").upper()
    if reroll == "Y":
      break
    elif reroll == "N":
      generate_stats = False
      break
    else:
      continue
