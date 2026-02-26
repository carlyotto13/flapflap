import pygame
from sys import exit
import random
from miu_settings import SOUND_SETTINGS, GAME_WIDTH, GAME_HEIGHT, FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT, GRAVITY, JUMP_STRENGTH, PIPE_WIDTH, PIPE_HEIGHT, PIPE_OPENING_SPACE, PIPE_SPEED
from miu_gameover_screen import run_game_over
import miu_highscore
from miu_animal import ANIMALS



def run_flappy(animal_key):

    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Flap Flap")
    clock = pygame.time.Clock()

    config = ANIMALS[animal_key]

    point_sound = pygame.mixer.Sound("../assets/sounds/obstacle_sound.wav")
    point_sound.set_volume(0.05)

    flap_sound = pygame.mixer.Sound("../assets/sounds/flap_sound.wav")
    flap_sound.set_volume(0.3)

    gameover_sound = pygame.mixer.Sound("../assets/sounds/gameover_sound.wav")
    gameover_sound.set_volume(0.1)



    # Hintergrund
    background = pygame.image.load(config["background"])

    # Spieler
    player_image = pygame.image.load(config["player"])
    player_image = pygame.transform.scale(player_image, (FROG_WIDTH, FROG_HEIGHT))

    class Player(pygame.Rect):
        def __init__(self, img):
            super().__init__(FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT)
            self.img = img

    player = Player(player_image)

    # Pipes / Hindernisse
    obstacle_image = pygame.image.load(config["obstacle"])
    obstacle_image = pygame.transform.scale(obstacle_image, (PIPE_WIDTH, PIPE_HEIGHT))
    bottom_image = pygame.transform.rotate(obstacle_image, 180)

    class Pipe(pygame.Rect):
        def __init__(self, img, x, y):
            super().__init__(x, y, PIPE_WIDTH, PIPE_HEIGHT)
            self.img = img
            self.passed = False

    pipes = []
    velocity_x = PIPE_SPEED
    velocity_y = 0
    score = 0
    game_over = False

    CREATE_PIPE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATE_PIPE_EVENT, 1500)

    def create_pipes():
        random_pipe_y = -PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        top = Pipe(obstacle_image, GAME_WIDTH, random_pipe_y)
        bottom = Pipe(bottom_image, GAME_WIDTH, random_pipe_y + PIPE_HEIGHT + PIPE_OPENING_SPACE)
        pipes.extend([top, bottom])

    def move():
        nonlocal velocity_y, game_over, score
        velocity_y += GRAVITY
        player.y += velocity_y
        player.y = max(player.y, 0)

        if player.y > GAME_HEIGHT:
            if SOUND_SETTINGS["game"]:
                gameover_sound.play()
            game_over = True


        for pipe in pipes:
            pipe.x += velocity_x

            if not pipe.passed and player.x > pipe.x + PIPE_WIDTH:
                score += 0.5
                pipe.passed = True
                if SOUND_SETTINGS["game"]:
                    point_sound.play()

            if player.colliderect(pipe):
                if SOUND_SETTINGS["game"]:
                    gameover_sound.play()
                game_over = True

        while pipes and pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)

    def draw():
        window.blit(background, (0, 0))
        window.blit(player.img, (player.x, player.y))

        for pipe in pipes:
            window.blit(pipe.img, pipe)

        font = pygame.font.SysFont("Comic Sans MS", 45)
        text = font.render(str(int(score)), True, (255, 255, 255))
        window.blit(text, (5, 0))

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == CREATE_PIPE_EVENT and not game_over:
                create_pipes()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    velocity_y = JUMP_STRENGTH
                    if SOUND_SETTINGS["game"]:
                        flap_sound.play()

                    if game_over:
                        player.y = FROG_START_Y
                        pipes.clear()
                        score = 0
                        game_over = False

        if not game_over:
            move()
            draw()
        else:
            miu_highscore.update_highscore(score)
            action, _ = run_game_over(score, last_animal=animal_key)

            if action == "TRY_AGAIN":
                return run_flappy(animal_key)

            elif action == "BACK_TO_MENU":
                return

        pygame.display.update()
        clock.tick(60)