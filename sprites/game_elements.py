import pygame

from random import choice, randrange

from settings import POW_S, Color, WIDTH, HEIGHT


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


class Cloud(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.add(self.game.clouds, self.game.all_sprites)

        # We could just avoid this function call but let's stick with the design pattern
        self.image = self.game.spritesheet.get_image(0, 1152, 260, 134)

        self.rect = self.image.get_rect()
        self.rect.x = randrange(WIDTH - self.rect.width)
        self.rect.y = randrange(-500, -50)
        self._load_images()

    def _load_images(self):

        scalerino = randrange(50, 100) / 100
        self.randomized_sprite = pygame.transform.scale(self.image, (int(self.rect.width * scalerino),
                                                                     int(self.rect.height * scalerino)))
        self.image = self.randomized_sprite

    def update(self):
        if self.rect.top > HEIGHT * 2:
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

    def __init__(self, game,):
        pygame.sprite.Sprite.__init__(self)
        self.add(game.all_sprites, game.mobs)
        self.game = game

        self._load_images()

        self.image = self.flying_frame[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100, WIDTH + 100])

        self.vx = randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.vx *= -1

        self.rect.y = randrange(HEIGHT / 2)

        self.vy = 0
        self.dy = 0.5

        self.current_frame = 0
        self.last_update = 0

    def update(self):

        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center

        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y += self.vy

        if self.rect.left > WIDTH + 100 or self.rect.right < -100:
            self.kill()

        self._animate()
        self.mask = pygame.mask.from_surface(self.image)

    def _load_images(self):
        self.flying_frame = [
            self.game.spritesheet.get_image(382, 635, 174, 126),
            self.game.spritesheet.get_image(0, 1879, 206, 107),
            self.game.spritesheet.get_image(0, 1559, 216, 101),
            self.game.spritesheet.get_image(0, 1456, 216, 101),
            self.game.spritesheet.get_image(382, 510, 182, 123)
            ]

    def _animate(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > 100:
            self.last_update = now

            self.current_frame = (self.current_frame + 1) % len(self.flying_frame)
            self.image = self.flying_frame[self.current_frame]

