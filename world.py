from typing import Any, Dict, List
import pygame as pg
import json

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.entity import Position


class MapTile:
    def __init__(self, sprite: pg.surface.Surface, tile_name: str) -> None:
        self.sprite = sprite
        self.tile_name = tile_name


class World:
    def __init__(self, app) -> None:
        self.CAMERA_COLS = 50
        self.CAMERA_ROWS = 40
        self.app = app
        self.spritesheet = app.spritesheet
        self.map: List[MapTile] = []
        self.tiles: Dict[str, Any] = {}
        self.load_from_file()
        print(self.tiles)
        self.__generate_map()

        self.surface = pg.Surface(
            (
                self.CAMERA_COLS * self.spritesheet.tile_size[0],
                self.CAMERA_ROWS * self.spritesheet.tile_size[1],
            )
        )
        self.update_surface()

    def is_walkable(self, pos: "Position"):
        """check if the position {pos} is walkable"""
        idx = self.pos_to_idx(pos)
        tile = self.tiles[self.map[idx].tile_name]
        return tile["walkable"]

    def pos_to_idx(self, pos: "Position"):
        return pos.x + self.CAMERA_COLS * pos.y

    def load_from_file(self):
        with open("assets/tiles.config.json") as fp:
            tiles_config = json.load(fp)
            for tile in tiles_config["tiles"]:
                self.tiles[tile["name"]] = {
                    "sprite": tile["sprite"],
                    "walkable": tile.get("walkable", False),
                }

    def update_surface(self):
        for row in range(self.CAMERA_ROWS):
            for col in range(self.CAMERA_COLS):
                idx = col + self.CAMERA_COLS * row
                tile = self.map[idx]
                self.surface.blit(
                    tile.sprite,
                    (
                        col * self.spritesheet.tile_size[0],
                        row * self.spritesheet.tile_size[1],
                    ),
                )

    def __generate_map(self):
        for row in range(self.CAMERA_ROWS):
            for col in range(self.CAMERA_COLS):
                tile_name = "wall" if col == 20 else "floor"
                self.map.append(self.create_map_tile(tile_name))

        print(f"create {len(self.map)} tiles.")
        # self.map = [self.__create_map_tile("floor") for i in range(2000)]

    def create_map_tile(self, tile_name: str):
        """create a map tile from tile config"""
        tile_config = self.tiles[tile_name]

        tile = MapTile(self.spritesheet.get_sprite(tile_config["sprite"]), tile_name)
        return tile
