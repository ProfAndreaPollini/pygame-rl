import json

import pygame as pg


class Sounds:
    def __init__(self) -> None:
        self.sounds_data = {}
        with open("assets/sounds.config.json") as fp:
            data = json.load(fp)

        for name, sound_filename in data.items():
            self.sounds_data[name] = pg.mixer.Sound(sound_filename)

    def play(self, name: str):
        s = self.sounds_data.get(name, None)
        if s:
            s.set_volume(1.0)
            s.play()
