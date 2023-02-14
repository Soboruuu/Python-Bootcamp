from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def difficulty_level():
  level = input("Choose your difficult level. 'easy' or 'hard'?\n")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS

def check_answer(guess, number, turns):
  if guess == number:
    print(f"Yes, the number was {number}. You win!")
  # If player didn't, check if the number is higher or lower than player's guess.
  elif guess > number:
    print("Too high.")
    return turns -1   
  elif guess < number:
    print("Too low.")
    return turns -1

def game():
  print(logo)
  print("Welcome to the game of high or low.")
  print("I am thinking of a number between 1 to 100.")
  number = randint(1,100)
  turns = difficulty_level()
  guess = 0
  
  while guess != number:
    print(f"You have {turns} attempts left.")
    guess = int(input("Guess a number.: \n"))
    turns = check_answer(guess, number, turns)
    if turns == 0:
      print("You've run out of guesses. You lose")
      return
    elif guess != number:
      print("Guess again.")



game()
