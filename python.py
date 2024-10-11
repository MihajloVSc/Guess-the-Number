import random

def game():
    the_number = random.randint(1, 100)
    input_number = None
    guess_number = 0
    
    while the_number !=  input_number:

        input_number = int(input('guess the number between  1 and 100 >>   '))

        guess_number += 1

        if input_number < the_number:
            print("The number is bigger.")
        elif input_number > the_number:
            print("The number is smaller.")
        else:
            print(f"You have guessed a number is {guess_number}. try.")



    
game()


    
