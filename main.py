from typing import Dict
import pygame as pg
import sys
from core.sound import Sounds
from core.entity import EntityRenderer, Player, Position

from typing import TYPE_CHECKING
from scene.menu_scene import MenuScene
from scene.play_scene import PlayScene
from scene.title_scene import TitleScene


if TYPE_CHECKING:
    from core.scene import Scene

from spritesheet import Spritesheet
from transitions import FadeInFromColor
from world import World

SCREEN_SIZE = (1280, 720)

pg.init()
pg.font.init()
pg.mixer.init()


class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(SCREEN_SIZE, pg.DOUBLEBUF | pg.HWSURFACE)
        pg.display.set_caption("Pygame Roguelike")
        self.spritesheet = Spritesheet(
            "assets/1bitpack_kenney_1.2/Tilesheet/colored_packed.png", 2
        )
        self.scenes: Dict[str, "Scene"] = {}
        title_scene = TitleScene(self)
        menu_scene = MenuScene(self)
        play_scene = PlayScene(self)
        self.current_scene = self.scenes["TITLE"]
        self.fonts = {
            "title": pg.font.Font(None, 60),
            "menu_item": pg.font.Font(None, 18),
        }

        # self.spritesheet.create_sprite("albero", 1, 0)
        self.spritesheet.setup_from_file("assets/sprites.config.json")
        self.world = World(self)
        self.player = Player(
            Position(10, 10), self.spritesheet.get_sprite("player"), self.world
        )
        self.entity_renderer = EntityRenderer(self.screen, self.spritesheet.tile_size)
        self.clock = pg.time.Clock()
        self.sounds = Sounds()

    def set_scene(self, scene_name):
        self.current_scene = self.scenes[scene_name]

    def run(self):

        while True:
            self.screen.fill((50, 50, 50))
            # self.screen.blit(self.world.surface, (0, 0))
            # self.screen.blit(self.spritesheet.get_sprite("albero"), (0, 0))
            # self.player.update()

            # self.entity_renderer.draw(self.player)
            self.current_scene.update()
            self.current_scene.draw()
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         sys.exit()
            # if not fade_in.update():
            #    fade_in.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    app = App()
    app.run()
