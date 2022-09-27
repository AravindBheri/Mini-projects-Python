import random

user_wins = 0
computer_wins = 0
draw = 0

choices = ["rock", "paper", "scissors"]

while True:
    
    computer_choice = random.choice(choices)
    
    user_choice = input("type ROCK/PAPER/SCISSORS? or Q to Quit ").lower()
    
    if user_choice == "q":
        break
    
    if user_choice not in choices:
        continue
    
    print("Computer picked", computer_choice)
    print("User picked", user_choice)
    
    if user_choice == computer_choice:
        print("DRAW.")
        draw += 1
    
    elif user_choice == "rock" and computer_choice == "scissors":
        print("User Won. :)")
        user_wins += 1
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("User Won. :)")
        user_wins += 1
        
    elif user_choice == "scissors" and computer_choice == "paper":
        print("User Won. :)")
        user_wins += 1
    else:
        print("Computer Won. :(")
        computer_wins += 1
        
print("User won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("DRAW", draw, "times")
print("BYE!!!!")
    
    
    
    