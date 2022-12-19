import pygame as pg

from .entity import Position
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import App


class Camera:
    def __init__(
        self, app: "App", size=(20, 20), pos: Position = Position(0, 0)
    ) -> None:
        self.pos: Position = pos
        self.app = app
        self.tile_size = self.app.spritesheet.tile_size
        self.size = size

    def apply(self):
        ...

    def get_rect(self):
        topleft = (self.pos.x * self.tile_size[0], self.pos.y * self.tile_size[1])
        return pg.Rect(
            topleft[0],
            topleft[1],
            self.tile_size[0] * self.size[0],
            self.tile_size[1] * self.size[1],
        )
