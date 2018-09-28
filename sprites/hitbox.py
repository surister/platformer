import pygame
from settings import Color


class HitBox(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player

        self.image = pygame.Surface((self.player.feet.width, self.player.feet.height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.player.rect.midbottom
        self.image.set_colorkey(Color.BLACK)

    def update(self):
        self.rect.midbottom = self.player.rect.midbottom


class Mob(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = self.game.picture.get_image()
        self.rect = self.image.get_rect()
        self.rect.midbottom((x, y))
