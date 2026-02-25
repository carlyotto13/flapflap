import pygame
from sys import exit
import random

pygame.init()

### BACKGROUND
# size
GAME_WIDTH = 360
GAME_HEIGHT = 640
# get image
background = pygame.image.load("../assets/frog/frog_background.png")

### FROG
# set starting position
frog_x = GAME_WIDTH / 8
frog_y = GAME_HEIGHT / 2
# size
frog_width = 55
frog_height = 64
# get image
frog_image = pygame.image.load("../assets/frog/frog_01.png")
# changing the size of the image
frog_image = pygame.transform.scale(frog_image, (frog_width, frog_height))

### Obstacle
# set starting position
pipe_x = GAME_WIDTH
pipe_y = 0
# size
pipe_width = 50
pipe_height = 512
# get image
top_pipe_image = pygame.image.load("../assets/frog/frog_obstacle.png")
# changing size
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
# bottom pipe = top pipe rotated by 180°
bottom_pipe_image = pygame.transform.rotate(top_pipe_image, 180)

# pipe class
class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, pipe_x, pipe_y, pipe_width, pipe_height)
        self.img = img
        self.passed = False

# frog class
class Frog (pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, frog_x, frog_y, frog_width, frog_height)
        self.img = img

# game logic
frog = Frog(frog_image)
pipes = []
velocity_x = -2 # move pipes to the left speed
velocity_y = 0 # move frog up/down speed
gravity = 0.4
score = 0 # starting score
game_over = False

# draw function
def draw():
    window.blit(background, (0, 0))
    window.blit(frog.img, (frog.x, frog.y))

    for pipe in pipes:
        window.blit(pipe.img, pipe)

    text_str = str(int(score))
    if game_over:
        text_str = "GAME OVER:" + text_str

    text_font = pygame.font.SysFont("Comic Sans MS", 45)
    text_render = text_font.render(text_str, True, "white")
    window.blit(text_render, (5, 0))

def move():
    global velocity_y, score, game_over
    velocity_y += gravity
    frog.y += velocity_y
    frog.y = max(frog.y, 0)

    if frog.y > GAME_HEIGHT:
        game_over = True
        return

    for pipe in pipes:
        pipe.x += velocity_x

        if not pipe.passed and frog.x > pipe.x + pipe_width:
            score += 0.5 # because there are 2 pipes
            pipe.passed = True

        if frog.colliderect(pipe):
            game_over = True
            return

    while len(pipes) > 0 and pipes[0].x  < - pipe_width:
        pipes.pop(0) # removes first element from the list


def create_pipes():
    random_pipe_y = pipe_y - pipe_height / 4 - random.random() * (pipe_height / 2)
    opening_space = GAME_HEIGHT / 4

    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image)
    bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space
    pipes.append(bottom_pipe)

    print(len(pipes))


# setup window
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Flap Flap")
clock = pygame.time.Clock()

create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500) # marks every 1.5 seconds

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over:
            create_pipes()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                velocity_y = -6

                #reset game
                if game_over:
                    frog.y = frog_y
                    pipes.clear()
                    score = 0
                    game_over = False

    if not game_over:
        move()
        draw()
        pygame.display.update()
        clock.tick(60)