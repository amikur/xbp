import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, count):
        count = min(count, self.count())
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-count:]
        self.cards = self.cards[:-count]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank in ["Jack", "Queen", "King"]:
                self.value += 10
            elif card.rank == "Ace":
                has_ace = True
                self.value += 11
            else:
                self.value += int(card.rank)
        if has_ace and self.value > 21:
            self.value -= 10

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Hand()
        self.dealer = Hand(dealer=True)

    def play(self):
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        print("Your hand is: ", self.player.cards)
        print("Your hand value: ", self.player.calculate_value())

        while True:
            choice = input("Do you want to hit or stand? Enter h or s: ")
            if choice.lower()==

