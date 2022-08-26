import random
import os
from art import logo, vs
from gameData import data


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def getRandomPerson():
    return random.choice(data)


def checkAnswer(ans, entityA, entityB):
    answer = ans.lower()
    scoreA = entityA['follower_count']
    scoreB = entityB['follower_count']

    if answer == 'a':
        return True if scoreA > scoreB else False
    elif answer == 'b':
        return True if scoreB > scoreA else False
    else:
        return False


def game(sc):
    entityA = getRandomPerson()
    entityB = getRandomPerson()

    while entityA["name"] == entityB["name"]:
        personB = getRandomPerson()

    print(f'''Compare A: {entityA["name"]}, a {entityA["description"]}, from {entityA["country"]}.''')
    print(vs)
    print(f'''Against B: {entityB["name"]}, a {entityB["description"]}, from {entityB["country"]}.''')

    answer = input("Who has more followers? Type 'A' or 'B': ")

    result = checkAnswer(answer, entityA, entityB)
    if result:
        sc+=1
        return True
    else:
        print(f"Sorry, that's wrong. Final score: {sc}")
        return False


check = 'y'

while check == 'y':
    score = 0
    clear()
    print(logo)

    round = game(score)
    while round:
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
        round = game(score)

    check = input("Do you want to play the game again? Type 'y' or 'n': ")
