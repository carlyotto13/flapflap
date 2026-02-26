# Bibs
import pygame
import sys
import random

pygame.init()

### BACKGROUND
# size
GAME_WIDTH = 360
GAME_HEIGHT = 640
# get image
background = pygame.image.load('../assets/starting_screen/start_background.png')

### CLOUD
cloud_x = GAME_WIDTH
cloud_y = GAME_HEIGHT / 2
# size
cloud_width = 209
cloud_height = 120
# get image
cloud_image = pygame.image.load('../assets/starting_screen/start_obstacle.png')
# changing size
cloud_image = pygame.transform.scale(cloud_image, (cloud_width, cloud_height))

### choosing blocks
block = pygame.image.load('../assets/starting_screen/start_block.png')
#sizw
block_width = 183
block_height = 72
block = pygame.transform.scale(block, (block_width, block_height))


### TEXTFIELDS
font = pygame.font.SysFont("Comic Sans MS", 30)

start_y = GAME_HEIGHT * 2 / 5
spacing = 90   # Abstand zwischen den Blöcken

blocks = []
labels = ["FROG", "HAMSTER", "PENGUIN", "DOG"]

for i in range(4):
    x = (GAME_WIDTH - block_width) / 2   # horizontal zentriert
    y = start_y + i * spacing
    rect = pygame.Rect(x, y, block_width, block_height)
    blocks.append((rect, labels[i]))

# game logic
velocity_x = -2
clouds = []

### CLASS
# cloud class
class Cloud(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, cloud_x, cloud_y, cloud_width, cloud_height)
        self.img = img
        self.passed = False


### FUNCTION
def draw():
    window.blit(background, (0, 0))

    for cloud in clouds:
        window.blit(cloud.img, cloud)

    for rect, text in blocks:
        window.blit(block, rect)

        label = font.render(text, True, (255, 255, 255))
        label_rect = label.get_rect(center=rect.center)  # Text mittig im Block
        window.blit(label, label_rect)

def move():
    for cloud in clouds:
        cloud.x += velocity_x

    while len(clouds) > 0 and clouds[0].x  < - cloud_width:
        clouds.pop(0) # removes first element from the list

def create_clouds():
    random_cloud_y = random.uniform(GAME_HEIGHT / 4,GAME_HEIGHT * 3 / 4)

    cloud = Cloud(cloud_image)
    cloud.y = random_cloud_y
    clouds.append(cloud)

    print(len(clouds))

# setup window
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Flap Flap")
clock = pygame.time.Clock()
create_clouds_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_clouds_timer, 3000) # marks every 1.5 seconds

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_clouds_timer:
            create_clouds()

    move()
    draw()
    pygame.display.update()
    clock.tick(60)

