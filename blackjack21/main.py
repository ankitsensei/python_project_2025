import art
import random
print(art.blackjack)

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
    for i in range(2):
        playerTotalCard.append(random.choice(cards))
    while askAgain:
        playerCardSum = 0
        for i in playerTotalCard:
            playerCardSum += i
        print(f"👉 You have cards => {playerTotalCard}")
        print(f"👉 Your sum of cards => {playerCardSum}")
        if playerCardSum > 21:
            break
        ask = input("Want to grab another card too? 🤔  [y/n]: ").lower()
        if ask == "y":
            playerTotalCard.append(random.choice(cards))
        if ask == "n":
            askAgain = False
    playerThings = [playerTotalCard, playerCardSum]
    return playerThings

def deal():
    global totalAmount
    
    
    while True:
        betAmount = int(input(f"Enter bet amount from  Rs.{totalAmount}: "))
        if betAmount > totalAmount:
            print("You don't have enough Rs. to play 🥹")
            break
        else:
            print(f"Looks like you have enough money to gamble 🤩")
            botRandomThings = botRandomCard()
            playerRandomThings = playerRandomCard()
            print(f"🔴 Bot has cards => {botRandomThings[0]}")
            print(f"🔴 Bot's sum of cards => {botRandomThings[1]}")
            print()
            if botRandomThings[1] > 21:
                print("Bot's card sum is more than 21. That's why you WON. 😁")
                break
            elif playerRandomThings[1] > 21:
                print("Your's card sum is more than 21. That's why you LOSE. 🥹")
                break
            elif botRandomThings[1] > playerRandomThings[1]:
                print("YOU LOST 🥹")
            elif botRandomThings[1] < playerRandomThings[1]:
                print("YOU WON 😁")
            if betAmount <= 0:
                print("Such a poor guy. You LOST buddy 😭")
                break
deal()



