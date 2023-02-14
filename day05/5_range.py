# add all the numbers between 1 to 100
sum=0
for number in range(1,101):
    sum = sum + number
print (sum)

# add all the even numbers between 1 to 100
even=0
for number in range(1,101):
  if number % 2 == 0:
    even=even+number
print(even)