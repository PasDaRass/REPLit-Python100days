# Input and arithmetic

net_bill = float(input("What was the bill?: "))
number_of_people = int(input("How many people?: "))
tip = int(input("What percentage would you like to tip?: "))
gross_bill = net_bill + (net_bill * (tip / 100))
# or
# gross_bill = net_bill / 100 * (tip + 100)
answer = round(gross_bill / number_of_people, 2)
print("The final amount is", gross_bill)
print("You all owe", answer, "each.")
