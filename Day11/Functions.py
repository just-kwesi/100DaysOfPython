import os

def playerScore(cards):
    score = 0
    aceCount = 0

    for card in cards:
        if card == 11:
            aceCount += 1
            continue
        else:
            score += card

    aceScore = score + (aceCount * 11)
    if aceScore <= 21:
        return aceScore
    else:
        return aceCount + score


def checkWinner(player, computer):
    if (21 >= player and player > computer) or (player <= 21 and  computer >21):
        return "player"

    elif (player > 21 and computer > 21) or player == computer:
        return "Draw"
    else:
        return "computer"



def clear():
    os.system('clear')
