import random

def get_choices():
  while True:
    player_choice = input("Enter a choice(rock, paper, scissors) [Press q  for quit]: ").lower()
    if player_choice == "q":
      break
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    print(f"You choose {player_choice}, Computer choose {computer_choice}")
    winner = check_win(choices["player"], choices["computer"])
    print(winner)
  print("Thank  you for playing!!")

def check_win(player, computer):
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "paper":
      return "you loose"
    else:
      return "you won"
  elif player == "paper":
    if computer == "scissors":
      return "you loose"
    else:
      return "you won"
  elif player == "scissors":
    if computer == "rock":
      return "you loose"
    else:
      return "you won"  

get_choices()
