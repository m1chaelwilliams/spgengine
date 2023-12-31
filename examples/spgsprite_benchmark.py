import pygame
from spgengine import *
from spgengine.sprite import *
from random import random, choice

COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
]

class CustomGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
    def sprites(self) -> list[SPGSprite]:
        return super().sprites()

class BenchMarkScene(BaseScene):
    def __init__(self, wm, sm, clock, *args, **kwargs) -> None:
        super().__init__(wm, sm, clock, *args, **kwargs)
    def on_load(self) -> None:
        self.sprites = self.group_manager.add_group('sprites', CustomGroup())

        return super().on_load()
    def spawn_10(self):
        for i in range(10):
            surf = pygame.Surface(
                (int(random() * 24 + 8), int(random() * 24 + 8))
            )
            surf.fill(choice(COLORS))

            x = int(random() * 1280)
            y = int(random() * 720)
            dx = int(random() * 30 + 1)
            dy = int(random() * 30 + 1)

            SPGSprite(
                self.sprites,
                surf,
                Vector2(x, y),
                Vector2(dx, dy)
            )
    def update(self, dt: int) -> None:
        for sprite in self.sprites.sprites():
            sprite.rect.x += sprite.velocity.x * dt
            sprite.rect.y += sprite.velocity.y * dt
            if sprite.rect.x > 1280 or sprite.rect.y > 720:
                self.sprites.remove(sprite)

        fps = self.clock.get_fps()
        if fps > 60:
            self.spawn_10()

        pygame.display.set_caption(f'SPGEngine Benchmark | {round(fps) = }, {len(self.sprites) = }')
        return super().update(dt)
    def draw(self, surface: Surface) -> None:
        surface.fill('black')

        self.sprites.draw(surface)

        return super().draw(surface)

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .add_scene('benchmark', BenchMarkScene)\
        .set_active_scene('benchmark')\
        .start()