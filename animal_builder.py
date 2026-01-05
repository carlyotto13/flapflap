from animal1 import Animal
import pygame

class AnimalBuilder:
    def __init__(self):
        self.animal = Animal()

    def set_images(self):
        pass

    def set_position(self):
        self.animal.x = 230
        self.animal.y = 350

    def get_result(self):
        return self.animal


class FrogBuilder(AnimalBuilder):
    def set_images(self):
        self.animal.IMGS = [
            pygame.transform.scale2x(pygame.image.load("assets/animal/frog1.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/frog2.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/frog3.png"))
        ]


class HamsterBuilder(AnimalBuilder):
    def set_images(self):
        self.animal.IMGS = [
            pygame.transform.scale2x(pygame.image.load("assets/animal/hamster1.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/hamster2.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/hamster3.png"))
        ]


class PenguinBuilder(AnimalBuilder):
    def set_images(self):
        self.animal.IMGS = [
            pygame.transform.scale2x(pygame.image.load("assets/animal/penguin1.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/penguin2.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/penguin3.png"))
        ]

class DogBuilder(AnimalBuilder):
    def set_images(self):
        self.animal.IMGS = [
            pygame.transform.scale2x(pygame.image.load("assets/animal/dog0.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/dog1.png")),
            pygame.transform.scale2x(pygame.image.load("assets/animal/dog2.png"))
        ]
