# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# import art
# print(art.logo)
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find_highest_bidder(bid_dict1):
    highest = 0
    winner = ""
    for key in bid_dict1:
        bid_amount = bid_dict1[key]
        if bid_amount > highest:
            highest = bid_dict1[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest}")

bid_dict = {}
bidding_on = True
while bidding_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    cont = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if cont != 'yes':
        bidding_on = False
        find_highest_bidder(bid_dict)

