from enum import Enum
from typing import Dict, List, Sequence


import pygame as pg

from world import World


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def rel_pos(self, dx: int, dy: int):
        return self + Position(dx, dy)


class Direction(Enum):
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
    UP = Position(0, -1)
    DOWN = Position(0, 1)


class Entity:
    def __init__(self, position: Position, sprite, world: World):
        self.position = position
        self.sprites: Dict[str, pg.surface.Surface] = {}
        self.sprites["default"] = sprite
        self.world = world

    @property
    def sprite(self):
        return self.sprites["default"]


class EntityRenderer:
    """Classe che rappresenta chi si deve occupare di renderizzare una entitá"""

    def __init__(self, surface: pg.surface.Surface, tile_size) -> None:
        """
        Inizializza un nuovo oggetto EntityRenderer.

        Args:
          surface (pg.surface.Surface): La superficie sulla quale verrà disegnata l'entità.

          tile_size (Tuple[int, int]): le dimensioni di una tile
        """
        self.surface = surface
        self.tile_size = tile_size

    def draw(self, entity: Entity):
        """
        Disegna l'entità sulla superficie specificata durante l'inizializzazione dell'oggetto EntityRenderer.

        Args:
          entity (Entity): L'entità da disegnare.
        """
        self.surface.blit(
            entity.sprite,
            (
                entity.position.x * self.tile_size[0],
                entity.position.y * self.tile_size[1],
            ),
        )


class Item:
    ...


class Inventory:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items: List[Item] = []


class Player(Entity):
    def __init__(self, position: Position, sprite, world: World):
        super().__init__(position, sprite, world)
        self.speed = 1
        self.inventory = Inventory(4)

    def move(self, direction):
        self.position.x += direction.value.x * self.speed
        self.position.y += direction.value.y * self.speed

    def move_rel(self, dx: int, dy: int):
        self.position.x += dx * self.speed
        self.position.y += dy * self.speed

    def update(self, event):
        dx = dy = 0
        if event.type == pg.KEYDOWN:
            # A key has been pressed
            match event.key:
                case pg.K_LEFT:
                    dx = -1
                case pg.K_RIGHT:
                    dx = 1
                case pg.K_UP:
                    dy = -1
                case pg.K_DOWN:
                    dy = 1

        if (dx, dy) != (0, 0) and self.world.is_walkable(self.position.rel_pos(dx, dy)):
            self.move_rel(dx, dy)
