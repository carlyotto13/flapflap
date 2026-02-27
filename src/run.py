import pygame
from sys import exit
import random
from settings import SOUND_SETTINGS, GAME_WIDTH, GAME_HEIGHT, FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT, GRAVITY, JUMP_STRENGTH, PIPE_WIDTH, PIPE_HEIGHT, PIPE_OPENING_SPACE, PIPE_SPEED
from gameover_screen import run_game_over
import highscore
from animal import ANIMALS
#from selection_screen_updated import run_flappy

class Player:
    def __init__(self, image_path, config):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (FROG_WIDTH, FROG_HEIGHT))
        self.rect = pygame.Rect(FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT)
        self.velocity_y = 0
        self.alive = True

    def jump(self):
        self.velocity_y = JUMP_STRENGTH

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        self.rect.y = max(self.rect.y, 0)

        if self.rect.y > GAME_HEIGHT:
            self.alive = False

    def draw(self, window):
        window.blit(self.image, self.rect)

class Pipe:
    def __init__(self, image, x, y, pipe_type):
        self.image = image
        self.rect = pygame.Rect(x, y, PIPE_WIDTH, PIPE_HEIGHT)
        self.type = pipe_type
        self.passed = False

    def draw(self, window):
        window.blit(self.image, self.rect)


class PipeManager:
    def __init__(self, obstacle_image_path):
        self.obstacle_image = pygame.image.load(obstacle_image_path)
        self.obstacle_image = pygame.transform.scale(self.obstacle_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_image = pygame.transform.rotate(self.obstacle_image, 180)
        self.pipes = []

    def create_pipes(self):
        random_pipe_y = -PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        top = Pipe(self.obstacle_image, GAME_WIDTH, random_pipe_y, "top")
        bottom = Pipe(self.bottom_image, GAME_WIDTH,
        random_pipe_y + PIPE_HEIGHT + PIPE_OPENING_SPACE, "bottom")
        self.pipes.extend([top, bottom])

    def update(self):
        for pipe in self.pipes:
            pipe.rect.x += PIPE_SPEED

        # Entferne Pipes außerhalb des Bildschirms
        self.pipes = [p for p in self.pipes if p.rect.x > -PIPE_WIDTH]

    def check_collision(self, player):
        for pipe in self.pipes:
            if player.rect.colliderect(pipe.rect):
                return True
        return False


class GameState:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.paused = False

    def reset(self):
        self.score = 0
        self.game_over = False
        self.paused = False

    def increment_score(self, amount=1):
        self.score += amount


class SoundManager:
    def __init__(self):
        self.sounds = {'point': pygame.mixer.Sound("../assets/sounds/obstacle_sound.wav"),
                       'flap': pygame.mixer.Sound("../assets/sounds/flap_sound.wav"),
                       'gameover': pygame.mixer.Sound("../assets/sounds/gameover_sound.wav")}

        # Set volumes
        self.sounds['point'].set_volume(0.05)
        self.sounds['flap'].set_volume(0.3)
        self.sounds['gameover'].set_volume(0.1)

    def play(self, sound_name):
        if SOUND_SETTINGS["game"] and sound_name in self.sounds:
            self.sounds[sound_name].play()


class FlappyBirdGame:
    def __init__(self, animal_key):
        pygame.init()
        self.window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Flap Flap")
        self.clock = pygame.time.Clock()

        self.config = ANIMALS[animal_key]
        self.animal_key = animal_key

        # Initialize components
        self.sound_manager = SoundManager()
        self.game_state = GameState()
        self.background = pygame.image.load(self.config["background"])

        # Initialize player and pipes
        self.player = Player(self.config["player"], self.config)
        self.pipe_manager = PipeManager(self.config["obstacle"])

        # Timer für Pipe-Erstellung
        self.CREATE_PIPE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.CREATE_PIPE_EVENT, 1500)

        self.font = pygame.font.SysFont("Comic Sans MS", 45)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == self.CREATE_PIPE_EVENT and not self.game_state.game_over:
                self.pipe_manager.create_pipes()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    if not self.game_state.game_over:
                        self.player.jump()
                        self.sound_manager.play('flap')
                    else:
                        return "RESTART"

                if event.key == pygame.K_ESCAPE:
                    self.game_state.paused = not self.game_state.paused

        return "CONTINUE"

    def update_score(self):
        for pipe in self.pipe_manager.pipes:
            if not pipe.passed and self.player.rect.x > pipe.rect.x + PIPE_WIDTH:
                self.game_state.increment_score(0.5)
                pipe.passed = True
            if pipe.type == "top": # Nur einmal Sound pro Pipe-Paar
                self.sound_manager.play('point')

    def check_game_over(self):
        if not self.player.alive or self.pipe_manager.check_collision(self.player):
            if not self.game_state.game_over:
                self.sound_manager.play('gameover')
                self.game_state.game_over = True
                highscore.update_highscore(int(self.game_state.score))

    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.player.draw(self.window)

        for pipe in self.pipe_manager.pipes:
            pipe.draw(self.window)

        # Score anzeigen
        score_text = self.font.render(str(int(self.game_state.score)), True, (255, 255, 255))
        self.window.blit(score_text, (5, 0))

        if self.game_state.paused:
            self.draw_pause_screen()

    def draw_pause_screen(self):
        s = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.window.blit(s, (0, 0))

        pause_text = self.font.render("PAUSED", True, (255, 255, 255))
        text_rect = pause_text.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))
        self.window.blit(pause_text, text_rect)

    def run(self):
        while True:
            action = self.handle_events()

            if action == "QUIT":
                pygame.quit()
                exit()
            elif action == "RESTART":
                self.game_state.reset()
                self.player = Player(self.config["player"], self.config)
                self.pipe_manager.pipes.clear()
                continue

            if not self.game_state.game_over and not self.game_state.paused:
                self.player.update()
                self.pipe_manager.update()
                self.update_score()
                self.check_game_over()

            self.draw()

            if self.game_state.game_over:
                return self.game_state.score
                #action, _ = run_game_over(int(self.game_state.score), last_animal=self.animal_key)
                #if action == "TRY_AGAIN":
                    #return run_flappy(self.animal_key)
                #elif action == "BACK_TO_MENU":
                    #return

            pygame.display.flip()
            self.clock.tick(60)

def run_flappy(animal_key):
    game = FlappyBirdGame(animal_key)
    return game.run()