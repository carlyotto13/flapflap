# world
#import pygame
#from obstacle import Obstacle
#from animal import Animal
#from game import GameIndicator
#from settings import W, H, obstacle_size, obstacle_gap, obstacle_pair_sizes
#import random

#class World:
    #def __init__(self, screen):
        #self.screen = screen
        #self.world_shift = 0
        #self.current_x = 0
        #self.gravity = 0.5
        #self.current_obstacle = None
        #self.obstacles = pygame.sprite.Group()
        #self.player = pygame.sprite.GroupSingle()
        #self._generate_world()
        #self.playing = False
        #self.game_over = False
        #self.passed = True
        #self.game = GameIndicator(screen)

    # adds obstacle once the last obstacle added reached the desired obstacle horizontal spaces
    #def _add_obstacle(self):
        #obstacle_pair_size = random.choice(obstacle_pair_sizes)
        #top_obstacle_height, bottom_obstacle_height = obstacle_pair_size[0] * obstacle_size, obstacle_pair_size[1] * obstacle_size
        #obstacle_top = Obstacle((W, 0 - (bottom_obstacle_height + obstacle_gap)), obstacle_size, H, True)
        #obstacle_bottom = Obstacle((W, top_obstacle_height + obstacle_gap), obstacle_size, H, False)
        #self.obstacles.add(obstacle_top)
        #self.obstacles.add(obstacle_bottom)
        #self.current_obstacle = obstacle_top

    # creates the player and the obstacle
    #def _generate_world(self):
        #self._add_obstacle()
        #animal = Animal((W//2 - obstacle_size, H//2 - obstacle_size), 30)
        #self.player.add(animal)

    # for moving background/obstacle
    #def _scroll_x(self):
        #if self.playing:
            #self.world_shift = -6
        #else:
            #self.world_shift = 0

    # add gravity to animal for falling
    #def _apply_gravity(self, player):
        #if self.playing or self.game_over:
            #player.direction.y += self.gravity
            #player.rect.y += player.direction.y

    # handles scoring and collision
    #def _handle_collisions(self):
        #animal = self.player.sprite
        # for collision checking
        #if pygame.sprite.groupcollide(self.player, self.obstacles, False, False) or animal.rect.bottom >= H or animal.rect.top <= 0:
            #self.playing = False
            #self.game_over = True
        #else:
            # if player pass through the pipe gaps
            #animal = self.player.sprite
            #if animal.rect.x >= self.current_obstacle.rect.centerx:
                #animal.score += 1
                #self.passed = True

    # updates the animals overall state
    #def update(self, player_event=None):
        # new obstacle adder
        #if self.current_obstacle.rect.centerx <= (W // 2) - obstacle_size:
            #self._add_obstacle()
        # updates, draws obstacles
        #self.obstacles.update(self.world_shift)
        #self.obstacles.draw(self.screen)
        # applying game physics
        #self._apply_gravity(self.player.sprite)
        #self._scroll_x()
        #self._handle_collisions()
        # configuring player actions
        #if player_event == "jump" and not self.game_over:
            #player_event = True
        #elif player_event == "restart":
            #self.game_over = False
            #self.obstacles.empty()
            #self.player.empty()
            #self.player.score = 0
            #self._generate_world()
        #else:
            #player_event = False
        #if not self.playing:
            #self.game.instructions()
        # updates, draws obstacles
        #self.player.update(player_event)
        #self.player.draw(self.screen)
        #self.game.show_score(self.player.sprite.score)

import pygame
from obstacle import Obstacle
from animal import Animal
from game import GameIndicator
from settings import W, H, obstacle_size, obstacle_gap, obstacle_pair_sizes
import random

class World:
    def __init__(self, screen):
        self.screen = screen
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.current_obstacle = None
        self.obstacles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self._generate_world()
        self.playing = False
        self.game_over = False
        self.passed = False
        self.game = GameIndicator(screen)

    # adds obstacle once the last obstacle added reached the desired obstacle horizontal spaces
    def _add_obstacle(self):
        obstacle_pair_size = random.choice(obstacle_pair_sizes)
        top_obstacle_height, bottom_obstacle_height = obstacle_pair_size[0] * obstacle_size, obstacle_pair_size[1] * obstacle_size
        obstacle_top = Obstacle((W, 0 - (bottom_obstacle_height + obstacle_gap)), obstacle_size, H, True)
        obstacle_bottom = Obstacle((W, top_obstacle_height + obstacle_gap), obstacle_size, H, False)
        self.obstacles.add(obstacle_top)
        self.obstacles.add(obstacle_bottom)
        self.current_obstacle = obstacle_top
        self.passed = False  # Reset passed flag for new obstacle

    # creates the player and the obstacle
    def _generate_world(self):
        self._add_obstacle()
        animal = Animal((W//4, H//2 - 15), 30)  # Better positioning
        self.player.add(animal)

    # for moving background/obstacle
    def _scroll_x(self):
        if self.playing:
            self.world_shift = -6
        else:
            self.world_shift = 0

    # add gravity to animal for falling
    def _apply_gravity(self, player):
        if self.playing or self.game_over:
            player.direction.y += self.gravity
            player.rect.y += player.direction.y

    # handles scoring and collision
    def _handle_collisions(self):
        animal = self.player.sprite
        # for collision checking
        if pygame.sprite.groupcollide(self.player, self.obstacles, False, False) or animal.rect.bottom >= H or animal.rect.top <= 0:
            self.playing = False
            self.game_over = True
        else:
            # if player pass through the pipe gaps
            if not self.passed and animal.rect.x >= self.current_obstacle.rect.centerx:
                animal.score += 1
                self.passed = True

    # updates the animals overall state
    def update(self, player_event=None):
        # new obstacle adder
        if self.current_obstacle.rect.centerx <= (W // 2) - obstacle_size:
            self._add_obstacle()
        # updates, draws obstacles
        self.obstacles.update(self.world_shift)
        self.obstacles.draw(self.screen)
        # applying game physics
        self._apply_gravity(self.player.sprite)
        self._scroll_x()
        self._handle_collisions()
        # configuring player actions
        if player_event == "jump" and not self.game_over:
            player_event = True
        elif player_event == "restart":
            self.game_over = False
            self.playing = False
            self.obstacles.empty()
            self.player.empty()
            self._generate_world()
        else:
            player_event = False
        if not self.playing:
            self.game.instructions()
        # updates, draws player
        self.player.update(player_event)
        self.player.draw(self.screen)
        self.game.show_score(self.player.sprite.score)