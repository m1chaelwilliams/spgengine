import pygame
from pygame.math import Vector2

class Transform:
    def __init__(self,
                 rect: pygame.Rect,
                 dx = 0,
                 dy = 0,
                 rotation = 0,
                 pivot: Vector2 = (0,0)) -> None:
        self.rect = rect
        self.dx = dx
        self.dy = dy
        self.rotation = rotation
        self.pivot = pivot
    @property
    def center(self):
        return Vector2(*self.rect.center)
    @property
    def position(self):
        return Vector2(self.rect.x, self.rect.y)
    @property
    def velocity(self):
        return Vector2(self.dx, self.dy)
    
class TopDownController:
    def __init__(self,
                 up = pygame.K_UP,
                 down = pygame.K_DOWN,
                 left = pygame.K_LEFT,
                 right = pygame.K_RIGHT,
                 use = pygame.K_SPACE,
                 select = pygame.K_RETURN) -> None:
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.use = use
        self.select = select

class PlatformerController:
    def __init__(self,
                 left = pygame.K_LEFT,
                 right = pygame.K_RIGHT,
                 jump = pygame.K_SPACE,
                 crouch = pygame.K_DOWN,
                 ) -> None:
        self.left = left
        self.right = right
        self.jump = jump
        self.crouch = crouch