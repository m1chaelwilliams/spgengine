import pygame
from typing import TypeVar, Type

T = TypeVar('T')

class GroupManager:
    '''
    Houses a list of pygame sprite groups in a string : group dictionary.
    '''
    def __init__(self) -> None:
        '''
        Initializes `self.groups` dictionary
        '''
        self.groups: dict[str, pygame.sprite.Group] = {}
    def add_group(self, name, group: T = pygame.sprite.Group) -> T:
        '''
        Adds [name : group] pair to `self.groups`
        '''
        self.groups[name] = group
        return self.groups[name]
    def remove_group(self, name: str) -> T:
        '''
        Removes [name : group] pair from `self.groups`
        '''
        return self.groups.pop(name)
    def get_group(self, name: str) -> pygame.sprite.Group:
        '''
        Returns group value
        '''
        return self.groups.get(name)
    def get_group_typed(self, name: str, type: Type[T]) -> T:
        '''
        Returns group value with explicit type.
        '''
        group = self.groups.get(name)
        if type(group) == type:
            return group