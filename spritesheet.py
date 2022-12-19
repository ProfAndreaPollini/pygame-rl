from typing import Dict
import pygame as pg
import json


class SpriteNotFound(Exception):
    ...


class Spritesheet:
    def __init__(
        self, filename: str, scale: int = 1, tile_width: int = 32, tile_height: int = 32
    ) -> None:
        self.load_sprite_image(filename, scale)
        self.tile_size = (tile_width, tile_height)
        self.tiles: Dict[str, pg.surface.Surface] = {}

    def setup_from_file(self, fname: str):
        """Carica gli sprite dello spritesheet da un file json su disco"""
        data = None
        with open(fname) as fp:
            data = json.load(fp)
        for sprite in data:
            name = sprite["name"]
            pos = sprite["pos"]
            self.create_sprite(name, pos[0], pos[1])

    def load_sprite_image(self, fname: str, scale: int):
        image = pg.image.load(fname)
        self.sprite_image = pg.transform.scale(
            image, (image.get_width() * scale, image.get_height() * scale)
        )

    def get_sprite(self, name: str) -> pg.surface.Surface:
        if name not in self.tiles.keys():
            raise SpriteNotFound()
        else:
            return self.tiles[name]

    def create_sprite(self, name: str, row: int, col: int) -> None:
        self.tiles[name] = self.get_tile(row, col)

    def get_tile(self, row: int, col: int) -> pg.surface.Surface:
        return self.sprite_image.subsurface(
            pg.Rect(
                col * self.tile_size[0],
                row * self.tile_size[1],
                self.tile_size[0],
                self.tile_size[1],
            )
        )
