# SPG Texture Manager

Caches textures. Manages textures into "stores".

stores = containers of sprites. Allows for different textures with the same name idenfier.

Texture Manager cache Data Structure:
```py
stores: dict[str, dict]
    ---> store: dict[str, Surface]
    --------> key = ID
    --------> value = texture
```

A default store is installed under the name `default`. When a store is not specified, textures are stored/retrieved from this store.

## Method List

```py
TextureManager()
```
 - Creates `stores` dictionary
 - Installs default `store` in `stores` under the name "default".

```py
add_texture(self, name: str, texture: pygame.Surface, stores: list[str] = []) -> None
```
 - If `stores` are passed, `texture` is added to each store with the given `name` key identifier.
 - it `stores` are not passed, `texture` is added to "default" store.

```py
get_texture(self, name: str, store: str = "default") -> pygame.Surface
```
 - Returns texture with ID = `name` in `store`.

```py
clear(self) -> None
```
 - Clears store list.

```py
clear_store(self, store: str) -> None
```
 - Clears specified store.

```py
clear_stores(self) -> None
```
 - Empties all stores.

```py
set_default_texture(self, texture: pygame.Surface)
```
 - Sets default texture that is returned when a texture is not found.