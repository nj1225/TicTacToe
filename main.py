#import math
import random



class Player:

    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, games):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, games):
        # get a random valid spot for our next move
        square = random.choice(games.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, games):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.input move(0-8):')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it is not,then we say it is VALID
            # if that is not available on the board,we also say it is invalid
            try:
                val = int(square)
                if val not in games.available_moves():
                    raise ValueError
                valid_square = True  # if there are succesful,then YAHHH!!!
            except ValueError:
                print('Invalid square .Try again')

        return val