import pygame
from sprites import Game


if __name__ == '__main__':

    g = Game.Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()
pygame.quit()
