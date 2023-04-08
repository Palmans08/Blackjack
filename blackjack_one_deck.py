from random import shuffle
from os import system, name

list_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
list_suits = ['clubs', 'diamonds', 'hearts', 'spades']
ongoing_game = True
dictionary_player = {'hand':[], 'scores':0, 'turn':True}
dictionary_dealer = {'hand':[], 'scores':0, 'turn':False}
cards = [(rank, suit) for rank in list_ranks for suit in list_suits]

# def clear_screen():
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#     else:
#         system('clear')

def calculate(x):
    total = 0
    count_ace = 0

    for rank in x['hand']:
        if rank[0] == 'J' or rank[0] == 'Q' or rank[0] == 'K':
            total += 10
        elif rank[0] == 'A':
            count_ace += 1
            total += 11
        else:
            total += rank[0]

    while count_ace != 0 and total > 21:
        total -= 10
        count_ace -= 1

    return total

def show_cards():
    # clear_screen()
    print('Dealers hand:')
    if dictionary_player['turn']:
        value_card_dealer, suit_dealer = dictionary_dealer['hand'][0]
        print(str(value_card_dealer) + ' ' + suit_dealer)
    else:
        for card in dictionary_dealer['hand']:
            value_card_dealer, suit_player = card
            print(str(value_card_dealer) + ' ' + suit_player)
        print(f'\nDealer has: {calculate(dictionary_dealer)}')

    print('\nPlayer hand:')
    for card in dictionary_player['hand']:
        value_card_player, suit_player = card
        print(str(value_card_player) + ' ' + suit_player)
    print(f'\nYou have: {calculate(dictionary_player)}')

def announce_outcome_turn():
    if calculate(dictionary_player) > 21:
        dictionary_dealer['scores'] += 1
        print('\nYou busted. Dealer won this round.')
    elif calculate(dictionary_dealer) > 21:
        dictionary_player['scores'] += 1
        print('\nDealer busted. You won this round.')
    elif calculate(dictionary_player) == calculate(dictionary_dealer):
        print('\nPush. Both hands are a draw.')
    elif calculate(dictionary_player) > calculate(dictionary_dealer):
        dictionary_player['scores'] += 1
        print('\nYou won this round.') 
    elif calculate(dictionary_player) < calculate(dictionary_dealer):
        dictionary_dealer['scores'] += 1
        print('\nDealer won this round.')

def end_game():
    # clear_screen()
    print(f'End of game\nThe dealer won: {str(dictionary_dealer["scores"])} times.\nYou won: {str(dictionary_player["scores"])} times.')
    exit()

while ongoing_game:
    for x in range(3):
        shuffle(cards)

    for x in range(2):
        dictionary_player['hand'] += cards[0],
        cards.pop(0)
        dictionary_dealer['hand'] += cards[0],
        cards.pop(0)

    while dictionary_player['turn']:
        show_cards()
        choise = ''
        if calculate(dictionary_player) < 21:
            while choise != ('H' or 'S') and dictionary_player['turn']:
                choise = input('\n(H)it (S)tand: ').upper()
                if choise == 'H':
                    dictionary_player['hand'] += cards[0],
                    cards.pop(0)
                elif choise == 'S':
                    dictionary_player['turn'] = False
                    dictionary_dealer['turn'] = True
                else:
                    print('Invalid choise, please type "H" for (H)it or "S" if you would like to (S)tand')
        elif calculate(dictionary_player) == 21:
            dictionary_player['turn'] = False
            dictionary_dealer['turn'] = False
        else:
            dictionary_player['turn'] = False
            dictionary_dealer['turn'] = False        

    while dictionary_dealer['turn']:
        if calculate(dictionary_dealer) < 17:
            dictionary_dealer['hand'] += cards[0],
            cards.pop(0)
        else:
            dictionary_dealer['turn'] = False

    show_cards()
    announce_outcome_turn()
    
    end_game_or_new_round = ''
    while end_game_or_new_round != ('Y' or 'N'):
        end_game_or_new_round = input('\nWould you like to play again? (Y)es or (N)o: ').upper()
        if end_game_or_new_round == 'Y':
            dictionary_player['turn'] = True
            dictionary_dealer['turn'] = False
        elif end_game_or_new_round == 'N':
            ongoing_game = False
            end_game()

    #add cards back to deck
    for i in dictionary_player['hand']:
        cards.append(i,)
    dictionary_player['hand'].clear()
    for i in dictionary_dealer['hand']:
        cards.append(i,)
    dictionary_dealer['hand'].clear()