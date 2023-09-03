from pygame.math import Vector2
from spgengine.ecs.entity import Entity

class Transform:
    def __init__(self,
                 entity: Entity,
                 position: tuple[int, int] = (0,0),
                 initial_velocity: tuple[int, int] = (0,0)) -> None:
        self.entity = entity

        self.position = Vector2(*position)
        self.velocity = Vector2(*initial_velocity)
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt