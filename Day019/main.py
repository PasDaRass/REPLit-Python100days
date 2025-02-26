loan_amount = 1000
apr = 0.05

for year in range(10):
  loan_amount += loan_amount * apr
  print("You will owe", round(loan_amount, 2), "by year", year+1)
