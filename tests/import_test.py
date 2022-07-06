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


# tiles = [
#     Tile('I', [8, 7]),
#     #Tile('B', [7, 7]),
#     Tile('I', [7, 8]),
#     Tile('T', [7, 9]),
#     Tile('E', [7, 10]),
#     Tile('S', [7, 11]),
#     Tile('T', [6, 10]),
#     Tile('S', [8, 10]),
#     Tile('S', [7, 0]),
#     Tile('I', [7, 1]),
# ]

# board = Board(tiles)
# print(board)
# words = board.get_words_on_board()
# print(words)

# compare = board.compare_words([Tile('E', (7, 9)), Tile('B', [7, 7])])
# print(compare)

# print(board.score_word([Tile('E', (6, 9)), Tile('B', [7, 7])]))