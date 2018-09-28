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

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.picture = pygame.image.load('/home/surister/pygame/sprites/assets/leon.png').convert()
        self.image = pygame.Surface((150, 150))
        self.image.blit(self.picture, (0, 0))
        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (230, 175)