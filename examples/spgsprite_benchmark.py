import pygame
from spgengine import *
from spgengine.sprite import *
import random

COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
]

class BenchMarkScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
    def on_load(self) -> None:
        self.sprites: list[SPGSprite] = []

        return super().on_load()
    def spawn_10(self):
        for x in range(10):
            surf = pygame.Surface(
                (random.randint(1, 100), random.randint(1, 100))
            )
            surf.fill(random.choice(COLORS))

            self.sprites.append(
                SPGSprite(
                    [],
                    surf,
                    Transform(
                        pygame.Rect(
                            random.randint(0, 1280),
                            random.randint(0, 1280),
                            1,
                            1
                        ),
                        30,
                        30
                    )
                )
            )
    def update(self, dt: int) -> None:
        if self.clock.get_fps() > 60:
            self.spawn_10()
        for sprite in self.sprites:
            sprite.transform.rect.x += sprite.transform.dx * dt
            sprite.transform.rect.y += sprite.transform.dy * dt
            if sprite.transform.position.x > 1280 or sprite.transform.position.y > 720:
                self.sprites.remove(sprite)

        pygame.display.set_caption(f'SPGEngine Benchmark: {round(self.clock.get_fps()) = }, {len(self.sprites) = }')

        return super().update(dt)
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill('black')
        for sprite in self.sprites:
            sprite.draw(surface, Vector2(0,0))

        return super().draw(surface)

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .add_scene('benchmark', BenchMarkScene())\
        .set_active_scene('benchmark')\
        .start()