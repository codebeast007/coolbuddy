import random


class Card():
    """Card class. Implements card features (suite, rank, value)"""
    
    #class variables
    suites = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
    ranks = ('A', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',  'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace')
    values = {'A':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,  'Eight':8, 'Nine':9, 'Ten':10, 'King':10, 'Queen':10, 'Jack':10, 'Ace':11}

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        return
    
    def __str__(self):
        return self.suite + ' ' + self.rank + ' ' + f"({Card.values[self.rank]})"
    
    def get_card_value(self):
        return Card.values[self.rank]
       

