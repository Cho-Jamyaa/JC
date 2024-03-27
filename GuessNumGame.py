import random

#Generate a Random number between 1 and 10
secret_number = random.randint(1, 10)

#maximum attempts allowed
max_attempts = 3


#Function to display a welcome message
def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")

#Function for recurwive guessing
    def guess_recursive(attempts_left):
        #Get user inout
        guess = int(input("\nGuess the number(between 1 and 10: "))

        #Check if the guess is correct
        if guess == secret_number:
            print("Congratualtions! You guess3d the correct number!")
        else: 
            print(f"Wrong guess. aAttempts left: {attempts_left-1}")
            if attempts_left> 1:
                #Make a recursive call for another guess
                guess(attempts_left - 1)
            else:
                print(f"\nSorry, you couldn't guess the correct number. the correct number was {secret_number}.")

            #Calling the function
                welcome_message()
                guess_recursive(max_attempts)

            #using id() to get memory attempts
                print(f"Memory address of secret number{secret_number} is: {id(secret_number)}")
