# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Without len & sum function
# sum = (sum(student_heights))
total_heights = 0
for height in student_heights:
  total_heights += height
print(total_heights)

# len = (len(student_heights))
number_of_students = 0
for number in student_heights:
  number_of_students += 1
print(number_of_students)

# With len & sum function
# ppl = (len(student_heights))
# sum = (sum(student_heights))
# average_height = (round(sum/ppl))
# print(average_height)
