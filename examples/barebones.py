import pygame
from spgengine import *

if __name__ == "__main__":
    GameManager()\
        .create_display((1280, 720))\
        .set_fps(120)\
        .set_title("SPGEngine Example: Barebones")\
        .add_scene('main', BaseScene())\
        .set_active_scene('main')\
        .start()