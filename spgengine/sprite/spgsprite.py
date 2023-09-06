from typing import Any
import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2

VEC2ZERO = Vector2(0,0)

class SPGSprite(Sprite):
    def __init__(self, 
                 groups,
                 image: pygame.Surface,
                 position: Vector2 = VEC2ZERO,
                 velocity: Vector2 = VEC2ZERO,
                 layer: int = 0
                 ) -> None:
        self._layer = layer
        super().__init__(groups)
        self.og_image = image
        self.image = image
        
        self.rect = self.image.get_rect(topleft = position)
        self.velocity = velocity
    @property
    def position(self) -> Vector2:
        return Vector2(*self.rect.topleft)
    def update(self, dt: int) -> None:
        pass
    def draw(self, surface: pygame.Surface, offset: Vector2 = VEC2ZERO) -> None:
        surface.blit(
            self.image,
            (
                self.rect.x + offset.x,
                self.rect.y + offset.y
            )
        )

class SPGSpriteLite(Sprite):
    def __init__(self, groups, image: pygame.Surface, position: Vector2 = VEC2ZERO) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)