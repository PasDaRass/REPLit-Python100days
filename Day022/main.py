import random

correct_number = random.randint(0, 1000000)
print("""
  Guess a number between 0 and 1,000,000 
  (Do not include commas in your answer)
  
Exit the game by guessing a negative number, eg. -1
  
""")
guess_number = 1000001
attempts = 0

while guess_number is not correct_number:
  guess_number = int(input("What is your guess? "))
  attempts += 1

  if guess_number == correct_number:
    print()
    print("You guessed the correct number! Well Done :]")
    print("It took you", attempts, "attempts to reach the answer")
    print()
    print("Thank you for playing")
    break
  elif guess_number < 0:
    print("You have exited the game")
    break
  elif guess_number < correct_number:
    print("Too low")
    continue
  elif guess_number > correct_number:
    print("Too high")
    continue
  else:
    print("You shouldn't be able to reach this condition")
