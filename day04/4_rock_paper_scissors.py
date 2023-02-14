rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images = [rock, paper, scissors]
              # 0 ,   1   ,  2
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number. You lose.")
else:
    print(game_images[your_choice])
    computer_choice = int(random.randint(0,2))
    print("Computer choose\n" + game_images[computer_choice])

    if your_choice == computer_choice:
        print("It's a draw!")
    elif your_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and your_choice == 2:
        print("You lose!")
    elif your_choice < computer_choice:
        print("You lose!")
    elif your_choice > computer_choice:
        print("You win!")

   