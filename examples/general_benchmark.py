import pygame
from pygame.math import Vector2
from spgengine import *
from random import random, choice

COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
]

class Sprite:
    def __init__(self, image: pygame.Surface, position: Vector2) -> None:
        self.image = image
        self.position = position

class BenchMarkScene(BaseScene):
    def __init__(self, wm, sm, clock, *args, **kwargs) -> None:
        super().__init__(wm, sm, clock, *args, **kwargs)
    def spawn_10(self):
        for i in range(10):
            surf = pygame.Surface(
                (int(random() * 24 + 8), int(random() * 24 + 8))
            )
            surf.fill(choice(COLORS))

            x = int(random() * 1280)
            y = int(random() * 720)

            self.sprites.append(
                Sprite(surf, Vector2(x,y))
            )
    def on_load(self) -> None:
        self.sprites: list[Sprite] = []

        return super().on_load()
    def update(self, dt: int) -> None:
        for sprite in self.sprites:
            sprite.position.x += 20 * dt
            sprite.position.y += 20 * dt
            if sprite.position.x > 1280 or sprite.position.y > 720:
                self.sprites.remove(sprite)

        fps = self.clock.get_fps()
        if fps > 60:
            self.spawn_10()

        pygame.display.set_caption(f'SPGEngine Benchmark | {round(fps) = }, {len(self.sprites) = }')
        return super().update(dt)
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill('black')
        for sprite in self.sprites:
            surface.blit(sprite.image, sprite.position)

        return super().draw(surface)

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .set_title("SPGEngine Benchmark")\
        .add_scene('main', BenchMarkScene)\
        .set_active_scene('main')\
        .start()