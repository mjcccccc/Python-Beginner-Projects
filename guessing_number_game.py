"""
Title of the project: Number Guessing Game 
Date: March 21, 2024
"""
import random

# Function to count the number of guesses it takes to find the correct number
def countTheGuess(numberToBeGuessed):
    is_iterate = True
    minimumGuess = 5  # Minimum number of guesses allowed
    countGuess = 1  # Initialize the guess count

    # Loop the game 
    while is_iterate:
        guess = int(input("Your Guess: "))  # Take user input for the guess
        if guess != numberToBeGuessed:
            # Check if the number of guesses is within the minimum limit
            if countGuess < minimumGuess:
                # Provide feedback to the user based on their guess
                if guess > numberToBeGuessed:
                    print("Try Again! You guessed too high")
                else:
                    print("Try Again! You guessed too small")
                countGuess += 1  # Increment guess count
            else:
                # If the user exhausts the allowed guesses
                print("Out of guesses, Better luck next time!")
                is_iterate = False
        else:
            # If the user guesses the correct number
            print("Congratulations you did it in %d attempts" % countGuess)
            is_iterate = False

if __name__ == "__main__":
    print("---Guessing a Number Game---")
    # Take input for the range within which the number is to be guessed
    lowerBound = int(input("Enter a Starting Range: "))
    upperBound = int(input("Enter a End Range: "))
    
    # Generate a random number within the specified range
    numberToBeGuessed = random.randint(lowerBound, upperBound)
    
    # Call the function to start the game
    countTheGuess(numberToBeGuessed)
