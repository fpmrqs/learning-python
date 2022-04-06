import random

def play():
  user = input("type r for rock, p for paper and s for scissors: ")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    print("It's a tie!")
    return
  
  if youWin(user, computer):
    print("You win!")
    return
  
  print("You lose!")

def youWin(user, computer):
  if (user == 's' and computer == 'p') or (user == 'p' and computer == 's') or (user == 'r' and computer == 's'):
    return True

play();
