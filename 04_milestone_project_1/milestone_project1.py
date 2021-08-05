#!/usr/bin/env python3

class TicTacToe:
    """
    Class to play a game of tictactoe
    """
    WIN_SCENARIOS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    PLAYER_SYMBOLS = ['X', 'O']
    EMPTY_SPACE = ' '

    def __init__(self):
        super().__init__()
        self.board = [self.EMPTY_SPACE]*9
        self.replay = False
        self.player_num = 0
        self.input_valid = False
        self.replay = 'y'

    def display_board(self):
        board = self.board
        print('\n\n')
        print(board[6] + '|' + board[7] + '|' + board[8])
        print('-----')
        print(board[3] + '|' + board[4] + '|' + board[5])
        print('-----')
        print(board[0] + '|' + board[1] + '|' + board[2])
        print('\n\n')

    def stalemate_check(self):
        if self.EMPTY_SPACE in self.board:
            return False
        else:
            print("\nIt's a Draw!\n")
            self.get_replay_input()

            return True

    def get_user_input(self):
        self.input_valid = False
        while not self.input_valid:
            player_input = input('Player{}: Enter your mark position:\n'.format(self.player_num + 1))
            self.validate_user_input(player_input)
        player_input = self.cast_to_board_number(player_input)
        self.place_mark_on_board(player_input)
        self.toggle_player_num()

    def validate_user_input(self, player_input):
        ret = True
        ret = self.check_if_input_is_digit(player_input)
        if not self.check_if_input_is_digit(player_input):
            return False
        player_input = self.cast_to_board_number(player_input)
        if not self.check_if_input_in_range(player_input):
            return False
        if not self.check_if_input_space_empty(player_input):
            return False
        self.input_valid = ret
        return ret

    def check_if_input_is_digit(self, player_input):
        if not player_input.isdigit():
            print('{} is not a valid digit.  Please enter a valid selection.'.format(player_input))
            return False
        return True

    def check_if_input_in_range(self, player_input):
        if not player_input in range(9):
            print('{} is not in the range 1-9.  Please enter a valid selection'.format(player_input))
            return False
        else:
            return True

    def check_if_input_space_empty(self, player_input):
        if self.board[player_input]!= self.EMPTY_SPACE:
            print('Board position {} is already taken.  Please enter a valid selection.'.format(player_input))
            return False
        return True

    def cast_to_board_number(self, player_input):
        """
        Convert from 1 indexed keypad to 0 indexed list position
        """
        return int(player_input) - 1

    def toggle_player_num(self):
        self.player_num = not self.player_num

    def place_mark_on_board(self, player_input):
        self.board[player_input] = self.PLAYER_SYMBOLS[self.player_num]

    def check_for_winner(self):
        for win_scenario in self.WIN_SCENARIOS:
            if self.board[win_scenario[0]] == self.board[win_scenario[1]] == self.board[win_scenario[2]] and not self.board[win_scenario[0]] == self.EMPTY_SPACE:
                return self.display_winning_player(win_scenario[0])

        return False

    def display_winning_player(self, board_position):
        if self.board[board_position] == self.PLAYER_SYMBOLS[0]:
            print("\nPLAYER1 WINS!")
            self.get_replay_input()
            return True
        elif self.board[board_position] == self.PLAYER_SYMBOLS[1]:
            print("\nPLAYER2 WINS!")
            self.get_replay_input()
            return True
        return False

    def get_replay_input(self):
        self.replay = input('\nWould you like to play again? (y/n)\n')

    def check_for_replay(self):
        if self.replay == 'y':
            return True
        else:
            return False

    def reset_board(self):
        self.board = [self.EMPTY_SPACE]*9
        self.player_num = 0

    def display_startup_message(self):
        print("Welcome to TicTacToe!\n")
        print("Using the keypad, select where you would like to place marks.")

    def run(self):
        self.display_startup_message()
        while self.check_for_replay():
            self.reset_board()
            self.display_board()

            while not self.check_for_winner() and not self.stalemate_check():
                self.get_user_input()
                self.display_board()



if __name__ == '__main__':
    game = TicTacToe()
    game.run()
