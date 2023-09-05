from spgengine.scenes import BaseScene
from typing import TypeVar, Type

T = TypeVar('T')

class SceneManager:
    def __init__(self) -> None:
        self.scenes: dict[str, BaseScene] = {}
        self.active_scene = ''
        self.prev_scene = ''
    def add_scene(self, name: str, scene: BaseScene):
        self.scenes[name] = scene
    def get_scene(self, name: str, type: Type[T] = BaseScene) -> T:
        return self.scenes.get(name)
    def get_active_scene(self) -> BaseScene:
        return self.scenes.get(self.active_scene)
    def set_scene(self, name: str, enter_args: list[any] = [], exit_args: list[any] = []) -> None:
        if not self.scenes[name].loaded:
            self.scenes[name].on_load()
        
        self.prev_scene = self.active_scene
        self.active_scene = name

        self.scenes[self.active_scene].on_scene_enter(*enter_args)
        if self.prev_scene:
            self.scenes[self.prev_scene].on_scene_exit(*exit_args)
        
    def remove_scene(self, name: str) -> BaseScene:
        return self.scenes.pop(name)