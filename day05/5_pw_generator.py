#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# pw = ""
#
# for p in range(nr_letters):
#   pw += random.choice(letters)
# for p in range(nr_numbers):
#   pw += random.choice(numbers)
# for p in range(nr_symbols):
#   pw += random.choice(symbols)
#
# print(pw)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pw_list = []

for p in range(nr_letters):
  pw_list += random.choice(letters)
for p in range(nr_numbers):
  pw_list += random.choice(numbers)
for p in range(nr_symbols):
  pw_list += random.choice(symbols)


random.shuffle(pw_list)
print(''.join(pw_list))

# password=""
#
# for char in range(nr_letters):
#     password += random.choice(letters)
# for char in range(nr_numbers):
#     password += random.choice(numbers)
# for char in range(nr_symbols):
#     password += random.choice(symbols)
#
# password.split()
# random.shuffle(password)
# print(password.join())
