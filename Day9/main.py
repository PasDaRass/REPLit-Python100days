# type casting

dob = int(input("What year were you born? "))

if 1925 <= dob <= 1946:
  print("Your generation is... Traditionalists!")
elif 1947 <= dob <= 1964:
  print("Your generation is... Baby Boomers!")
elif 1965 <= dob <= 1981:
  print("Your generation is... Generation X!")
elif 1982 <= dob <= 1995:
  print("Your generation is... Millenials!")
elif 1996 <= dob <= 2015:
  print("Your generation is... Generation Z!")
else:
  print("Your answer falls outside the scope of this list")
