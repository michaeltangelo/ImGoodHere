from collections import namedtuple
import random

def best_hand(c0, c1, board_cards):
    # prep cards array sort ascending
    cards = [c0] + [c1] + board_cards
    sorted = cards.sort()

    Counter = namedtuple('Counter', 'count value')
    c1 = Counter(0, 0) # tracks the first pair/trip/quad
    c2 = Counter(0, 0) # tracks the second pair/trip

    StraightCounter = namedtuple('StraightCounter', 'count highest_value straight')
    c3 = StraightCounter(0, 0, False) # tracks straights

    print("begin algo")
    for i in range(len(cards) - 1):
        curr = cards[i].value()
        next = cards[i+1].value()
        diff = abs(next-curr)
        if diff == 0:
            if c1.value == curr:
                c1 = c1._replace(count = (c1.count + 1))
            if c1.count == 0 and c1.value != curr:
                c1 = c1._replace(count = (c1.count + 1))
                c1 = c1._replace(value = curr)
            elif c1.count != 0 and c1.value != curr:
                c2 = c2._replace(count = c2.count + 1)
                c2 = c2._replace(value = curr)
            # if not c3.straight:
            #     c3 = c3._replace(count = 0)
            #     c3 = c3._replace(highest_value = 0)
        elif diff == 1:
            if c3.count == 0: # this could be the highest value of the straight, store it
                c3 = c3._replace(highest_value = curr)
            c3 = c3._replace(count = c3.count + 1)
            print(c3.count)
            if c3.count == 4:
                c3 = c3._replace(straight = True)
        else:
            if not c3.straight:
                c3 = c3._replace(count = 0)

    if c1 + c2 == 5:
        print("Boat!")
    elif c1 > 1 and c2 > 1:
        print("Two pair")
    elif c1:
        print("Pair of A")
    elif c2:
        print("Pair of B")
    print(cards)
    print("Count A:", c1)
    print("Count B:", c2)
    print(c3)
    return "unimplmeneted"

def value_to_string(value):
    if value > 9:
        if value == 10:
            return "J"
        elif value == 11:
            return "Q"
        elif value == 12:
            return "K"
        elif value == 13:
            return "A"
        else:
            raise Exception("Card must be within 0-13")
    return str(value)
    
def suit_to_string(suit):
    if suit == 0:
        return "s"
    elif suit == 1:
        return "h"
    elif suit == 2:
        return "c"
    elif suit == 3:
        return "d"
    else:
        print(suit)
        raise Exception("Suit is not 0-3")