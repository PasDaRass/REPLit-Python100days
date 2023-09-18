# Print with colour and concatenation

print("\033[35mMINI ADVENTURE SIM")
print("\033[0m")
hero = input("What is your hero's name?\n\033[31m")
nemesis = input("\033[0mWhat is the name of your nemesis?\n\033[31m")
superpower = input("\033[0mWhat is your hero's superpower?\n\033[31m")
home = input("\033[0mWhere do you live?\n\033[31m")
food = input("\033[0mWhat is your favorite food?\n\033[31m")
print("\033[34m")

print("You are", hero, "who once prevailed against your enemy", nemesis, "using the power of", superpower, "whilst eating", food, "in", home)
