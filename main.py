import pygame
from sprites import Game


if __name__ == '__main__':

    g = Game.Game()

    while g.running:
        g.new()

    pygame.quit()
