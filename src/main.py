# main.py

import pygame
from selection import run_selection
from gameover_screen import run_game_over
import highscore
from run import run_flappy
from sound import update_background_music


class GameInitializer:
    '''
    Responsible for initializing the global game system.
    '''
    @staticmethod
    def initialize():
        '''Initializes pygame, sound system and highscore.'''
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load("../assets/sounds/background_music.wav")
        pygame.mixer.music.set_volume(0.1)

        highscore.load_highscore()


class MainGameLoop:
    '''Controls game loop (selection, starting, gameover, ...'''
    def __init__(self):
        '''Saves last selected animal for replay.'''
        self.last_animal = None

    def run(self):
        '''Runs main game loop'''
        update_background_music()

        while True:
            # startscreen or back to menu
            if not self.last_animal:
                choice = run_selection()
                self.last_animal = choice
            else:
                choice = self.last_animal

            update_background_music()

            # start the gameplay
            score = run_flappy(choice)

            # Game Over Screen and update highscore if necessary.
            highscore.update_highscore(score)
            action, self.last_animal = run_game_over(score, choice)

            # Return to menu if chosen.
            if action == "BACK_TO_MENU":
                self.last_animal = None


if __name__ == "__main__":
    '''Entry point for game: Initializes systems'''
    GameInitializer.initialize()
    game = MainGameLoop()
    game.run()