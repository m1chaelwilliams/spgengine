from spgengine.ecs.entity import Entity
from spgengine.ecs.components.collider import Collider
from spgengine.ecs.components.transform import Transform

class RigidBody:
    def __init__(self,
                 entity: Entity,
                 ) -> None:
        self.entity = entity

        self.transform = self.entity.get_component(Transform)
        self.collider = self.entity.get_component(Collider)
    def on_collision(self, direction: str, opposing_collider: Collider):
        if direction == "horizontal":
            if self.transform.velocity.x > 0:
                self.collider.rect.right = opposing_collider.rect.left
                self.transform.position.x = self.collider.rect.x - self.collider.offset[0]
            elif self.transform.velocity.x < 0:
                self.collider.rect.left = opposing_collider.rect.right
                self.transform.position.x = self.collider.rect.x - self.collider.offset[0]
        elif direction == "vertical":
            if self.transform.velocity.y > 0:
                self.collider.rect.bottom = opposing_collider.rect.top
                self.transform.position.y = self.collider.rect.y - self.collider.offset[1]
            elif self.transform.velocity.y < 0:
                self.collider.rect.top = opposing_collider.rect.bottom
                self.transform.position.y = self.collider.rect.y - self.collider.offset[1]