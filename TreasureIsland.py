print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# could also can use below instead of multiple spelling checks
# firstInput = input().lower()
firstInput = input('''You're at a cross road. 
            Where do you want to go? Type "left" or "right"''')
if firstInput not in ("left","LEFT","Left"):
    print("Fall in to a hole! GAME OVER!")
else:
    secondInput = input('''You have come to a lake. 
    There is an island in the middle of the lake.
    Type "wait" to wait for a boat. 
    Type "swim" to swim across.''')
    if secondInput not in ("wait","Wait","WAIT"):
        print("Attacked by trout! GAME OVER!")
    else:
        thirdInput = input('''You arrive at the island unharmed.
        There is a house with 3 doors.
        One red, one yellow, one blue. 
        Which color do you choose?''')
        if thirdInput in ("Red", "red","RED"):
            print("Burned by fire. GAME OVER!")
        elif thirdInput in ("Blue", "blue", "BLUE"):
            print("Eaten by Beasts. GAME OVER!")
        elif thirdInput in ("Yellow", "yellow", "YELLOW"):
            print("You Win!!")
        else:
            print("GAME OVER!")