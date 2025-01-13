import art
import random
# print(art.blackjack)

cards = [1,2,3,4,5,6,7,8,9,10,11]
totalAmount = 2500



def botRandomCard():
    global cards
    
    botTotalCard = []
    botCardSum = 0
    
    while botCardSum < 16:
        # Bot taking more card
        botTotalCard.append(random.choice(cards))
        botCardSum = 0
        for i in botTotalCard:
            botCardSum += i
        botThings = [botTotalCard, botCardSum]
        return botThings

def playerRandomCard():
    playerTotalCard = []
    playerCardSum = 0
    askAgain = True
    while askAgain:
        for i in range(2):
            playerTotalCard.append(random.choice(cards))
        for i in playerTotalCard:
            playerCardSum += i
        print(f"Your cards are: {playerTotalCard}")
        print(f"Your sum of Cards are: {playerCardSum}")
        ask = input("Want to grab another card too? 🤔  [y/n]: ").lower()
        if ask != "y":
            askAgain = False
    if playerCardSum >=21:
        playerThings = [playerTotalCard, playerCardSum]
    else:
        playerThings = [0]
    return playerThings

def deal():
    global totalAmount
    betAmount = int(input(f"Enter bet amount from  Rs.{totalAmount}: "))
    if betAmount <= totalAmount:
        while True:
            hit = input("Want more cards [y/n]: ").lower()
            if hit == 'y':
                # Grab another card
                print("Grabbing")
            else: # If clicked stand
                print()
                break
            
    else:
        print("You don't have enough Rs. to play 🥹")

deal()



