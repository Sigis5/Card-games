import random

def blackjack():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    random.shuffle(deck)
    playerhand = [deck.pop(), deck.pop()]
    dealerhand = [deck.pop(), deck.pop()]
    print(f"Your hand: {playerhand}, Total value: {sum(playerhand)}")
    print(f"Dealer's shows: {dealerhand[0]}")
    playervalue = sum(playerhand)
    dealervalue = sum(dealerhand)
    if playervalue == 21:
        print("You just got a blackjack!")
    else:
        print("Choose your next option:")
    while playervalue < 21:
        option = input("Press H to hit or S to stand: ")
        if option == "H":
            newhand = deck.pop()
            playerhand.append(newhand)
            print(f"Your hand: {playerhand}, Total value: {sum(playerhand)}")
            playervalue = sum(playerhand)
            while playervalue > 21 and 11 in playerhand: 
                playerhand.remove(11)
                playerhand.append(1)
                playervalue = sum(playerhand)
            if playervalue > 21:
                print("Bust! Dealer wins!")
                return
            else:
                continue
        elif option == "S":
            print("You stand.")
            print(f"Dealer hand: {dealerhand} ")
            break
        else:
            print("Wrong input!")
    while dealervalue < 17:
        newdealhand = deck.pop()
        dealerhand.append(newdealhand)
        dealervalue = sum(dealerhand)
        while dealervalue > 21 and 11 in dealerhand:
            dealerhand.remove(11)
            dealerhand.append(1)
            dealervalue = sum(dealerhand)
        print(f"Dealer hand: {dealerhand}, Total value: {sum(dealerhand)}")
        if dealervalue > 21:
            print("Dealer busts. You win!")
            return
        elif dealervalue == 21:
            print("Dealer has got a blackjack! You lose!")
        else:
            continue
    if playervalue > dealervalue:
        print("You win!")
    elif dealervalue > playervalue:
        print("Dealer wins!")
    else:
        print("It's a tie!")
def game():
    while True:
        play = input("Press y to begin playing or anything else to exit: ").lower()
        if play == "y":
            blackjack()
        else:
            exit()
game()