import random

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

def calculate_score(hand):
    total = 0
    aces = 0
    
    for card in hand:
        total += card_values[card]
        if card == "A":
            aces += 1
            
    while total > 21 and aces > 0:
        total -= 10  
        aces -= 1    
        
    return total
    
def blackjack():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]*4
    random.shuffle(deck)
    playerhand = [deck.pop(), deck.pop()]
    dealerhand = [deck.pop(), deck.pop()]
    playervalue = calculate_score(playerhand)
    dealervalue = calculate_score(dealerhand)
    print(f"Your hand: {playerhand}, Total value: {playervalue}")
    print(f"Dealer's shows: {dealerhand[0]}")
    if playervalue == 21:
        print("You just got a blackjack!")
    else:
        print("Choose your next option:")
    while playervalue < 21:
        option = input("Press H to hit or S to stand: ")
        if option == "H":
            newhand = deck.pop()
            playerhand.append(newhand)
            playervalue = calculate_score(playerhand)
            print(f"Your hand: {playerhand}, Total value: {playervalue}")
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
        dealervalue = calculate_score(dealerhand)
        print(f"Dealer hand: {dealerhand}, Total value: {dealervalue}")
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