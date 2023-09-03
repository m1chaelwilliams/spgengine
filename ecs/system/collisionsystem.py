from spgengine.ecs.entity import Entity
from spgengine.ecs.components.collider import Collider
from spgengine.ecs.components.rigidbody import RigidBody

class CollisionSystem:
    def __init__(self) -> None:
        self.entities: list[Entity] = []
    def add_entity(self, entity: Entity):
        if entity.get_component(Collider):
            self.entities.append(entity)
    def remove_entity(self, entity: Entity):
        if entity in self.entities:
            self.entities.remove(entity)
    def check_collisions(self, direction: str):
        for entity in self.entities:
            collider1 = entity.get_component(Collider)
            if not collider1.static:
                for entity2 in self.entities:
                    if entity != entity2:
                        collider2 = entity2.get_component(Collider)
                        if collider1.rect.colliderect(collider2.rect):
                            if entity.has_component(RigidBody):
                                entity.get_component(RigidBody).on_collision(direction, collider2)
                            if entity2.has_component(RigidBody):
                                entity2.get_component(RigidBody).on_collision(direction, collider1)
    def update(self):
        self.check_collisions("horizontal")
        self.check_collisions("vertical")