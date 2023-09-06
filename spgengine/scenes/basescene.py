import pygame
from pygame import Surface
from spgengine.managers import *
from spgengine.io import Eventhandler

class BaseScene:
    def __init__(self, wm, sm, clock, *args, **kwargs) -> None:
        # managers unique to a scene
        self.texture_manager = TextureManager()
        self.font_manager = FontManager()
        self.group_manager = GroupManager()
        # singleton managers. E.G. Only one instance per application
        self.window_manager: WindowManager = wm
        self.scene_manager: SceneManager = sm
        
        self.clock: pygame.time.Clock = clock

        # states
        self.loaded = False
    def on_load(self) -> None:
        self.loaded = True
    def on_scene_enter(self, *args, **kwargs) -> None:
        pass
    def on_scene_exit(self, *args, **kwargs) -> None:
        pass 
    def update(self, dt: int) -> None:
        pass
    def draw(self, surface: pygame.Surface) -> None:
        pass