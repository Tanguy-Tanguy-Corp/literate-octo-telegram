from scrabble_python.items import Tile
from scrabble_python.items import Word
from scrabble_python.items import Purse
from scrabble_python.items import Board

def test_tile_import():
    tile = Tile('A', (0, 0))
    assert isinstance(tile, Tile)

def test_word_import():
    word = Word('test', (0,0))
    assert isinstance(word, Word)

def test_purse_import():
    purse = Purse()
    assert isinstance(purse, Purse)

def test_board_import():
    board = Board()
    assert isinstance(board, Board)
