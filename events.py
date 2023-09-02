import pygame
from pygame.event import Event

class Eventhandler:
    '''
    Takes polled events and caches them for effeciency purposes
    '''

    # cached states
    mouse: dict[int, bool] = {}
    mouse_held: dict[int, bool] = {}
    keys_pressed: list = []
    keys_held: list = []
    close_requested: bool = False
    
    events: list[Event] = []

    @staticmethod
    def process_events(events: list[Event]) -> None:
        Eventhandler.events = events

        Eventhandler.mouse.clear()
        Eventhandler.keys_pressed.clear()
        Eventhandler.close_requested = False

        for e in events:
            # mouse events
            if e.type == pygame.MOUSEBUTTONDOWN:
                Eventhandler.mouse[e.button] = True
                Eventhandler.mouse_held[e.button] = True
            if e.type == pygame.MOUSEBUTTONUP:
                Eventhandler.mouse_held[e.button] = False
            # keyboard events
            if e.type == pygame.KEYDOWN:
                Eventhandler.keys_pressed.append(e.key)
                Eventhandler.keys_held.append(e.key)
            if e.type == pygame.KEYUP:
                if e.key in Eventhandler.keys_held:
                    Eventhandler.keys_held.remove(e.key)
            if e.type == pygame.QUIT:
                Eventhandler.close_requested = True
    @staticmethod
    def keydown(key) -> bool:
        return key in Eventhandler.keys_pressed
    @staticmethod
    def keydown_any() -> bool:
        return len(Eventhandler.keys_pressed) > 0
    @staticmethod
    def keyheld_any() -> bool:
        return len(Eventhandler.keys_held) > 0
    @staticmethod
    def keyheld(key) -> bool:
        return key in Eventhandler.keys_held
    @staticmethod
    def clicked(button: int = 1) -> bool:
        return Eventhandler.mouse.get(button, False)
    @staticmethod
    def clickheld(button: int = 1) -> bool:
        return Eventhandler.mouse_held.get(button, False)