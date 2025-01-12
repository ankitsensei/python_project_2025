import art
import random
# print(art.blackjack)

cards = [1,2,3,4,5,6,7,8,9,10,11]
totalAmount = 2500



def botRandomCard():
    global cards
    
    randomCard = random.choice(cards)
    
    botTotalCard = []
    botSumCard = 0
    
    for i in botTotalCard:
        botSumCard +=i
        
    if botSumCard > 16:
        # take more card
        

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



