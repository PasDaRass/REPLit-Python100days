# if /elif /else dynamic

name = input("What's your name? ")
day = input("What day of the week is it? ")
interest = input("What do you love doing? ")

if day.lower() == "monday":
  print("Hi", name + "! I hope you enjoy", interest, "today.")
elif day.lower() == "tuesday":
  print(interest, name + ". What will they type next!?")
elif day.lower() == "wednesday":
  print(name, "no cares that you like", interest)
elif day.lower() == "thursday":
  print(interest, "who likes", name, "or is it", name, "liked by", interest)
elif day.lower() == "friday":
  print("Oh its a good day", name + ". let's try", interest)
else:
  print(name, "its the weekend... Programs need breaks too!")
