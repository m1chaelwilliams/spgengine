import pygame
from pygame import Surface

class TextureManager:
    '''
    Manages all assets into "stores" for organizational purposes.
    If a store is not specified, the texture is thrown in a default 
    pool under the name "default".
    '''
    def __init__(self) -> None:
        self.textures: dict[str, Surface] = {}
        self.stores: dict[str, dict[str, Surface]] = {
            'default':self.textures
        }
        self.DEFAULT_TEXTURE = pygame.Surface((50, 50))

    def set_default_texture(self, texture: Surface):
        self.DEFAULT_TEXTURE = texture
    def add_texture(self, name: str, texture: Surface, stores: list[str] = []):
        if stores:
            for store in stores:
                if store not in self.stores:
                    self.stores[store]: dict[str, Surface] = {}
                self.stores.get(store, self.textures)[name] = texture
        else:
            self.textures[name] = texture
    def get_texture(self, name: str, store: str = "default") -> Surface:
        return self.stores\
                .get(store, self.textures)\
                .get(name, self.DEFAULT_TEXTURE)
    def clear(self):
        for store in self.stores.values():
            store.clear()
    def clear_store(self, store: str):
        if store in self.stores:
            self.stores.get(store).clear()
    def clear_stores(self):
        for store in self.stores.values():
            store.clear()