suits = ['spades', 'clubs', 'hearts', 'diamonds']
suit = suits[2]
rank = 'K'
value = 10
print(f"Your card is: {rank} of {suit}")
suits.append("snakes")
for suit in suits:
    print(suit)
#
import random
cards = []
suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
def shuffle():
    random.shuffle(cards)
def deal():
    card = cards.pop()
    return card
shuffle()
card = deal()
print(card)
#
def deal(number):
    cards_dealt = []
    for x in range(number):
        cards_dealt.append(cards.pop())
    return cards_dealt
shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]
if rank == 'A':
    value = 11
elif rank == 'J' or rank == 'Q' or rank == 'K':
    value = 10
else: value = rank
rank_dict = {'rank': rank, 'value': value}
print(rank_dict['rank'], rank_dict['value'])
#
ranks = [
    {'rank': 'A', 'value': 11}, 
    {'rank': '2', 'value': 2},
    {'rank': '3', 'value': 3},
    {'rank': '4', 'value': 4},
    {'rank': '5', 'value': 5},
    {'rank': '6', 'value': 6},
    {'rank': '7', 'value': 7}, 
    {'rank': '8', 'value': 8},
    {'rank': '9', 'value': 9},
    {'rank': '10', 'value': 10},
    {'rank': 'J', 'value': 10},
    {'rank': 'Q', 'value': 10},
    {'rank': 'K', 'value': 10}
    ]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
def shuffle():
    random.shuffle(cards)
def deal(number):
    cards_dealt = []
    for x in range(number):
        cards_dealt.append(cards.pop())
    return cards_dealt
shuffle()
card = deal(1)[0]
print(card[1]['value'])
#
class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
    def __str__(self) -> str:
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11}, 
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7}, 
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10}
            ]
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt

deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print(deck2.cards)
card1 = Card("hearts", {'rank': 'J', 'value': 10})
print(card1)
#
class Hand:
    def __init__(self, dealer = False) -> None:
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards .extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += int(card.rank['value'])
            if card.rank['rank'] == 'A':
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_backjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_backjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.get_value())
        print()

deck = Deck()
deck.shuffle()
hand = Hand()
hand.add_card(deck.deal(2))
hand.display()
#