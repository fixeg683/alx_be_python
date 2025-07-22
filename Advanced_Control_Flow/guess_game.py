import random  # Import the random module to generate random numbers

# Function that runs a single round of the guessing game
def play_game():
    secret_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    guess_count = 0  # Initialize a counter to track number of guesses

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    # Loop to keep prompting the user until they guess correctly
    while True:
        try:
            guess = int(input("Enter your guess: "))  # Get the user's guess and convert to integer
            guess_count += 1  # Increment guess counter

            # Match-case block to handle different guess outcomes
            match guess:
                case _ if guess == secret_number:
                    print("🎉 Congratulations, you guessed it!")  # Correct guess
                    print(f"It took you {guess_count} guess(es).")  # Display total attempts
                    break  # Exit the loop once guessed correctly
                case _ if guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")  # Guess too high
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")  # Guess too low
        except ValueError:
            print("Please enter a valid integer.")  # Handle non-integer input gracefully

# Loop to allow user to play multiple rounds
while True:
    play_game()  # Start a new game round
    again = input("Play again? (yes/no): ").strip().lower()  # Ask if the user wants to play again
    if again != "yes":
        print("Thanks for playing! Goodbye!")  # Exit message
        break  # Exit the loop if the user doesn't want to play again
