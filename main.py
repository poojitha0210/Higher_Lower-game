from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()




























# from art import logo,vs
# from game_data import data
# import random
# from replit import clear
# def data_list(account):
#   acc_name=account["name"]
#   acc_description=account["description"]
#   acc_country=account["country"]

#   return f"{acc_name}, a {acc_description} from {acc_country}"

# def game(guess,choice1_count,choice2_count):
#   if choice1_count>=choice2_count:
#       return guess=='A'

#   else:
#       return guess=='B'
    
# print(logo)
# choice2=random.choice(data)
# count=0
# game_continue=True
# choice1=choice2
# choice2=random.choice(data)
# while choice1==choice2:
#    choice2=random.choice(data)
  
# while game_continue:
#   print(f"Compare A: {data_list(choice1)}")
#   print(vs)
#   print(f"Against B: {data_list(choice2)}")
#   guess=input("Who has more followers? Type 'A' or 'B':").upper()
  
#   choice1_count=choice1["follower_count"]
#   choice2_count=choice2["follower_count"]
#   is_correct=game(guess,choice1_count,choice2_count)

#   clear()
#   print(logo)
#   if is_correct:
#     count+=1
#     print(f"You are right, current score is {count}.")
#   else:
#     print(f"Sorry, that's wrong. Final score {count}.")
