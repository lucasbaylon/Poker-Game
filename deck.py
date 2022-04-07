from cards import Card
import random


class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(value, suit)) for suit in suits] for value in values]

    def shuffle(self):
        random.shuffle(self)
        print("Deck mélangé.")

    def deal(self, location, times=1):
        for i in range(times):
            location.cards.append(self.pop(0))

    def burn(self):
        self.pop(0)
