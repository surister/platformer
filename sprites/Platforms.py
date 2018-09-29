from random import randrange
import pygame

from settings import Color, POW_S
from sprites.powerups import PowerUp

platforms = {1: (0, 288, 380, 94),
             2: (213, 1662, 210, 100)}


class BasePlatform(pygame.sprite.Sprite):

    __slots__ = ('x', 'y', 'game', '_type')

    def __init__(self, x, y, game, _type=None):

        super().__init__()
        self.game = game
        self.add(self.game.all_sprites, self.game.platforms)

        self.image = self.game.spritesheet.get_image(*platforms[_type])

        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        if randrange(100) < POW_S:
            PowerUp(self.game, self)
