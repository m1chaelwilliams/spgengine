# SPG Game Manager

This is the center piece of SPGEngine. It contains the main game loop 
and all important starting proceedures.

## Method List

### Note: Most methods return the `GameManager()` instance for easy method stringing.

```python
GameManager()
```
- Creates `pygame.time.Clock()` object.
- Sets FPS to 0 (Uncapped by default).
- Creates `SceneManager()` object.

```python
create_display(self, win_size: tuple[int, int], *flags) -> self
```
- Creates pygame display.
- Creates [Window Manager](./windowmanager.md) instance.

```python
set_fps(self, fps: float) -> self
```
- Sets FPS for application instance.

```python
add_scene(self, name: str, scene_type: Type[T], *args, **kwargs) -> self
```
- Creates scene object of type `scene_type` and passes additional args
- Adds scene to scene manager with `SceneManager().add_scene(name, scene)`.

```python
remove_scene(self, name: str) -> self
```
- Removes scene from scene manager with `SceneManager().remove_scene(name)`

```python
set_active_scene(self, name: str) -> self
```
- Sets active scene to `name`.


```py
set_title(self, title: str) -> self
```
- Sets pygame display title

```py
set_icon(self, icon_path: str, scale: float = 1) -> self
```
- Sets pygame display icon