import pygame
from spgengine import *
from spgengine.io import Eventhandler

class SceneSwitch(BaseScene):
    def __init__(self, scene_id: int, bg_color: str) -> None:
        super().__init__()
        self.scene_id = scene_id
        self.bg_color = bg_color
    def update(self, dt: int) -> None:
        if Eventhandler.clicked():
            new_scene = self.scene_id + 1
            if new_scene > 3:
                new_scene = 1
            self.scene_manager.set_scene(str(new_scene))
        return super().update(dt)
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(self.bg_color)
        return super().draw(surface)

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .set_fps(120)\
        .set_title("SPGEngine Example: Multiple Scenes")\
        .add_scenes({
            '1':SceneSwitch(1, 'red'),
            '2':SceneSwitch(2, 'green'),
            '3':SceneSwitch(3, 'blue'),
        })\
        .set_active_scene('1')\
        .start()