#Write your code below this row 👇

for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    number = "feezbuzz"
  elif number % 3 == 0:
#    and number % 5 != 0:
    number = "feez"
  elif number % 5 == 0: 
    # and number % 3 != 0:
   number = "buzz"
  print(number)