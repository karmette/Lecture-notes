# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 720
HEIGHT = 720
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# outside game loop
class Cat(pygame.sprite.Sprite):
    def __init__(self):
        # super refers to the parent (pygame.sprite.Sprite)
        # we need to do this so pygame recognizes it
        # and we can do special pygame stuff with it
        super().__init__()
        
        self.image = pygame.image.load("cat.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = 100
        self.rect.y = 100
        

# Game loop
cat = Cat()
running = True
while running:
    # Clock tick
    clock.tick(FPS)

    # Quit game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        cat.rect.y -=5
    

    # inside game loop
    screen.fill(color=(100,0,255)) # draw the background first!
    
    screen.blit(cat.image, cat.rect)

    pygame.display.flip()
pygame.quit()