############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random

from art import logo
from Functions import playerScore,checkWinner,clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackJack ():
    print(logo)
    gameSwitch = True

    playerCards = []
    computerCards = []

    for i in range(2):
        playerCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))

    while gameSwitch:

        currentScore = playerScore(playerCards)
        computerScore = playerScore(computerCards)
        print(f"Your cards: {playerCards}, current score: {currentScore}")
        print(f"Computer's first card: {computerCards[0]}")

        anotherCard = ""
        if currentScore < 21:
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

        if anotherCard == "y":
            playerCards.append(random.choice(cards))
            currentScore = playerScore(playerCards)
        else:
            while computerScore < 17:
                computerCards.append(random.choice(cards))
                computerScore = playerScore(computerCards)

            print(f"Your final hand: {playerCards}, final score: {currentScore}")
            print(f"Computer's final hand: {computerCards}, final score: {computerScore}")

            results = checkWinner(currentScore, computerScore)
            if results == "player":
                print(f"You Win 😎")
            elif results == 'computer':
                print(f"Computer Wins 😭")
            else:
                print(f"It was a Draw 🤯")

            gameSwitch = False


gameController = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while gameController == 'y':
    clear()
    blackJack()
    gameController = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
