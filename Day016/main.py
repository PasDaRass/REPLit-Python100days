attempts_left = 3
print("Guess the missing lyrics")

while attempts_left != 0:
  print()
  print("You have", attempts_left, "attempts left")
  print()
  print("I tried so hard and got so far")
  print("But __ ___ ___, it doesn't even matter")
  print("I had to fall to lose it all")
  print("But __ ___ ___, it doesn't even matter")
  print()
  if attempts_left == 1:
    print("Clue: The lyrics are the same as the song title")
    print()
  answer = input("What are the lyrics? ").lower()
  if answer == "in the end":
    print("Well done, you got the right answer!")
    break
  else:
    print("That's not it, try again...")
    attempts_left -= 1
