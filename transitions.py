import pygame as pg


class FadeIn:
    def __init__(self, surface: pg.surface.Surface, duration_ms: int):
        """
        Initialize a fade in transition.

        Parameters:
            surface (pygame.Surface): The surface to fade in.
            duration (int): The duration of the fade in transition in milliseconds.
        """
        self.surface = surface
        self.duration = duration_ms
        self.alpha_delta = 255 / (self.duration / 1000 * 60)
        self.complete = False

    def update(self):
        """
        Update the fade in transition.

        Returns:
            bool: True if the fade in transition is complete, False otherwise.
        """
        if self.complete:
            return True

        current_alpha = self.surface.get_alpha()
        print(current_alpha)
        self.surface.set_alpha(current_alpha + self.alpha_delta)
        if current_alpha + self.alpha_delta >= 255:
            self.complete = True
            return True
        return False


class FadeOut:
    def __init__(self, surface, duration):
        """
        Initialize a fade out transition.

        Parameters:
            surface (pygame.Surface): The surface to fade out.
            duration (int): The duration of the fade out transition in milliseconds.
        """
        self.surface = surface
        self.duration = duration
        self.alpha_delta = 255 / (self.duration / 1000 * 60)
        self.complete = False

    def update(self):
        """
        Update the fade out transition.

        Returns:
            bool: True if the fade out transition is complete, False otherwise.
        """
        if self.complete:
            return True

        current_alpha = self.surface.get_alpha()
        print(current_alpha)
        self.surface.set_alpha(current_alpha - self.alpha_delta)
        if current_alpha - self.alpha_delta <= 0:
            self.complete = True
            return True
        return False


class FadeInFromColor(FadeOut):
    def __init__(
        self, w: int, h: int, duration_ms: int, color: pg.Color = pg.Color(0, 0, 0, 255)
    ):
        surface = pg.surface.Surface((w, h), flags=pg.SRCALPHA).convert_alpha()
        surface.fill(color)
        super().__init__(surface, duration_ms)

    def draw(self, dest: pg.surface.Surface):
        dest.blit(self.surface, (0, 0))


class FadeOutToColor(FadeIn):
    def __init__(
        self, w: int, h: int, duration_ms: int, color: pg.Color = pg.Color(0, 0, 0, 255)
    ):
        surface = pg.surface.Surface((w, h), flags=pg.SRCALPHA).convert_alpha()
        surface.fill(color)
        super().__init__(surface, duration_ms)

    def draw(self, dest: pg.surface.Surface):
        dest.blit(self.surface, (0, 0))
