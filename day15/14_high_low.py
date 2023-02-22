from game_data import data
import random
from art import logo, vs


def random_account():
    account = random.choice(data)
    return account


def format_account(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check(account_a_follower, account_B_follower, answer):
    if account_a_follower > account_B_follower:
        return answer == "a"
    else:
        return answer == "b"


score = 0
game_over = False
account_B = random_account()
print(logo)

while not game_over:
    account_A = account_B
    account_B = random_account()
  
    while account_B == account_A:
        account_B = random_account()

    print(f"Compare A: {format_account(account_A)}")
    print(vs)
    print(f"Against B: {format_account(account_B)}")

    answer = input("\nWho has more followers? Type 'A' or 'B'").lower()
    account_a_follower = account_A['follower_count']
    account_b_follower = account_B['follower_count']
    is_correct = check(account_a_follower, account_b_follower, answer)
  
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! your current score: {score}")
    else:
        print(f"You're wrong! your final score: {score}")
        game_over = True
