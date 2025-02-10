subject = input("What subject was your test in? ")
max_score = int(input("What number is the maxiumum score? "))
your_score = int(input("What score did you receive? "))

grade_percentage = round((your_score / max_score) * 100, 2)
print()
if 90 <= grade_percentage <= 100:
  print("You got an A+ in", subject)
elif 80 <= grade_percentage < 90:
  print("You got an A- in", subject)
elif 70 <= grade_percentage < 80:
  print("You got a B in", subject)
elif 60 <= grade_percentage < 70:
  print("You got a C in", subject)
elif 50 <= grade_percentage < 60:
  print("You got a D in", subject)
else:
  print("You got an F in", subject)

print("Your grade percentage was", str(grade_percentage) + "%")
