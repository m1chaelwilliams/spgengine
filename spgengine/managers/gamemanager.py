import pygame
from spgengine.io import Eventhandler
from spgengine.managers.scenemanager import SceneManager
from spgengine.managers.windowmanager import WindowManager
from spgengine.scenes.basescene import BaseScene
import sys

class GameManager:
    DEFAULT_WIN_SIZE = (1280, 720)
    DEFAULT_FLAGS = []

    def __init__(self,) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 0

        self.scene_manager = SceneManager()
    def start(self) -> None:
        while not Eventhandler.close_requested:
            self.update()
            self.draw()
        self.close()
    def update(self):
        Eventhandler.process_events(pygame.event.get())
        dt = self.clock.tick(self.fps) / 1000

        self.scene_manager.get_active_scene().update(dt)
    def draw(self):
        self.scene_manager.get_active_scene().draw(self.window_manager.screen)
        pygame.display.update()
    def close(self) -> None:
        pygame.quit()
        sys.exit()

    # utils
    def create_display(self,
                       win_size: tuple[int, int],
                       *flags
                       ):
        screen = pygame.display.set_mode(win_size, *flags)
        self.window_manager = WindowManager(screen)
        return self
    def set_fps(self, fps: float):
        self.fps = fps
        return self
    def add_scene(self, name: str, scene: BaseScene):
        self.scene_manager.add_scene(name, scene)
        if self.window_manager:
            scene.window_manager = self.window_manager
        else:
            self.create_display(GameManager.DEFAULT_WIN_SIZE, GameManager.DEFAULT_FLAGS)
        scene.clock = self.clock
        scene.scene_manager = self.scene_manager
        return self
    def add_scenes(self, scenes: dict[str, BaseScene]):
        for name, scene in scenes.items():
            self.add_scene(name, scene)
        return self
    def remove_scenes(self, scenes: list[str]):
        for name in scenes.keys():
            self.scene_manager.remove_scene(name)
        return self
    def remove_scene(self, name: str):
        self.scene_manager.remove_scene(name)
        return self
    def set_active_scene(self, name: str):
        if name in self.scene_manager.scenes:
            self.scene_manager.set_scene(name)
        return self
    def set_default_scene(self, name: str):
        self.DEFAULT_SCENE = self.scene_manager.get_scene(name)
        return self
    def set_title(self, title: str):
        pygame.display.set_caption(title)
        return self
    def set_icon(self, icon_path: str, scale: float = 1):
        icon_surf = pygame.image.load(icon_path).convert_alpha()
        if scale != 1:
            icon_surf = pygame.transform.scale_by(icon_surf, scale)
        
        pygame.display.set_icon(icon_surf)