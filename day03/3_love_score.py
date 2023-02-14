# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name12_lower = name1.lower() + name2.lower()

t = name12_lower.count("t")
r = name12_lower.count("r")
u = name12_lower.count("u")
e = name12_lower.count("e")

true=(t+r+u+e)

l = name12_lower.count("l")
o = name12_lower.count("o")
v = name12_lower.count("v")
love=(l+o+v+e)

# true_s=str(true)
# love_s=str(love)
love_score=int(str(true)+str(love))
# true_love=int(true_s+love_s)

if (love_score) < 10 or (love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score) > 40 and (love_score) < 50:
  print (f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

  




# T_name1 = name1_lower.count("t")
# R_name1 = name1_lower.count("r")
# U_name1 = name1_lower.count("u")
# E_name1 = name1_lower.count("e")

# T_name2 = name2_lower.count("t")
# R_name2 = name2_lower.count("r")
# U_name2 = name2_lower.count("u")
# E_name2 = name2_lower.count("e")

