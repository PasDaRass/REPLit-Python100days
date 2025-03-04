import random, os

def scr_clear():
  os.system("clear")

def roll_dice(sides):
  return random.randint(1, sides)  

def character_details():
  char_name = input("Name your Hero or Villain: ")
  char_class = ""
  while char_class != "warrior" and char_class != "mage" and char_class != "rogue":
    scr_clear()
    char_class = input("What is your class [Warrior, Mage, Rogue] ? ").lower()
  return char_name, char_class

def generate_stats_health():
  return (roll_dice(6)*roll_dice(12)/2) + 10
  
def generate_stats_strength():
  return (roll_dice(6)*roll_dice(12)/2) + 12

running = True

while running:
  print("Fantasy Character Generator")
  print()
  char_name, char_class = character_details()
  char_health = generate_stats_health()
  char_strength = generate_stats_strength()
  scr_clear()
  print("Name:", char_name)
  print("Class:", char_class)
  print("Health:", char_health)
  print("Strenght:", char_strength)
  print()
  reroll=""
  while reroll != "Y" and reroll != "N":
    reroll = input("Generate a new character? Y or N").upper()
    if reroll == "Y":
      break
    elif reroll == "N":
      running = False
    else:
      continue
  scr_clear()
