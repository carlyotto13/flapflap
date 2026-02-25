
import pygame
from sys import exit
import random
from src.miu_settings import GAME_WIDTH, GAME_HEIGHT, FROG_START_X, FROG_START_Y, FROG_WIDTH, FROG_HEIGHT, GRAVITY, PIPE_WIDTH, PIPE_HEIGHT, PIPE_OPENING_SPACE, PIPE_SPEED
from src.miu_gameover_screen import run_game_over
from src.miu_highscore import update_highscore

def run_frog():
    pygame.init()
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Flap Flap Frog")
    clock = pygame.time.Clock()

    # Hintergrund
    background = pygame.image.load("assets/frog/frog_background.png")

    # Frosch
    frog_image = pygame.image.load("assets/frog/frog_01.png")
    frog_image = pygame.transform.scale(frog_image, (FROG_WIDTH, FROG_HEIGHT))
    frog_x, frog_y = FROG_START_X, FROG_START_Y

    class Frog(pygame.Rect):
        def __init__(self, img):
            super().__init__(frog_x, frog_y, FROG_WIDTH, FROG_HEIGHT)
            self.img = img

    frog = Frog(frog_image)

    # Pipes
    pipe_x = GAME_WIDTH
    pipe_y = 0
    top_pipe_image = pygame.image.load("assets/frog/frog_obstacle.png")
    top_pipe_image = pygame.transform.scale(top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
    bottom_pipe_image = pygame.transform.rotate(top_pipe_image, 180)

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
        random_pipe_y = pipe_y - PIPE_HEIGHT / 4 - random.random() * (PIPE_HEIGHT / 2)
        top = Pipe(top_pipe_image, GAME_WIDTH, random_pipe_y)
        bottom = Pipe(bottom_pipe_image, GAME_WIDTH, random_pipe_y + PIPE_HEIGHT + PIPE_OPENING_SPACE)
        pipes.extend([top, bottom])

    def move():
        nonlocal velocity_y, game_over, score
        velocity_y += GRAVITY
        frog.y += velocity_y
        frog.y = max(frog.y, 0)
        if frog.y > GAME_HEIGHT:
            game_over = True

        for pipe in pipes:
            pipe.x += velocity_x
            if not pipe.passed and frog.x > pipe.x + PIPE_WIDTH:
                score += 0.5
                pipe.passed = True
            if frog.colliderect(pipe):
                game_over = True

        while pipes and pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)

    def draw():
        window.blit(background, (0, 0))
        window.blit(frog.img, (frog.x, frog.y))
        for pipe in pipes:
            window.blit(pipe.img, pipe)

        font = pygame.font.SysFont("Comic Sans MS", 45)
        text = font.render(str(int(score)), True, (255, 255, 255))
        window.blit(text, (5, 0))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == CREATE_PIPE_EVENT and not game_over:
                create_pipes()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    velocity_y = -6
                    if game_over:
                        frog.y = FROG_START_Y
                        pipes.clear()
                        score = 0
                        game_over = False

        if not game_over:
            move()
            draw()
        else:
            update_highscore(score)
            # Game Over Screen starten und Rückgabe abfangen
            action, _ = run_game_over(score, last_animal="FROG")
            if action == "TRY_AGAIN":
                return run_frog()  # startet Frosch erneut
            elif action == "BACK_TO_MENU":
                return  # kehrt zum Selection Screen zurück

        pygame.display.update()
        clock.tick(60)
