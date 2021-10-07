import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    # constructor
    def __init__(self, dealer):   # self == this
        self._dealer = dealer
        self._make_deck()

    # private method
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # tuple
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):  # 'dunder str"  tostring()
        return f"CardDeck({self._dealer})"

    # properties ...
    #  getter properties
    #  setter properties