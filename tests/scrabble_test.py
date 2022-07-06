from scrabble_python import Scrabble

board_size = 15
rack_size = 7
lang = 'fr'


def test_scrabble_init():
    scrabble = Scrabble(board_size=board_size, rack_size=rack_size, lang=lang)
    assert len(scrabble.players) == scrabble.nb_players == 2
    assert [len(player.rack) for player in scrabble.players] == [rack_size] * scrabble.nb_players
    assert len(scrabble.purse) == 102 - (rack_size*scrabble.nb_players)
