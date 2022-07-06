from .items import Player
from .items import Board
from .items import Purse
from .errors import ScrabbleError


class Scrabble:
    def __init__(self, players: list[Player] = None, purse: Purse = None, board: Board = None, board_size: int = 15, rack_size: int = 7,  lang: str = 'fr') -> None:
        self.lang = lang
        self.board_size = board_size
        self.rack_size = rack_size

        self.players = players
        if self.players is None:
            self.players = [
                Player('player_1', rack_size=self.rack_size),
                Player('player_2', rack_size=self.rack_size)
            ]
        self.nb_players = len(self.players)
        if self.nb_players > 4:
            raise ScrabbleError('4 players max')
        
        self.purse = purse
        self.board = board
        if purse is None or board is None:
            self.__initialize_game()

    def __initialize_game(self):
        self.purse = Purse(lang=self.lang)
        self.board = Board(size=self.board_size)
        for _ in range(self.rack_size):
            for player in self.players:
                player.rack.append(self.purse.draw())
