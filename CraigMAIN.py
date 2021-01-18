import pygame
from pygame import *
import sys
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1280
HEIGHT = 720
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


player_img = pygame.image.load('Craig.png')
wall_img = pygame.image.load("Wall.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (80, 68))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = 5
        if keystate[pygame.K_s]:
            self.speedy = -5
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
 ##          self.rect.up = HEIGHT

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = wall_img
        self.image = pygame.transform.scale(wall_img, (200, 38))
        self.rect = self.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

game_map =

# x location, y location, img width, img height, img file



# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
pygame.key.set_repeat(True)

all_sprites = pygame.sprite.Group()
player = Player()
walls = Walls()
all_sprites.add(player)
all_sprites.add(walls)

# Game loop
while True:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == K_w:
                player.rect.centery -= 5
            elif event.key == pygame.K_DOWN or event.key == K_s:
                player.rect.centery += 5
            elif event.key == pygame.K_LEFT or event.key == K_a:
                player.rect.left -= 5
            elif event.key == pygame.K_RIGHT or event.key == K_d:
                player.rect.right += 5

        # Moving sprites with arrow keys or WASD


    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()