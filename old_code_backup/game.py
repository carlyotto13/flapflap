# game.py
import pygame
from settings import W, H

pygame.font.init()

class GameIndicator:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Bauhaus 93', 60)
        self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)
        self.color = pygame.Color("white")
        self.inst_color = pygame.Color("black")

    def show_score(self, int_score):
        animal_score = str(int_score)
        score = self.font.render(animal_score, True, self.color)
        self.screen.blit(score, (W // 2, 50))

    def instructions(self):
        inst_text1 = "Press SPACE button to Jump,"
        inst_text2 = "Press \"R\" Button to Restart Game."
        ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
        ins2 = self.inst_font.render(inst_text2, True, self.inst_color)
        self.screen.blit(ins1, (95, 400))
        self.screen.blit(ins2, (70, 450))