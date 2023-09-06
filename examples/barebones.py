import pygame
from spgengine import *
from spgengine.managers import *

class SimpleScene(BaseScene):
    def __init__(self, wm, sm, clock, *args, clear_color: str) -> None:
        super().__init__(wm, sm, clock)
        self.clear_color = clear_color
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self.clear_color)
        return super().draw(surface)

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .set_fps(120)\
        .set_title("SPGEngine Example: Barebones")\
        .add_scene('main', SimpleScene, clear_color="red")\
        .set_active_scene('main')\
        .start()