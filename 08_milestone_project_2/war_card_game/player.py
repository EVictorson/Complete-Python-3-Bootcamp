class Player:
    """
    A class to represent a person playing a card game.

    ...

    Attributes
    ----------
    name : str
        player's name.
    all_cards : [card]
        list of cards in the players hand.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def remove_one_card(self):
        """ remove one card from the player """
        return self.hand.pop()

    def add_cards(self, new_cards):
        """ add cards to the player in the event they won """
        if isinstance(new_cards, list):
            # If a list of cards is passed, extend the current list
            self.hand.extend(new_cards)
        else:
            # If a single card is passed, just append it to the current list
            self.hand.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.hand))


if __name__ == '__main__':
    new_player = Player("Eric")
    print(new_player)
