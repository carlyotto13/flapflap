import pygame
from animal_builder import FrogBuilder, HamsterBuilder, PenguinBuilder, DogBuilder
from animal_director import AnimalDirector


class SelectionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 40)

        self.options = [
            ("Frog", FrogBuilder, (100, 200)),
            ("Hamster", HamsterBuilder, (100, 270)),
            ("Penguin", PenguinBuilder, (100, 340)),
            ("Dog", DogBuilder, (100, 410)),
        ]

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.screen.fill((30, 30, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for text, builder_cls, pos in self.options:
                        rect = pygame.Rect(pos[0], pos[1], 300, 50)
                        if rect.collidepoint(mouse_pos):
                            builder = builder_cls()
                            director = AnimalDirector(builder)
                            return director.construct()

            for text, _, pos in self.options:
                label = self.font.render(text, True, (255, 255, 255))
                self.screen.blit(label, pos)

            pygame.display.update()
            clock.tick(60)
