import pygame
from settings import Color


class HitBox(pygame.sprite.Sprite):

    def __init__(self, game, player):

        super().__init__()
        self.player = player
        self.game = game
        self.add(self.game.all_sprites)
        self.image = pygame.Surface((self.player.feet.width, self.player.feet.height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.player.rect.midbottom

    def update(self):
        self.rect.midbottom = self.player.rect.midbottom


class Mob(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = self.game.picture.get_image()
        self.rect = self.image.get_rect()
        self.rect.midbottom((x, y))
