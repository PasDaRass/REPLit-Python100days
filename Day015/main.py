exit_query = ""

while exit_query != "yes":
  animal_query = input("What animal sound do you want? ").lower()
  print()
  if animal_query == "dog":
    print("woof")
  elif animal_query == "cat":
    print("meow")
  elif animal_query == "bird":
    print("tweet")
  elif animal_query == "snake" or animal_query == "python":
    print("ssssssssssssssssssssssss")
  elif animal_query == "cow":
    print("moo")
  elif animal_query == "sheep":
    print("baa")
  elif animal_query == "bee" or animal_query == "wasp":
    print("buzzzz")
  elif animal_query == "fox":
    print("Gering-ding-ding-ding-dingeringeding!")
    print("Wa-pa-pa-pa-pa-pa-pow!")
    print("Hatee-hatee-hatee-ho!")
    print("Joff-tchoff-tchoffo-tchoffo-tchoff!")
  else:
    print("I don't know that animal unfortunately")
  print()
  exit_query = input("Do you want to exit? ").lower()
