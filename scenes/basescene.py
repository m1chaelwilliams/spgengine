import pygame
from pygame import Surface
from spgengine.managers import *
from spgengine.io import Eventhandler

class BaseScene:
    def __init__(self) -> None:
        # managers unique to a scene
        self.texture_manager = TextureManager()
        self.font_manager = FontManager()
        self.group_manager = GroupManager()
        # singleton managers. E.G. Only one instance per application
        self.window_manager: WindowManager = None
        
        self.clock: pygame.time.Clock = None
    def on_load(self) -> None:
        pass
    def update(self, dt: int) -> None:
        pass
    def draw(self, surface: pygame.Surface) -> None:
        pass