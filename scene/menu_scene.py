import sys


from core.scene import Scene
from typing import TYPE_CHECKING

from transitions import FadeInFromColor


if TYPE_CHECKING:
    from main import App

import pygame as pg

MENU_OFFSET = 100


class MenuScene(Scene):
    def __init__(self, app: "App"):
        super().__init__("MENU_SCENE", app)
        self.fade_in = FadeInFromColor(*self.app.screen.get_size(), duration_ms=1000)

        self.menu_items = [("PLAY", "PLAY_SCENE"), ("EXIT", "EXIT_SCENE")]
        self.selected = 0  # voce di menu selezionata

    def update(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_DOWN:
                        self.selected += 1
                        self.selected %= len(self.menu_items)
                        self.app.sounds.play("ui_select")
                    case pg.K_UP:
                        self.selected -= 1
                        if self.selected < 0:
                            self.selected += len(self.menu_items)
                        self.selected %= len(self.menu_items)
                        self.app.sounds.play("ui_select")

                    case pg.K_RETURN:
                        self.app.set_scene(self.menu_items[self.selected][1])
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def draw(self):
        text_surface = self.app.fonts["title"].render(f"BIGOLO", True, (255, 255, 255))

        text_rect = text_surface.get_rect()
        # Get the width and height of the screen
        screen_width, screen_height = self.app.screen.get_size()

        # Calculate the position to draw the text at
        text_x = screen_width / 2 - text_rect.width / 2
        text_y = screen_height / 2 - text_rect.height / 2

        self.app.screen.blit(text_surface, dest=(text_x, 50))

        h = 30
        for name, scene_name in self.menu_items:
            col = (
                (255, 0, 0)
                if name == self.menu_items[self.selected][0]
                else (255, 255, 255)
            )
            text_surface = self.app.fonts["title"].render(name, True, col)
            text_rect = text_surface.get_rect()
            # Get the width and height of the screen
            # screen_width, screen_height = self.app.screen.get_size()

            # Calculate the position to draw the text at
            text_x = screen_width / 2 - text_rect.width / 2
            text_y = (screen_height - MENU_OFFSET + h) / 2 - text_rect.height / 2
            h += text_rect.height + 50

            self.app.screen.blit(text_surface, dest=(text_x, text_y))

        if not self.fade_in.update():
            self.fade_in.draw(self.app.screen)
