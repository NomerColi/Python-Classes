import random
from PIL import Image

class Card:
    suits = ['S', 'D', 'b', 'P']
    ranks = ['0', '1', '2']

    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def printCard(self):
        print(self)


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

    def shuffleCards(self):
        random.shuffle(self.cards)

    def printDeck(self):
        print(self.cards)

deck = Deck()
deck.shuffleCards()
deck.printDeck()

img = Image.open(r"card_images/" + "2_card.bmp")