from pygame import Surface
from spgengine.ecs.entity import Entity

class Image:
    def __init__(self, 
                 entity: Entity,
                 image: Surface) -> None:
        self.entity = entity

        self.image = image