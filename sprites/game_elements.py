import pygame

from random import choice, randrange

from settings import POW_S, Color


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
        self.current_frame = 0

    def update(self):
        self.rect.bottom = self.platform.rect.top - 5
        if not self.game.platforms.has(self.platform):
            self.kill()


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


class Mob(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.add(game.all_sprites, game.mobs)
        self.game = game

        self.image = self.game.picture.get_image()
        self.rect = self.image.get_rect()
        self.rect.midbottom((x, y))

    def update(self):
        pass

    def _load_images(self):
        self.flying_frame = [
            self.game.spritesheet.get_image(382, 635, 174, 126),
            self.game.spritesheet.get_image(0, 1879, 206, 107),
            self.game.spritesheet.get_image(0, 1559, 216, 101),
            self.game.spritesheet.get_image(0, 1456, 216, 101),
            self.game.spritesheet.get_image(382, 510, 182, 123)
            ]

