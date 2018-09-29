
import pygame
from random import choice, randint


class PowerUp(pygame.sprite.Sprite):

    __slots__ = ('x', 'y', 'game', 'type')

    def __init__(self, game, plat):

        super().__init__()

        self.platform = plat
        self.game = game
        self.add(self.game.powerups, self.game.all_sprites)

        self.type = choice(['boost'])

        self.image = self.game.spritesheet.get_image(852, 1089, 65, 77)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.platform.rect.centerx
        self.rect.bottom = self.platform.rect.top - 5

        self.last_update = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 200:
                self.last_update = now
                self.rect.bottom = self.platform.rect.top - randint(3, 6)
        if not self.game.platforms.has(self.platform):
            self.kill()
