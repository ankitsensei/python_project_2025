import random

cards = [1,2,3,4,5,6,7,8,9,10,11]

def botRandomCard():
    global cards
    
    botTotalCard = []
    botCardSum = 0
    
    while botCardSum < 16:
        # take more card
        randomCard = random.choice(cards)
        botTotalCard.append(randomCard)
        for i in botTotalCard:
            botCardSum += 1
    print(botTotalCard)
    print(botCardSum)
    
botRandomCard()

