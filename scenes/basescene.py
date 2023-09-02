import pygame
from pygame import Surface
from spgengine.managers import *

class BaseScene:
    def __init__(self) -> None:
        self.texture_manager = TextureManager()
        self.font_manager = FontManager()
        self.group_manager = GroupManager()
    def update(self) -> None:
        pass
    def draw(self, surface: Surface) -> None:
        pass