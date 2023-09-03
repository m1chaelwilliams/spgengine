import pygame
from spgengine.ecs.entity import Entity
from spgengine.ecs.components.image import Image
from spgengine.ecs.components.transform import Transform

class Collider:
    '''
    Simple collider component.

    "Static" are components that do not move and thus do not need to check for
    collisions.
    '''

    def __init__(self,
                 entity: Entity,
                 offset: tuple[int, int] = (0, 0),
                 size: tuple[int, int] = None,
                 static: bool = False
                 ) -> None:
        self.entity = entity
        self.offset = offset

        # state
        self.static = static

        if size:
            width = size[0]
            height = size[1]
        else:
            width, height = self.entity.get_component(Image).image.get_size()
        
        self.transform_component = self.entity.get_component(Transform)
        self.rect = pygame.Rect(
            self.transform_component.position.x + offset[0],
            self.transform_component.position.y + offset[1],
            width,
            height
        )
    def update(self, dt):
        self.rect.x = self.transform_component.position.x + self.offset[0]
        self.rect.y = self.transform_component.position.y + self.offset[1]