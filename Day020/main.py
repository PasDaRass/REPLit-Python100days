print("Lets count in steps!")
print("I need a starting number, ending number and the steps")
print()
start_num = int(input("What is the starting number: "))
end_num = int(input("What is the ending number: ")) + 1
steps = int(input("How many steps should I count in: "))

for i in range(start_num, end_num, steps):
  print(i)
