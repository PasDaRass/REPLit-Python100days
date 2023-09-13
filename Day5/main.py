# If/ Else Statements

print("Which character are you? Harry Potter Edition")
print("--")
answer1 = input("Are you in Gryffindor? ")
if answer1.lower() == "no":
  print("You are Malfoy")
else:
  answer2 = input("Do you wear glasses? ")
  if answer2.lower() == "yes":
    print("You are Harry")
  else:
    answer3 = input("Are you a boy? ")
    if answer3.lower() == "yes":
      print("You are Ron")
    else:
      print("You are Hermione")
