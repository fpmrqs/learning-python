import random

def guess(number):
  random_number = random.randint(1, number)
  guess = 0

  while guess != random_number:
    guess = int(input("guess the number: "))
    if guess < random_number:
      print("Too low!")
    elif guess > random_number:
      print("too high!")
    
  print(f"Well done you guessed {random_number}")

def computer_guess(number):
  low = 1
  high = number
  feedback = ""

  
  while feedback != "c":
    guess= random.randint(low, high)
    feedback = input(f"{guess}. What's the feedback")
    if  feedback == "high":
      high = guess - 1
    elif feedback == "low":
      low = guess - 1
    
  print("Well done")

computer_guess(30)

  