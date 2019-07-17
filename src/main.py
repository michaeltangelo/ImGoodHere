from classes import (
    Card,
    Board,
    Deck,
    #rand_card, 
    #rand_board,
)
import utils

def main():
    print("Running main.py")
    d = Deck()
    hole_cards = d.draw(2)
    # board = d.draw(5)
    board = [Card.from_int(1), Card.from_int(2), Card.from_int(15), Card.from_int(28), Card.from_int(5)]
    print(utils.best_hand(hole_cards[0], hole_cards[1], board))
    print("Finished main.py")

if __name__ == "__main__":
    main()