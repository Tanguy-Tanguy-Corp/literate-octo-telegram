from uuid import uuid4
from .tile import Tile
from .rack import Rack

class Player:
    def __init__(self, player_id_name:str = None, rack:Rack = None) -> None:
        self.id = player_id_name
        if self.id is None:
            self.id = str(uuid4())