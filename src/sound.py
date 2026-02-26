# sound.py

import pygame
from settings import SOUND_SETTINGS

def update_background_music():
    if SOUND_SETTINGS["background"]:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()