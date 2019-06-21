import time
import colorama
from colorama import Fore, Back, Style
from card import Card
from deck import Deck
from dealer import Dealer 
from player import Player


class Blackjack():
    """Implements blackjack game specification"""

    #Methods accessed from within this class (Private Methods)

    def __init__(self, player_name, dealer_name):
        #Create dealer and player        
        self.player = Player(player_name)
        self.dealer = Dealer(dealer_name)


    def PRINT(self, message, sleep_seconds = 0):
        """Custom print function. Prints a given formatted string and sleeps for given seconds"""

        print(message + '\n')
        if(sleep_seconds > 0):
            time.sleep(sleep_seconds)


    def declare_result(self, winner, loser, result):
        """Declares result with winner/loser"""

        if(result == 'BLACKJACK'):
            self.PRINT(Fore.LIGHTGREEN_EX + f"{winner} hits blackjack and WINS!!!", 3)
        elif(result == 'BUSTED'):
            self.PRINT(Fore.LIGHTRED_EX + f"{loser} busts and LOSES... " + Fore.LIGHTGREEN_EX + f"and {winner} WINS !!!!", 3)



    def deal_card_to_player(self, dealer, player):
        """Deals a card to player. If dealt card is ACE, asks user to select between 1 and 11."""

        self.PRINT(Fore.LIGHTYELLOW_EX + f"\nDealing card to {player.name}...", 2)
        card = dealer.deal_a_card()
        
        #handle Ace condition for player. Ask his input
        if(card.rank.upper() == 'A' or card.rank.upper() == 'ACE'):
            user_ace_value = int(input(f"You have an Ace. How do you want to take it (1 or 11)?: "))
            print(Fore.LIGHTYELLOW_EX + f"{player.name} decided take Ace as {user_ace_value}")
            if(user_ace_value == 1):
                card.rank = 'A'
            elif(user_ace_value == 11):
                card.rank = 'Ace'
        
        player.take_card(card)
        self.PRINT(Fore.YELLOW + f"Card dealt is '{card}'. " + Fore.LIGHTYELLOW_EX + f"{player.name}\'s current score is: {player.cards_sum}", 2)




    def deal_card_to_dealer(self, dealer, show_current_score):
        """Deals a card to dealer. If dealt card is an ACE, automatically determines 1 or 11 and takes 
        most appropriate value for the current game."""

        if(show_current_score == True):
            self.PRINT(Fore.LIGHTCYAN_EX + f"\nDealing card to {dealer.name}...", 2)
        else:
            self.PRINT(Fore.LIGHTCYAN_EX + f"\nDealing card to {dealer.name} face down (no display of score)...", 2)
        card = dealer.deal_a_card()
        
        #at dealer end, handle Ace card smartly.
        if(card.rank.upper() == 'A' or card.rank.upper() == 'ACE'):
            if(dealer.cards_sum == 0 or (dealer.cards_sum >= 6 and dealer.cards_sum < 11)): #check for less than 11. If first card is 11 then dont take second also 11.
                card.rank = 'Ace'
            else:
                card.rank = 'A'

        dealer.take_card(card)
        if(show_current_score == True):#print only first card. second is considered face down
            self.PRINT(Fore.CYAN + f"Card dealt is '{card}'. " + Fore.LIGHTCYAN_EX + f"{dealer.name}\'s current score is: {dealer.cards_sum}", 2) 
        

    def did_i_bust(self, checkme):
        return (checkme.cards_sum > 21)

    def did_i_hit_blackjack(self, checkme):
        return (checkme.cards_sum == 21)



#Methods accessed by outsiders (Public Methods)

    def deal_first_two_cards(self):
        """Handles dealing of first two cards to player and dealer. Dealer's second card is dealt face down."""

        is_game_over_in_first_two_cards = False
        for idx in [1, 2]:
            #deal card to player
            self.deal_card_to_player(self.dealer, self.player)

            if(self.did_i_hit_blackjack(self.player)):
                self.declare_result(self.player.name, self.dealer.name, 'BLACKJACK')
                is_game_over_in_first_two_cards = True
                break

            #deal card to dealer
            self.deal_card_to_dealer(self.dealer, (idx == 1))
        return is_game_over_in_first_two_cards




    def player_plays_the_game(self):
        """Player's game until player decides to STAND or wins blackjack or busts"""

        is_players_game_over = False
        self.PRINT(Fore.LIGHTYELLOW_EX + f"{self.player.name}\'s current score is {self.player.cards_sum}")
        player_decision = input("Hit or Stand?(h-to continue / s-to stop)?: ")
        self.player.update_decision(player_decision)

        #deal cards to player
        while(self.player.hitting):
            
            self.deal_card_to_player(self.dealer, self.player)
            
            if(self.did_i_hit_blackjack(self.player)):
                self.declare_result(winner=self.player.name, loser=self.dealer.name, result='BLACKJACK')
                is_players_game_over = True
                break

            elif(self.did_i_bust(self.player)):
                self.declare_result(loser=self.player.name, winner=self.dealer.name, result='BUSTED')
                is_players_game_over = True
                break

            self.PRINT(Fore.LIGHTYELLOW_EX + f"{self.player.name}\'s current score is {self.player.cards_sum}")
            player_decision = input("Hit or Stand?(h-to continue / s-to stop)?: ")
            self.player.update_decision(player_decision)
            #end of while
        
        if(self.player.hitting == False):
            self.PRINT(Fore.LIGHTYELLOW_EX + f"\n{self.player.name} decided to STAND at {self.player.cards_sum}", 2)
        
        return is_players_game_over



    def dealer_plays_the_game(self):
        """Dealer's game until dealer decides to STAND or wins blackjack or busts"""

        is_dealers_game_over = False
        #deal cards to house...
        self.PRINT(Fore.LIGHTCYAN_EX + f"Flipping the card to face up of {self.dealer.name}...", 2)
        flipped_card = self.dealer.peek()
        self.PRINT(Fore.LIGHTCYAN_EX + f"Flippeed card was '{flipped_card}'. {self.dealer.name}\'s current score is: {self.dealer.cards_sum}", 2) 

        while(self.dealer.iam_in_game_range() == False):

            if(self.did_i_hit_blackjack(self.dealer)):
                self.declare_result(winner=self.dealer.name, loser=self.player.name, result='BLACKJACK')
                is_dealers_game_over = True
                break
            
            elif(self.did_i_bust(self.dealer)):
                self.declare_result(loser=self.dealer.name, winner=self.player.name, result='BUSTED')
                is_dealers_game_over = True
                break

            if(self.dealer.iam_in_game_range()):
                break

            self.deal_card_to_dealer(self.dealer, True)
            #end of while        
        return is_dealers_game_over



    def determine_the_winner(self):
        """Determines the winner by comparing player's and dealer's scores."""

        result = ''
        if(self.player.cards_sum == self.dealer.cards_sum):
            result = Fore.LIGHTBLUE_EX + f"Damn, Its a DRAWWWWWWW......."
        elif(self.player.cards_sum > self.dealer.cards_sum):
            result = Fore.LIGHTGREEN_EX + f"Hurrrrayyyyy [{self.player.name}] WINS !!!!!!!!!"
        else:
            result = Fore.LIGHTGREEN_EX + f"...And the Mighty <{self.dealer.name}> WINS !!!!!!!!"
        return result


    def shuffle_deck(self):
        """Shuffles the deck"""
        self.PRINT(Fore.LIGHTWHITE_EX + Style.BRIGHT + f"\n.....Shuffling deck.....", 3)
        self.dealer.shuffle_deck()

    def display_both_players_cards(self):        
        print(Fore.LIGHTYELLOW_EX + f"Players cards: ", *self.player.player_cards, sep=', ')
        print(Fore.LIGHTCYAN_EX + f"Dealers cards: ", *self.dealer.dealer_cards, sep=', ')