import pygame

from settings import WIDTH, HEIGHT, FPS, Color

# Basic initializations

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Basic game loop

run = True

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(Color.BLUE)

    pygame.display.flip()  # Flip the display once you have drawn


pygame.quit()
