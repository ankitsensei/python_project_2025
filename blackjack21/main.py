import art
import random
import os
import platform
print(art.blackjack)

cards = [1,2,3,4,5,6,7,8,9,10,11]
totalAmount = 2500
score = 0


def clear_terminal():
    if platform.system() == "windows":
        os.system("cls")
    else:
        os.system("clear")
        
        
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
        clear_terminal()
        print(f"🟢 You have cards => {playerTotalCard}")
        print(f"🟢 Your sum of cards => {playerCardSum}")
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
    global score
    
    while True:
        if score < totalAmount:
            score += totalAmount
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
                totalAmount += betAmount
                print(f"Now, you have Rs.{totalAmount}")
            elif playerRandomThings[1] > 21:
                print("Your's card sum is more than 21. That's why you LOSE. 🥹")
                totalAmount -= betAmount
                print(f"Now, you have Rs.{totalAmount} left.")
            elif botRandomThings[1] > playerRandomThings[1]:
                print("YOU LOST 🥹")
                totalAmount -= betAmount
                print(f"Now, you have Rs.{totalAmount} left.")
            elif botRandomThings[1] < playerRandomThings[1]:
                print("YOU WON 😁")
                totalAmount += betAmount
                print(f"Now, you have Rs.{totalAmount}")
            if totalAmount <= 0:
                print("Such a poor guy. You LOST buddy 😭")
                print(f"Your score is: {score}")
                break
deal()



