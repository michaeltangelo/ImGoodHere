import math
import random
import utils as u

class Card:
    """
    A card is represented by an array consisting of a number and a suit.
    Suits are ordered as:
    1) Spades
    2) Hearts
    3) Clubs
    4) Diamonds
    Therefore, the King of Hearts will be represented as a array of size 2:
    [13, 2]

    Note: Value is [1, 13], or one to thirteen inclusive
    Note: Suit is [0, 3], or one to three inclusive
    """

    def __init__(self, value, suit):
        # Member Variables
        self.data = [None] * 2
        self.data[0] = int(value)
        self.data[1] = int(suit)
    @staticmethod
    def from_int(value):
        # print("begin")
        # print(value)
        # print(value % 13)
        # print(value//13)
        # print("end")
        return Card((value % 13), (value//13))
    def __repr__(self):
        return (u.value_to_string(self.data[0])) + (u.suit_to_string(self.data[1]))
    def __lt__(self, other):
        if self.data[0] > other.data[0]:
            return True
        elif self.data[0] == other.data[0]:
            return self.data[1] < other.data[1]
        else:
            return False
    def value(self):
        return self.data[0]
    def suit(self):
        return self.data[1]
    # Returns the card as an int. For example, King of Hearts will be card # 39
    def as_int(self):
        return data[0] * (data[1]+1)

class Board:
    """
    The board class represents a board.
    """
    board = [None] * 5

    def __init__(self, c0 = None, c1 = None, c2 = None, c3 = None, c4 = None):
        if c0 != None:
            self.board[0] = c0
        if c1 != None:
            self.board[1] = c1
        if c2 != None:
            self.board[2] = c2
        if c3 != None:
            self.board[3] = c3
        if c4 != None:
            self.board[4] = c4
    def __repr__(self):
        s = "["
        for c in self.board:
            s += str(c)
            if c != self.board[4]:
                s += ","
        return s +"]"
    
    @staticmethod
    def from_ints(int_array):
        b = Board()
        for i in range(len(int_array)):
            c = Card.from_int(int_array[i])
        return b

class Deck:
    deck = list(range(1, 52))
    def draw(self, num=1):
        cards = []
        for i in range(num):
            r = random.randrange(len(self.deck))
            n = self.deck.pop(r)
            c = Card.from_int(n)
            cards.append(c)
        if num == 1:
            return cards[0]
        else:
            return cards

def rand_card():
    return Card(random.randint(1, 13), random.randint(0,3))

def rand_board():
    c0 = rand_card()
    c1 = rand_card()
    random_ints = [random.randint(0, 51) for i in range(5)]
    return Board.from_ints(random_ints)