#Game of Rock, Paper, Scissors using user Input against Computer
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
user_choice = int(input('''What do you choose? Type 0 for Rock, Type 1 
for Paper, Type 2 for Scissors'''))

comp_choice = random.randint(0,2)
if user_choice > 2 or user_choice < 0:
    print("You have entered wrong input")
else:
    print(game_list[user_choice])
    print(game_list[comp_choice])
    if (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2):
        print("You Loose!!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0):
        print("You Loose!!")
    elif user_choice == comp_choice:
        print("Its a Draw!!")
    else:
        print("You Win!!")
