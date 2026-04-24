import random
from art import logo

def deal_card():
    """ This in a function to deal random cards to the players """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_list):
  """ This is a function to calculate the scores/sum of the cards each player has drawn """
  score = sum(card_list)
    #if 11 in card_list and 10 in card_list and len(card_list) == 2:
    if score == 21 and len(card_list) == 2:
        score = 0
    elif score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
    return score

def compare(u_score, c_score):
  """ This is a function to compare the values of user and compueter to decide the winner """
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "Win, with a Blackjack."
    elif c_score == 0:
        return "Lose, Opponent has a Blackjack."
    elif u_score > 21:
        return "Lose, You went over."
    elif c_score > 21:
        return "Win, Opponent went over. "
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."

def play_game():
  """ This is a function that contains the main logic for playing the game """
    print(logo)
    user_card = []
    computer_card = []
    game_over = False
    comp_score = -1
    user_score = -1

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_card)
        comp_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
            if user_input == 'y':
                user_card.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_card.append(deal_card())
        comp_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer final hand: {computer_card}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()
