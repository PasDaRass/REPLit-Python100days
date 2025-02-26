number_prompt = int(input("What number should we use for our multiplication game?\nMultiples of "))
points = 0

for i in range(1, 11):
  answer = int(input("{} * {} = ".format(i, number_prompt)))
  if answer == i * number_prompt:
    print("That's right!")
    points+=1
  else:
    print("Wrong answer... It's", i * number_prompt)
print("")
print("You scored", points, "out of 10")

if points == 10:
  print("🏆 You got them all right! 🏆")
