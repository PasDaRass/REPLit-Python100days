# User input with if / elif / else

anime = input("What's your favorite anime? ")
if anime.lower() == "naruto":
  print("Yes! Naruto is such a great anime!")
  character = input("Who is your favorite character? ")
  if character.lower() == "rock lee":
    print("Rock Lee is my favorite character too!")
  else:
    print("Cool choice! I prefer Rock Lee though")
elif anime.lower() == "bleach":
  print("I really like Bleach as well!")
  character = input("Who is your favorite character? ")
  if character.lower() == "shunsui":
    print("Shunsui is so cool! You have good taste")
  else:
    print("Nice, I would choose Shunsui as my favourite")
else:
  print("I'm glad you like that show")
