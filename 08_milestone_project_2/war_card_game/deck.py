import random
import card

class Deck:
    """
    A class to represent a standard 52 card playing deck.

    ...

    Attributes
    ----------
    all_cards : list[card]
        list of card objects

    """

    def __init__(self):
        self.all_cards = []
        self._create_deck()

    def _create_deck(self):
        """Creates the deck."""
        for suit in card.Card.POSSIBLE_SUITS:
            for rank in card.Card.POSSIBLE_RANKS:
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """Shuffles the deck. """
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        """
        Pops one card off the top of the all_cards list
        Returns card object.
        """
        return self.all_cards.pop()


if __name__ == '__main__':
    deck = Deck()
    print(deck.all_cards)

    print("\nShuffling deck.\n")
    deck.shuffle()
    print(deck.all_cards)

    print("\nnumber of cards created = {}".format(deck.all_cards[0].count))

    card = deck.deal_one_card()
    print("\nnumber of cards created = {}".format(deck.all_cards[0].count))
