from card import Card
import random

class Deck():
    """Deck class, implements Deck operations including creation of pack of decks,
       shuffling decks and dealing a card from the deck."""

    def __init__(self, number_of_decks = 1):
        self.number_of_decks = number_of_decks
        self.deck = [] #start with an empty list of cards
        while (number_of_decks > 0):
            #shuffle suites in temp list before picking for deck
            temp_suites = list(Card.suites)
            random.shuffle(temp_suites)
            #shuffle ranks in temp list before picking for deck
            temp_ranks = list(Card.ranks)
            random.shuffle(temp_ranks)

            for suite in temp_suites:          
                for rank in temp_ranks:
                    self.deck.append(Card(suite, rank))
            number_of_decks = number_of_decks - 1


    
    def __str__(self):
        temp_deck_list = ''
        for card in self.deck:
            temp_deck_list += card.__str__() + '\n'
        
        return (f'There are {self.number_of_decks} decks. Cards are ordered as...: \n' + temp_deck_list)
    
    
    
    def shuffle(self, number_of_times_to_shuffle = 1):
        while(number_of_times_to_shuffle > 0):
            number_of_times_to_shuffle = number_of_times_to_shuffle - 1
            random.shuffle(self.deck)
    
    
    def deal(self):
        return self.deck.pop()