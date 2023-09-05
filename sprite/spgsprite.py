from typing import Any
import pygame
from pygame.sprite import Sprite, Group
from pygame.math import Vector2
from spgengine.sprite.spgcomponents import *

class SPGSprite(Sprite):
    def __init__(self,
                 groups: list[Group],  
                 image: pygame.Surface,
                 transform: Transform,
                 depth: int = 0) -> None:
        super().__init__(groups)
        self._image = image
        self.image = self._image
        self.transform = transform
        self.depth = depth
    @property
    def rect(self):
        return self.transform.rect
    def update(self, dt) -> None:
        pass
    def draw(self, surface: pygame.Surface, offset: Vector2) -> None:
        surface.blit(
            self.image,
            (self.transform.rect.x + offset.x,
            self.transform.rect.y + offset[1])
        )
