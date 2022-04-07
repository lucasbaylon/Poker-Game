class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value_name = ""
        suit_name = ""
        if self.value == 0:
            value_name = "Deux"
        elif self.value == 1:
            value_name = "Trois"
        elif self.value == 2:
            value_name = "Quatre"
        elif self.value == 3:
            value_name = "Cinq"
        elif self.value == 4:
            value_name = "Six"
        elif self.value == 5:
            value_name = "Sept"
        elif self.value == 6:
            value_name = "Huit"
        elif self.value == 7:
            value_name = "Neuf"
        elif self.value == 8:
            value_name = "Dix"
        elif self.value == 9:
            value_name = "Valet"
        elif self.value == 10:
            value_name = "Dame"
        elif self.value == 11:
            value_name = "Roi"
        elif self.value == 12:
            value_name = "As"
        if self.suit == 0:
            suit_name = "Carreau"
        elif self.suit == 1:
            suit_name = "Trèfle"
        elif self.suit == 2:
            suit_name = "Coeur"
        elif self.suit == 3:
            suit_name = "Pique"
        return value_name + " de " + suit_name
