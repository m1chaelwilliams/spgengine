from spgengine.scenes import BaseScene
from typing import TypeVar, Type

T = TypeVar('T')

class SceneManager:
    '''
    Manages scenes in application.
    Scenes must inherit from `BaseScene` class.
    Injected into each scene on initialization.
    '''
    
    def __init__(self) -> None:
        '''
        Initializes scene dictionary [str, BaseScene].
        Creates empty variables for `active_scene` and `prev_scene`.
        '''
        self.scenes: dict[str, BaseScene] = {}
        self.active_scene = ''
        self.prev_scene = ''
    def add_scene(self, name: str, scene: BaseScene):
        '''
        Adds [name : scene] pair to `scenes` dictionary.
        '''
        self.scenes[name] = scene
    def get_scene(self, name: str, type: Type[T] = BaseScene) -> T:
        '''
        Returns scene object at `name`. Optional type arg.
        '''
        return self.scenes.get(name)
    def get_active_scene(self) -> BaseScene:
        '''
        Returns active scene.
        '''
        return self.scenes.get(self.active_scene)
    def set_scene(self, name: str, enter_args: list[any] = [], exit_args: list[any] = []) -> None:
        '''
         - Calls `on_load()` if not loaded
         - Sets active scene to `name` and caches previous scene to `prev_scene`
         - Calls `on_scene_enter` and passes `enter_args`
         - Calls `on_scene_exit` on previous scene and passes `exit_args`
        '''
        if not self.scenes[name].loaded:
            self.scenes[name].on_load()
        
        self.prev_scene = self.active_scene
        self.active_scene = name

        self.scenes[self.active_scene].on_scene_enter(*enter_args)
        if self.prev_scene:
            self.scenes[self.prev_scene].on_scene_exit(*exit_args)
        
    def remove_scene(self, name: str) -> BaseScene:
        '''
        Removes scene from `scenes`
        '''
        return self.scenes.pop(name)