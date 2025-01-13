import random

cards = [1,2,3,4,5,6,7,8,9,10,11]

def botRandomCard():
    global cards
    
    botTotalCard = []
    botCardSum = 0
    
    while botCardSum < 16:
        # take more card
        botTotalCard.append(random.choice(cards))
        botCardSum = 0
        for i in botTotalCard:
            botCardSum += i
    print(botTotalCard)
    print(botCardSum)
botRandomCard()

