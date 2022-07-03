from tile import Tile


class Rack(list[Tile]):
    def __init__(self, joueur_id: str, tiles: list[Tile], size: int = 7):
        self.size = size
        self.joueur_id = joueur_id
        if len(tiles) > self.size:
            raise ValueError('Too much tiles, max is 7')
        self = tiles
