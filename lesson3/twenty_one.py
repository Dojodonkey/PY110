'''
Rules of Twenty-One

Deck:
Start with a standard 52-card deck consisting of the 4 suits (Hearts, Diamonds, Clubs, and Spades),
and 13 values (2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace).

Goal:
The goal of Twenty-One is to try to get as close to 21 as possible without going over.
If you go over 21, it's a bust, and you lose.

Setup:
The game consists of a dealer and a player.
Both participants are initially dealt a hand of two cards.
The player can see their two cards,
but can only see one of the dealer's cards.

Card values:
All of the card values are pretty straightforward, except for the Ace.
The cards with numbers 2 through 10 are worth their face value.
The Jack, Queen, and King are each worth 10.
The Ace can be worth 1 or 11 depending on circumstances.
Its value is determined each time a new card is drawn from the deck.
For example, if the hand contains a 2, an Ace, and a 5, then the total value of the hand is 18.
In this case, the Ace is worth 11 because the sum of the hand (2 + 11 + 5) doesn't exceed 21.
Now, say another card is drawn, and it happens to be an Ace.
Your program must determine the value of both Aces.
If the sum of the hand (2 + 11 + 5 + 11) exceeds 21,
then one of the Aces must be worth 1, resulting in the hand's total value being 19.
What happens if another card is drawn and it also happens to be an Ace?
It can get tricky if there are multiple Aces in a hand, so your program must account for that.

Card  :	Value
2 - 10 : face value
Jack, Queen, King :	10
Ace : 1 or 11

Player turn:
The player always goes first,
and can decide to either hit or stay.
A hit means the player wants to be dealt another card.
Remember, if his total exceeds 21, he will bust and lose the game.
The decision to hit or stay depends on the player's cards and what the player thinks the dealer has.
For example, if the dealer is showing a "10" (the other card is hidden), and the player has a "2" and a "4",
then the obvious choice is for the player to hit.
The player can continue to hit as many times as they want.
The turn is over when the player either busts or stays.
If the player busts, the game is over, and the dealer won.

Dealer turn:
When the player stays, it's the dealer's turn.
The dealer must follow a strict rule for determining whether to hit or stay:
hit until the total is at least 17.
If the dealer busts, then the player wins.

Comparing cards:
When both the player and the dealer stay,
it's time to compare the total value of the cards and see who has the highest value.

- High Level Strategy:
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

A:
1. Create a deck of cards and shuffle them.
2. Assign a data structure for both 'player' and 'dealer'.
    - Deal two cards to both the player and dealer.
        - Output the cards of the player and one from the dealer.
3. The player must decide they want to 'hit' or 'stay'.
    - each time the player 'hits', display the player's hand and the one card of the dealer.
    - if the player 'hits' and the total is over 21, 'bust' and the player looses.
4. The dealer must hit until the total of their hand is over 17.
    - if the hand total is over 21, 'bust' and the dealer looses.
5. If both the player and the dealer 'stay' then the total of their hands must be compared.
    - whichever hand is closer to 21, wins.
'''
import os
import random

# messages
def prompt(message):
    print(f'=> {message}')

# calculate hands
def total(cards):
    # only ranks:
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == 'Ace':
            sum_val += 11
        elif value in ['Jack', 'Queen', 'King']:
            sum_val += 10
        else:
            sum_val += int(value)
    # adjust ace value:
    aces = values.count('Ace')
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

# bust
def busted(cards):
    return total(cards) > 21

# players turn
def players_turn():
    while True:
        answer = input('hit or stay?: ')
        if answer.strip() == 'stay' or busted(player):
            break
        else:
            deal_card(player)
            os.system('clear')
            show_hand()
            # check if hand is busted
            if busted(player):
                break

    if busted(player):
        os.system('clear')
        show_final_hands()
        prompt('Busted! You lose..')
        return False

    else:
        prompt('You chose to stay..')
        return True


# dealers turn
def dealers_turn():
    while total(dealer) < 17:
        deal_card(dealer)
    # hit on 17?
    if total(dealer) == 17:
        hit_after_17 = random.choice(('yes', 'no'))
        if hit_after_17 == 'yes':
            deal_card(dealer)
# check for busted hand
    if busted(dealer):
            os.system('clear')
            show_final_hands()
            prompt('Dealer is busted! Player wins!')
            return False
    return True

# deal 1 card
def deal_card(hand):
    # add a card to the hand and remove it from the deck
    hand.append(deck.pop(deck.index(random.choice(deck))))

# dealing initial hand
def deal_hand(hand):
    while len(hand) < 2:
        deal_card(hand)

# view hand throughout game
def show_hand():
    prompt(f'Player: {player}')
    prompt(f'Dealer: {dealer[0]}')

def show_final_hands():
    os.system('clear')
    prompt('__Final Hands__')
    prompt(f'Player: {player}')
    prompt(f'Dealer: {dealer}')

# compare hands
def compare_hands():
    dealer_points = 21 - total(dealer)
    player_points = 21 - total(player)
    show_final_hands()
    if player_points < dealer_points:
        prompt('Player wins!..')
        return 'player'
    elif player_points == dealer_points:
        prompt('It\'s a draw!..')
        return 'draw'
    else:
        prompt('The house wins!..')
        return 'dealer'

# Game Begins:
game_play = True
while game_play:

    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(suit, rank) for suit in suits for rank in ranks] # list containing 52 tuples of cards

    # Main Game Flow:
    player = []
    dealer = []
    # deal cards to player and dealer
    prompt('Initial hands are dealt...')
    deal_hand(player)
    deal_hand(dealer)
    show_hand()

    # player's turns
    player1 =  players_turn()
    dealer1 = dealers_turn()

    # determine winner if both stay or if busted
    if dealer1 == True and player1 == True:
        winner = compare_hands()
    elif busted(dealer):
        winner = 'player'
    elif busted(player):
        winner = 'dealer'


    # play again prompts using 'winner'
    player_won = ['Beginner\'s luck...', 'Just a fluke...', 'You got balls kid...']
    dealer_won = ['House always wins ;)...', 'Better luck next time pony boy...', 'Tough luck...']
    draw_won = ['Let\'s settle this..', 'Well, every blue moon...', 'Looks like this ain\'t over...']

    while True:

        if winner == 'player':
            play_again = input(f'=> {random.choice(player_won)}Play again?(y/n): ')
        elif winner == 'draw':
            play_again = input(f'=> {random.choice(draw_won)}Play again?(y/n): ')
        elif winner == 'dealer':
            play_again = input(f'=> {random.choice(dealer_won)}Play again?(y/n): ')
        #answer to play again
        n_answers = ['Chicken', 'Weak sauce', 'Alright, walk away sunshine boy']
        y_answers = ['Another round begins', 'Another round another dollar', 'Hold on to your hat, another round is beginning']

        if play_again.lower().strip() == 'n':
            prompt(f'{random.choice(n_answers)}...')
            game_play = False
            break
        elif play_again.lower().strip() == 'y':
            os.system('clear')
            prompt(f'{random.choice(y_answers)}...')
            break
        else:
            prompt(f'{random.choice(['Try again chico, I didn\'t get that', 'Take a deep breath and try that again'])}...')
