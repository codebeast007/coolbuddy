from card import Card
from deck import Deck


class Dealer():
    NUMBER_OF_DECKS = 6
    NUMBER_OF_TIMES_TO_SHUFFLE = 3

    def __init__(self, dealer_name):
        self.name = dealer_name
        self.cards_sum = 0
        self.dealer_cards = [] #list of cards dealer got while playing
        self.mydeck =  Deck(self.NUMBER_OF_DECKS)
        self.mydeck.shuffle(self.NUMBER_OF_TIMES_TO_SHUFFLE)

    def deal_a_card(self):
        return self.mydeck.deal()

    def take_card(self, dealt_card):
        self.dealer_cards.append(dealt_card)
        self.cards_sum += dealt_card.get_card_value()

    def iam_in_game_range(self):
        return (self.cards_sum >=17 and self.cards_sum < 21)
   
    def shuffle_deck(self):
        self.mydeck.shuffle(self.NUMBER_OF_TIMES_TO_SHUFFLE)
    
    def peek(self):
        return self.dealer_cards[-1]