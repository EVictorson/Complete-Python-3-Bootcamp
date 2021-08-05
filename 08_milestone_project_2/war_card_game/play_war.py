import player, deck, card

class PlayWar:
    NUM_DRAWN_CARDS = 3

    def __init__(self):
        self.player1 = player.Player("one")
        self.player2 = player.Player("Two")
        self.player1_played_cards = []
        self.player2_played_cards = []

        self.new_deck = deck.Deck()
        self.new_deck.shuffle()
        self.deal_cards()
        self.round_number = 0
        self.game_on = True
        self.at_war = True


    def play(self):
        while self.game_on:
            self.round_number += 1
            print(f"Round {self.round_number}")

            if self.check_win_condition():
                break
            self.start_next_round()

            while self.at_war:
                # Use last card to always be comparing last card when war occurs
                if self.player1_played_cards[-1].value > self.player2_played_cards[-1].value:
                    self.player1.add_cards(self.player1_played_cards)
                    self.player1.add_cards(self.player2_played_cards)

                    self.at_war = False

                elif self.player2_played_cards[-1].value > self.player1_played_cards[-1].value:
                    self.player2.add_cards(self.player1_played_cards)
                    self.player2.add_cards(self.player2_played_cards)

                    self.at_war = False

                else:
                    print('WAR!')

                    if len(self.player1.hand) < self.NUM_DRAWN_CARDS:
                        print("Player one unable to declare war")
                        print("Player Two Wins!")
                        self.game_on = False
                        break

                    elif len(self.player2.hand) < self.NUM_DRAWN_CARDS:
                        print("Player two unable to declare war")
                        print("Player One Wins!")
                        self.game_on = False
                        break

                    else:
                        for num in range(self.NUM_DRAWN_CARDS):
                            self.player1_played_cards.append(self.player1.remove_one_card())
                            self.player2_played_cards.append(self.player2.remove_one_card())


    def deal_cards(self):
        for i in range(int(card.Card.MAX_COUNT/2)):
            self.player1.add_cards(self.new_deck.deal_one_card())
            self.player2.add_cards(self.new_deck.deal_one_card())

    def check_win_condition(self):
        if self.check_player_one_win() or self.check_player_two_win():
            return True

        return False

    def check_player_one_win(self):
        if len(self.player2.hand) == 0:
            print("Player two is out of cards!  Player one wins!")
            self.game_on = False
            return True
        return False

    def check_player_two_win(self):
        if len(self.player1.hand) == 0:
            print("Player one is out of cards!  Player two wins!")
            self.game_on = False
            return True
        return False

    def start_next_round(self):
        self.player1_played_cards = []
        self.player1_played_cards.append(self.player1.remove_one_card())

        self.player2_played_cards = []
        self.player2_played_cards.append(self.player2.remove_one_card())



if __name__ == '__main__':
    pw = PlayWar()
    pw.play()
