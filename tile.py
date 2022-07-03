from uuid import uuid4
from scrabble_helpers import createDistribution


class Tile:
    def __init__(self, tile_id: str=None, letter: str=None, loc=None, lang:str='fr'):
        if tile_id is None:
            tile_id = 'id'
        if letter is None:
            letter = 'A'
        if loc is None:
            loc=[1,1]


        self._id = str(uuid4())
        self.lang = lang
        self.letter = letter
        self.loc = loc
        self.value =self.__get_value()

    def __get_value(self):
        distribution = createDistribution(self.lang, 'dict')
        return distribution[self.letter]['value']