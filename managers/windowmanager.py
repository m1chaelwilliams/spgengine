import pygame
from spgengine.io import Eventhandler

class WindowManager:
    '''
    Manages application screen. Allows for extended functionality via a "proxy screen".
    '''
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen: pygame.Surface = screen
        self.proxy_screen: pygame.Surface = None
        self.proxy_scale = 0
        self.proxy_flags = None

    def close(self):
        '''
        Sends a close request event to the Game Manager completely terminating the application.
        '''
        Eventhandler.close_requested = True
    def config_window(self, size: tuple[int, int], *flags) -> pygame.Surface:
        '''
        Resets screen with new configuration. If a proxy screen exists, adjusts to new main screen.
        '''
        self.screen = pygame.display.set_mode(size, *flags)
        if self.proxy_screen:
            self.create_proxy_screen(
                (self.screen.get_width() / self.proxy_scale, self.screen.get_height() / self.proxy_scale),
                *self.proxy_flags
            )
    def create_proxy_screen(self, size: tuple[int, int], *flags) -> pygame.Surface:
        '''
        Creates a proxy screen. (Typically used for scaling up pixel art)
        '''
        self.proxy_screen = pygame.Surface(size, *flags)
        self.proxy_scale = self.screen.get_width() / size[0]
        self.proxy_flags = flags
    def get_proxy_mouse_pos(self) -> tuple[int, int]:
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0] / self.proxy_scale, mouse_pos[1] / self.proxy_scale)