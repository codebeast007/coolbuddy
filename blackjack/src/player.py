from card import Card
from deck import Deck

class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.player_cards = [] #list of cards player has
        self.cards_sum = 0
        self.hitting = True

    def take_card(self, dealt_card):
        self.player_cards.append(dealt_card)
        self.cards_sum += dealt_card.get_card_value()          

    def update_decision(self, decision):
        self.hitting = (decision.lower() == 'h')
