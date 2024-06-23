import sys, random

HEARTS = chr(9829)
CLUBS = chr(9827)
SPADES = chr(9824)
DIAMONDS = chr(9830)
BACKSIDE = 'backside'

print("Welcome to blackjack")
money = 5000


def getBet(maxBet):
    while True:
        print("How much do you want to bet? (1-", maxBet, " or QUIT)")
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit))
        random.shuffle(deck)
        return deck
    
def displayCards(cards):
    rows = ['', '', '', '', '']
    for card in cards:
        rows[0] +=' ___ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)
def getHandValue(cards):
    value = 0
    number_aces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_aces += 1
        elif rank in ('K', 'J', 'Q'):
            value += 10
        else:
            value += int(rank)
    value += number_aces
    for i in range(number_aces):
        if value + 10 <= 21:
            value += 10
    return value

def displayHands(player_hand, dealer_hand, show_dealer):
    print()
    if show_dealer:
        print('DEALER: ', getHandValue(dealer_hand))
        displayCards(dealer_hand)
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealer_hand[1:])
    print("PLAYER: ", getHandValue(player_hand))
    displayCards(player_hand)

def getMove(player_hand, money):
    """Ask the player for their move, return H, S or D"""
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player_hand) == 2 and money>0:
            moves.append('(D)ouble down')
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


while True:
    #CHeck if player is out of money
    if money <= 0:
        print("It is good that you weren't playing with the real money")
        print("Thanks for playing")
        sys.exit()
    #Ask player to enter their bet
    print("Money: ", money)
    #Get bet
    bet = getBet(money)
    #Get cards
    deck = getDeck()
    #GIve the dealre and player two cards from the deck
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    #Handle player actions
    print("Bet: ", bet)
    while True:
        displayHands(player_hand, dealer_hand, False)
        print()
        if getHandValue(player_hand) >21:
            break
        move = getMove(player_hand, money - bet)
        if move == 'D':
            additional_bet = getBet(min(bet, (money - bet)))
            bet += additional_bet
            print("Bet increased to {}. Current bet is {}".format(bet, bet))
        if move in ("H", "D"):
            new_card = deck.pop()
            rank, suit = new_card
            print("You drew a {} of {}".format(rank, suit))
            player_hand.append(new_card)
            if getHandValue(player_hand) > 21:
                continue
        if move == "S":
            break
        #Handle dealer actions
        if getHandValue(player_hand) <= 21:
            while getHandValue(dealer_hand) < 17:
                # The dealer hits
                print("The dealer hits..")
                dealer_hand.append(deck.pop())
                displayHands(player_hand, dealer_hand, False)
                if getHandValue(dealer_hand) > 21:
                    # The dealer has busted
                    break
                input("Press enter to continie..")
                print('\n\n')
    
        displayHands(player_hand, dealer_hand, True)
        player_value = getHandValue(player_hand)
        dealer_value = getHandValue(dealer_hand)
        # Handle whether the player won, lost or draw
        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You win ${bet}!")
            money += bet
        elif player_value == dealer_value:
            print("It is a draw and the bet is returned to you!")
        input("Press enter to continue..")
        print('\n\n')

    print("Thanks for playing!")
    print(f"You left with ${money}")


    

