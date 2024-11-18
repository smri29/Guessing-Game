import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100. You have 10 attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            attempts += 1
            difference = abs(number_to_guess - guess)

            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
                break
            elif difference >= 50:
                print("Too far!")
            elif difference >= 20:
                print("Far!")
            elif difference >= 10:
                print("Close!")
            else:
                print("Very close!")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing! Goodbye.")


# Start the game
play_game()
