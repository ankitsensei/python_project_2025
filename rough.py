import random

cards = [1,2,3,4,5,6,7,8,9,10,11]

def playerRandomCard():
    playerTotalCard = []
    playerCardSum = 0
    askAgain = True
    for i in range(2):
        playerTotalCard.append(random.choice(cards))
    while askAgain:
        for i in playerTotalCard:
            playerCardSum += i
        print(f"Your cards are: {playerTotalCard}")
        print(f"Your sum of Cards are: {playerCardSum}")
        ask = input("Want to grab another card too? 🤔  [y/n]: ").lower()
        if ask == "y":
            playerTotalCard.append(random.choice(cards))
        else:
            askAgain = False      
        if playerCardSum >=21:
            playerThings = [playerTotalCard, playerCardSum]
        else:
            playerThings = [playerTotalCard, [0]]
            askAgain = False
    return playerThings

print(playerRandomCard())