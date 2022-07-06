from .tile import Tile


class Rack:
    def __init__(self, tiles: list[Tile], size: int = 7):
        self.size = size
        if len(tiles) > self.size:
            raise ValueError('Too much tiles, max is 7')
        self = tiles
