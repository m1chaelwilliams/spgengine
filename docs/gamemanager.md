# SPG Game Manager

This is the center piece of SPGEngine. It contains the main game loop 
and all important starting proceedures.

## Method List

```python
GameManager()
```
Tasks:
- Creates `pygame.time.Clock()` object.
- Sets FPS to 0 (Uncapped by default)
- Creates `SceneManager()` object.