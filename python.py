import random # First, we import the random module to generate random numbers.

def game(): # Define a function called game().
    the_number = random.randint(1, 100) # Generate a random number between 1 and 100 and assign it to 'the_number'.
    input_number = None # Initialize 'input_number' to None. This will store the user's guesses.
    guess_number = 0 # Initialize 'guess_number' to 0. This will count how many guesses the user has made.
    
    # Start a while loop that continues as long as 'the_number' is not equal to 'input_number'.
    while the_number !=  input_number:
        
        # Prompt the user to input a guess. The input is converted to an integer.
        input_number = int(input('guess the number between  1 and 100 >>   '))

        guess_number += 1 # Increment the guess counter by 1 for each guess.

        # Check if the guessed number is smaller than the actual number.
        if input_number < the_number:
            print("The number is bigger.") # Inform the user that the number they guessed is smaller.

        # Check if the guessed number is larger than the actual number.
        elif input_number > the_number:
            print("The number is smaller.") # Inform the user that the number they guessed is larger.

        # If the guessed number matches the actual number:
        else:
            # Print a message stating that the user has guessed the correct number, 
            # and how many tries it took.
            print(f"You have guessed a number in {guess_number}. try.")
    
# Call the game() function to start the game.
game()
