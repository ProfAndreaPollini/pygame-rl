import sys
from core.camera import Camera


from core.scene import Scene
from typing import TYPE_CHECKING

from transitions import FadeInFromColor


if TYPE_CHECKING:
    from main import App

import pygame as pg


class PlayScene(Scene):
    def __init__(self, app: "App"):
        super().__init__("PLAY_SCENE", app)
        self.need_map_generation = True
        # self.fade_in = FadeInFromColor(*self.app.screen.get_size(), duration_ms=1000)
        self.camera = Camera(app)

    def generate_level(self):
        world = self.app.world
        for x in range(world.CAMERA_COLS):
            for y in range(world.CAMERA_ROWS):
                tile_name = "floor"
                if (
                    x == 0
                    or x == world.CAMERA_COLS - 1
                    or y == 0
                    or y == world.CAMERA_ROWS - 1
                ):
                    idx = x + world.CAMERA_COLS * y
                    tile_name = "wall"
                self.app.world.map[idx] = world.create_map_tile("wall")

        world.update_surface()

    def update(self):
        if self.need_map_generation:
            print("GENERATING LEVEL...")
            self.generate_level()
        for event in pg.event.get():
            # if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            #     self.app.set_scene("MENU_SCENE")
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                self.app.player.update(event)
                self.camera.pos.x = (
                    self.app.player.position.x - self.camera.size[0] // 2
                )
                self.camera.pos.y = (
                    self.app.player.position.y - self.camera.size[1] // 2
                )

    def draw(self):
        cr = self.camera.get_rect()
        self.app.screen.blit(self.app.world.surface, (-cr[0], -cr[1]))
        self.app.entity_renderer.draw(self.app.player)
        text_surface = self.app.fonts["title"].render(
            f"BIGOLO PLAY", True, (255, 255, 255)
        )

        self.app.screen.blit(text_surface, dest=(100, 250))

        # if not self.fade_in.update():
        #     self.fade_in.draw(self.app.screen)
