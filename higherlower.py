import random
from art import highlow
from art import vs
from game_data import data

def format_data(account):
    name = account["name"]
    desc = account["description"]
    cntry = account["country"]
    return f"{name}, a {desc}, from {cntry}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
continue_playing = True
account_b = random.choice(data)

while continue_playing:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You win. Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_playing = False
