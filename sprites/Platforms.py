
import pygame

from settings import Color


platforms = {'big_grass': (0, 288, 380, 94),
             'small_grass': (213, 1662, 210, 100)}


class BasePlatform(pygame.sprite.Sprite):

    __slots__ = ('x', 'y', 'game', 'type')

    def __init__(self, x, y, game, _type=None):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        if _type is None:
            self.image = self.game.spritesheet.get_image(*platforms['big_grass'])
        else:
            self.image = self.game.spritesheet.get_image(*platforms[_type])

        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
