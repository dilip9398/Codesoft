import random
from random import choice

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

print("Welcome to the Game!")
print("Start! Rock , paper, scissors") #Choose among these!
player = input("You choose : ").lower()
#User choices
if player == "rock":
    print(rock)
elif player ==  "paper":
    print(paper)
elif player == "scissors":
    print(scissors)
else:
    print("Your entered Invalid input! You Lost!")
    exit()



#Computer random choices
print("Computer choose")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
else:
    print(scissors)

#Prints who is the winner or match is draw
if player == computer:
    print("Match is draw!")
elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            print("You win!")
else:
    print("Computer wins!")
