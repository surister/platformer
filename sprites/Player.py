import pygame
from settings import Color, WIDTH, HEIGHT, PLAYER_ACC, WORLD_ACC, PLAYER_FRICTION


def vector(*args):
    return pygame.math.Vector2(args)


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.image = pygame.Surface((30, 40))
        self.image.fill(Color.GREEN)

        self.rect = self.image.get_rect()

        self.pos = vector(WIDTH / 2, HEIGHT / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, WORLD_ACC)

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15

    def update(self):

        self.acc.x = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pygame.K_SPACE]:
            self.jump()
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
