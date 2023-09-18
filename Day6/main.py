# Using elif

print("Try to brute force a username and password")

username = input("Input your Username: ")
password = input("Input your Password: ")

if username == "username" and password == "password":
  print("BORING! but sure, you found one")
elif username == "Python" and password == "100days":
  print("Good find! you got one!")
elif username == "Pas" and password == "byNumbers":
  print("You got me! Well done finding this one")
else:
  print("Login details not found, try try again :]")
