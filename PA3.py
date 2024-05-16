#Pritam Ban
#COSI 10a Spring 2024
#Programming Assignment 3
#Description: Blackjack Game, does not allow for doubling down or splitting cards, can only play one hand at a time
#Known bugs: Game breaks if player inputs a non integer value for their bet

import random

def betInputValidation(playerBet, playerMoney):
    """
    Validate the input for the bet fucntion, make sure user
    doesn't bet more than they have
    """

    while int(playerBet) <= 0:
        print()
        print("Error -- You can't less than $1")
        print()

        playerBet = input("Enter your bet: ")
    while int(playerBet) > int(playerMoney):
        print()
        print("Error -- You don't have enough money to bet that")
        print()

        playerBet = input("Enter your bet: ")
    return int(playerBet)

def getCard():
    """
    Get a random value for the card between 2 and 14 
    (14 being the value for Ace, 1 is not present in the range)
    """

    cardVal = random.randint(2,14)
    return cardVal

def playerAceLogic():
    """
    Get the user to choose if they want their Ace to be
    valued at 11 or valued at 1
    """

    aceOrOne = input("Would you like the value to be 11 or 1?: ")
    if aceOrOne == "11":
        return 11
    elif aceOrOne == "1":
        return 1

def dealerAceLogic(dealerCardValue):
    """
    Get the dealer to choose between their Ace being worth 
    11 or 1 points, dealer only chooses 11 points if their card value is
    10 or below
    """

    if dealerCardValue <= 10:
        return 11
    else:
        return 1
    
def hitOrStand(playerCardValue):
    """
    Validates input for if the player wants to hit or stand
    returns their choice
    """


    while playerCardValue <= 21:
        hitOrStand = input("HIT or STAND?: ")
        while hitOrStand != "HIT" or hitOrStand != "STAND":
            if hitOrStand == "HIT":
                return "HIT"
            if hitOrStand == "STAND":
                return "STAND"
            
            print()
            print("Error -- please type in \"HIT\" or \"STAND\"")
            print()
            hitOrStand = input("HIT or STAND?: ")

def playFunction():
    """
    Gets the player choice if they want to play again
    validates input to make sure user inputs Y or N
    """

    print()
    playagainChoice = input("PLAY AGAIN? Y / N: ")
    while playagainChoice != "Y" and playagainChoice != "N":
        print()
        print("Error -- Please enter Y or N")
        print()

        playagainChoice = input("PLAY AGAIN? Y / N: ")
    if playagainChoice == "Y":
        return True
    elif playagainChoice == "N":
        return False

def getFaceCard(x):
    """
    Returns a face value card for the corresponding value
    """

    if x == 11:
        return "J "
    elif x == 12:
        return "Q "
    elif x == 13:
        return "K "

def main():
    playerMoney = 100
    card = 0
    playerCardValue = 0
    dealerCardValue = 0
    playerCards = ""
    dealerCards = ""

    playagainChoice = True

    while playagainChoice == True:

        if playerMoney <= 0:
            print("You're broke, close and try again")
            break

        card = 0
        playerCardValue = 0
        dealerCardValue = 0
        playerCards = ""
        dealerCards = ""

        print ("Welcome to BlackJack")
        print ("You have $", playerMoney)

        # get bet
        playerBet = input("Enter your bet: ")
        playerBet = betInputValidation(playerBet, playerMoney)
        playerMoney = playerMoney - playerBet
        print()


        print("Your Cards: ", end="")


        # Get the first card for the player hand
        card += getCard()
        if card > 10 and card < 14:
            playerCards += getFaceCard(card)
            card = 10
            playerCardValue += card
        elif card == 14:
            playerCards += "A "
            playerCardValue += playerAceLogic()
        else:
            playerCardValue += card
            playerCards += str(card) + " "


        # Get the second card for the player hand
        card = 0
        card += getCard()
        if card > 10 and card < 14:
            playerCards += getFaceCard(card)
            card = 10
            playerCardValue += card
        elif card == 14:
            playerCards += "A "
            playerCardValue += playerAceLogic()
        else:
            playerCardValue += card
            playerCards += str(card) + " "

        print(playerCards, end=" ")
        print()
        print("Dealer Card: ", end="")


        # Get the first card for the dealer hand
        card = 0
        card += getCard()
        if card > 10 and card < 14:
            dealerCards += getFaceCard(card)
            
            card = 10
            dealerCardValue += card
        elif card == 14:
            dealerCards += "A "
            dealerCardValue+= dealerAceLogic(dealerCardValue)
        else:
            dealerCardValue += card
            dealerCards += str(card) + " "

        print(dealerCards)
        if playerCardValue == 21:
            choice =""
            playerMoney += int(playerBet) * 2
            print("WIN, You have $", playerMoney)
            playagainChoice = playFunction()
            break

        print("Your Card Value:", playerCardValue)
        print()
        choice = hitOrStand(playerCardValue)

        while choice == "HIT":
            print()
            print("Your Cards: ", end="")
            

            #Get a new card for the player hand
            card = 0
            card += getCard()
            if card > 10 and card < 14:
                playerCards+= getFaceCard(card)
                
                card = 10
                playerCardValue += card
            elif card == 14:
                playerCards += "A "
                playerCardValue += playerAceLogic()
            else:
                playerCardValue += card 
                playerCards += str(card)+ " "

            print(playerCards, end=" ")
            print("Dealer Cards: ", dealerCards)
            print("New Card Value:", playerCardValue)

            if playerCardValue > 21:
                choice = ""
                print("BUST, You have $", playerMoney)
                playagainChoice = playFunction()
            elif playerCardValue == 21:
                choice =""
                playerMoney += int(playerBet) * 2
                print("WIN, You have $", playerMoney)
                playagainChoice = playFunction()
            else:
                choice = hitOrStand(playerCardValue)
                
        while choice == "STAND":
            print()
            print("Your Cards: ", playerCards, "Your Card Value: ", playerCardValue)
            
            #Get next dealer card
            card = 0
            card += getCard() 
            if card > 10 and card < 14:
                dealerCards+= getFaceCard(card)
                
                card = 10
                dealerCardValue += card
            elif card == 14:
                dealerCards + "A "
                dealerCardValue += dealerAceLogic(dealerCardValue)
            else:
                dealerCardValue += card
                dealerCards += str(card) + " "
            
            print("Dealer Cards: ", dealerCards, "Dealer Card Value: ", dealerCardValue)

            while dealerCardValue < 17:
                #Keep picking dealer cards until card value is greater than 16
                card = 0
                card += getCard()
                if card > 10 and card < 14:
                    dealerCards+= getFaceCard(card)
                    card = 10
                    dealerCardValue += card
                elif card == 14:
                    playerCards += "A "
                    dealerCardValue += dealerAceLogic(dealerCardValue)
                else:
                    dealerCardValue += card
                    dealerCards += str(card) + " "

                print("Dealer Cards: ", dealerCards, "Dealer Card Value: ", dealerCardValue)

            if dealerCardValue > playerCardValue and dealerCardValue < 22:
                choice =""
                print("Dealer Win :( You have $", playerMoney)
                playagainChoice = playFunction()
            elif dealerCardValue < playerCardValue or dealerCardValue > 21 :
                choice = ""
                playerMoney += int(playerBet) * 2
                print("WIN! You have $", playerMoney)
                playagainChoice = playFunction()


main()
