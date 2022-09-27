import random

guesses = 0

top_of_range = input("Enter the range: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than zero")
        quit()
        
else:
    print("please enter a number!")
    quit()
        
random_number = random.randint(1, top_of_range)

while True:
    
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please enter a number!")
        continue
        
    guesses += 1
    
    if user_guess == random_number:
        print("You guesses it right")
        break
    else:
        print("You got it wrong.")
    
print("You guessed it in", guesses, "guesses")
        

        
    
    
    
    