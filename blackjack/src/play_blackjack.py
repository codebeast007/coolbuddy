from blackjack import Blackjack
import time
import colorama
from colorama import Fore, Back, Style
from card import Card
from deck import Deck
from dealer import Dealer 
from player import Player


if __name__ == '__main__':

    colorama.init(autoreset=True, strip=True)

    print(Fore.LIGHTWHITE_EX + '\n----------------------------------- How is this played -----------------------------------\n')
    print(Fore.LIGHTWHITE_EX + "Game is between player and the dealer. Goal is to hit 21 or get closer to it when the game ends.\n")
    print(Fore.LIGHTWHITE_EX + "Game ends when dealer gets a score of 17 or higher. First player and dealer both are dealt 2 cards each.\n")
    print(Fore.LIGHTWHITE_EX + "Then player is dealt cards until player decides to stop (calls 'stand') upon getting close to 21.\n")
    print(Fore.LIGHTWHITE_EX + "Then dealer is dealt cards until dealer gets 17 or higher.\n")
    print(Fore.LIGHTWHITE_EX + "        When do I win: \n")
    print(Fore.LIGHTWHITE_EX + "            >> Getting Ace with K or Q or J hits blackjack and wins.\n")
    print(Fore.LIGHTWHITE_EX + "            >> Upon dealer hitting 17+, whoever has higher score wins.\n\n")
    print(Fore.LIGHTWHITE_EX + "            >> Anyone crossing 21 loses and other wins.\n")

    input_player_name = input(f"Enter player's name: ") 
    input_dealer_name = input(f"Enter dealer's name: ") 

    while(input(f"Do you want to play?y/n: ").lower() == 'y'):
        is_game_over = False

        blackjack_game = Blackjack(input_player_name, input_dealer_name)

        blackjack_game.shuffle_deck()

        #Deal first two cards to player and dealer
        is_game_over = blackjack_game.deal_first_two_cards()


        if(is_game_over == False):
            is_game_over = blackjack_game.player_plays_the_game()

        if(is_game_over == False):
            is_game_over = blackjack_game.dealer_plays_the_game()

        if(is_game_over == False):
            blackjack_game.PRINT(Fore.GREEN + f"Determining the winner....", 2)
            result = blackjack_game.determine_the_winner()
            blackjack_game.PRINT(result, 2)

        blackjack_game.display_both_players_cards()
        
        print(Fore.LIGHTMAGENTA_EX + '\nYou have reached the end of game....\n\n')

