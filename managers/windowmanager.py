import pygame
from spgengine.io import Eventhandler
from spgengine.managers.scenemanager import SceneManager
from spgengine.scenes.basescene import BaseScene
import sys

class WindowManager:
    def __init__(self,) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 0

        self.scenes: dict[str, BaseScene] = {
        }
        self.DEFAULT_SCENE = BaseScene()
    def start(self) -> None:
        while not Eventhandler.close_requested:
            self.update()
            self.draw()
        self.close()
    def update(self) -> None:
        Eventhandler.process_events(pygame.event.get())
        dt = self.clock.tick(self.fps) / 1000
        self.scenes.get(SceneManager.get_scene(), self.DEFAULT_SCENE).update(dt)
    def draw(self) -> None:
        self.scenes.get(SceneManager.get_scene(), self.DEFAULT_SCENE).draw(self.screen)
        pygame.display.update()
        
    def close(self) -> None:
        pygame.quit()
        sys.exit()

    # utils
    def create_display(self,
                       win_size: tuple[int, int],
                       *flags
                       ):
        self.screen = pygame.display.set_mode(win_size, *flags)
        return self
    def set_fps(self, fps: float):
        self.fps = fps
        return self
    def add_scene(self, name: str, scene: BaseScene):
        self.scenes[name] = scene
        return self
    def add_scenes(self, scenes: dict[str, BaseScene]):
        for name, scene in scenes.items():
            self.scenes[name] = scene
        return self
    def remove_scenes(self, scenes: dict[str, BaseScene]):
        for name in scenes.keys():
            self.scenes.pop(name)
        return self
    def remove_scene(self, name: str):
        self.scenes.pop(name)
        return self
    def set_active_scene(self, name: str):
        if name in self.scenes:
            SceneManager.set_scene(name)
        return self
    def set_default_scene(self, name: str):
        self.DEFAULT_SCENE = self.scenes.get(name, self.DEFAULT_SCENE)
        return self
    def set_title(self, title: str):
        pygame.display.set_caption(title)
        return self
    def set_icon(self, icon_path: str, scale: float = 1):
        icon_surf = pygame.image.load(icon_path).convert_alpha()
        if scale != 1:
            icon_surf = pygame.transform.scale_by(icon_surf, scale)
        
        pygame.display.set_icon(icon_surf)