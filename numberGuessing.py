import random

print(" || Welcome to the Number Guessing game || ")
print(" I'm thinking of a number between 1 and 100. ")

choice = input("Choose a difficulty 'easy' or 'hard' : ").lower()
num_to_guess = int(random.randint(1,100))

def play_game(number):
    attempts = 0
    if choice == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")

    found_it = False
    guess = int(input("Make a guess : "))
    while attempts != 1:
    #for i in range(attempts-1):
        if guess == number:
            found_it = True
            print(f"You got it! The answer was {number}.")
        elif guess < num_to_guess:
            print("Too low.")
        elif guess > num_to_guess:
            print("Too high.")

        guess = int(input("Guess again."))
        attempts -= 1
    if not found_it or attempts == 0:
        print("You 've run out of guesses. Try again.")


play_game(num_to_guess)
