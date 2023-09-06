import pygame

class FontManager:
    def __init__(self) -> None:
        self.default_font_size = 25
        self.fonts: dict[str, pygame.font.Font] = {}
    def set_default_font_size(self, size: int) -> None:
        self.default_font_size = size
    def load_font(self, name: str, path: str, size: int) -> None:
        try:
            self.fonts[name] = pygame.font.Font(path, size)
        except:
            pass
    def load_sysfont(self, name: str, font_name: str, size: int) -> None:
        try:
            self.fonts[name] = pygame.font.SysFont(font_name, size)
        except:
            pass
    def get_font(self, name: str) -> pygame.font.Font:
        return self.fonts.get(name, pygame.font.Font(None, self.default_font_size))