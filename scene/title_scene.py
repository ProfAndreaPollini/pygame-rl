import sys


from core.scene import Scene
from typing import TYPE_CHECKING

from transitions import FadeInFromColor


if TYPE_CHECKING:
    from main import App

import pygame as pg


class TitleScene(Scene):
    def __init__(self, app: "App"):
        super().__init__("TITLE", app)
        self.fade_in = FadeInFromColor(*self.app.screen.get_size(), duration_ms=1000)

    def update(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.app.set_scene("MENU_SCENE")
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def draw(self):
        text_surface = self.app.fonts["title"].render(f"BIGOLO", True, (255, 255, 255))

        self.app.screen.blit(text_surface, dest=(100, 50))

        if not self.fade_in.update():
            self.fade_in.draw(self.app.screen)
