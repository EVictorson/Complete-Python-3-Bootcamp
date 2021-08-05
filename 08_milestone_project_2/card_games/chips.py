class Chips:

    def __init__(self, num_chips=100):
        self.total = num_chips
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
