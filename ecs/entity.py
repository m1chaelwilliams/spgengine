from typing import TypeVar, Type, Optional
from pygame import Surface

T = TypeVar('T')

class Entity:
    def __init__(self) -> None:
        self.components: dict[Type[T], T] = {}
    def get_component(self, component_type: Type[T]) -> Optional[T]:
        return self.components.get(component_type)
    def has_component(self, component_type: Type[T]) -> bool:
        return component_type in self.components.keys()
    def add_component(self, component: T):
        self.components[type(component)] = component
        return self
    def update(self, dt):
        for component in self.components.values():
            if hasattr(component, 'update'):
                component.update(dt)
    def draw(self, surface: Surface):
        pass
    def on_collision(self):
        pass