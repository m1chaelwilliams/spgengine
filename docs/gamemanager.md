# SPG Game Manager

This is the center piece of SPGEngine. It contains the main game loop 
and all important starting proceedures.

## Method List

### Note: Most methods return the `GameManager()` instance for easy method stringing.

```python
GameManager()
```
Tasks:
- Creates `pygame.time.Clock()` object.
- Sets FPS to 0 (Uncapped by default).
- Creates `SceneManager()` object.

```python
def create_display(self, win_size: tuple[int, int], *flags)
```
Tasks:
- Creates pygame display.
- Creates [Window Manager](./windowmanager.md) instance.

```python
def set_fps(self, fps: float)
```
Tasks:
- Sets FPS for application instance.

```python
def add_scene(self, name: str, scene: BaseScene)
```
Tasks:
- Adds scene to scene manager.
- Lazy injects the following:
    - `WindowManager()`
    - `pygame.time.Clock()`
    - `SceneManager()`