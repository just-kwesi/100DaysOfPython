import os
from art import logo


def clear():
    os.system('clear')


print(logo)
print('Welcome to the secret auction.')

ctrl = True
bids = {}

while ctrl:
    name = input('What is your name? : ')
    bid = input("What's your bid?: $")
    biddersCheck = input("Are there any other bidders? Type 'yes' or 'no'. ")

    bids[name] = bid

    clear()
    if biddersCheck != 'yes':
        ctrl = False

bidWinnerName = ""
bidWinAmount = 0
for key, value in bids.items():
    if int(value) > bidWinAmount :
        bidWinnerName = key
        bidWinAmount = int(value)

print(f"The winner is {key} with a bid of ${value}.")
