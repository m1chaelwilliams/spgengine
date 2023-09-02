import pygame

class GroupManager:
    def __init__(self) -> None:
        self.groups: dict[str, pygame.sprite.Group] = {}
    def add_group(self, name, group_type: pygame.sprite.Group):
        self.groups[name] = group_type()
    def get_group(self, name: str):
        return self.groups.get(name)