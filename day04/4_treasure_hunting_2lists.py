
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

map[column - 1][row - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# # my idea

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# column = position[0]
# row = position[1]

# if column == "1" and row == "1":
#   row1[0]="X"
# elif column == "2" and row == "1":
#   row1[1]="X"
# elif column == "3" and row == "1":
#   row1[2]="X"
# elif column == "1" and row == "2":
#   row2[0]="X"
# elif column == "2" and row == "2":
#   row2[1]="X"
# elif column == "3" and row == "2":
#   row2[2]="X"
# elif column == "1" and row == "3":
#   row3[0]="X"
# elif column == "2" and row == "3":
#   row3[1]="X"
# elif column == "3" and row == "3":
#   row3[2]="X"
