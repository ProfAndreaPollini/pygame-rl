from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import App


class Scene:
    def __init__(self, name: str, app: "App"):
        self.name = name
        app.scenes[self.name] = self
        self.app = app

    def update(self):
        ...

    def draw(self):
        ...
