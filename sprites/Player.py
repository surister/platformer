import pygame
from settings import Color, WIDTH, HEIGHT, PLAYER_ACC, WORLD_ACC, PLAYER_FRICTION


def vector(*args):
    return pygame.math.Vector2(args)


class Player(pygame.sprite.Sprite):

    __slots__ = ['game']

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)

        self.game = game

        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0

        self.load_images()
        self.image = self.standing_frames[0]

        self.rect = self.image.get_rect()

        self.pos = vector(WIDTH / 2, HEIGHT / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, WORLD_ACC)

    def load_images(self):

        self.standing_frames = (self.game.spritesheet.get_image(x=614, y=1063, width=120, height=191),
                                self.game.spritesheet.get_image(x=690, y=406, width=120, height=201))

        for st_frame, wk_frame in self.standing_frames, self.standing_frames:
            st_frame.set_colorkey(Color.BLACK)
            wk_frame.set_colorkey(Color.BLACK)

        self.walking_frames_r = (self.game.spritesheet.get_image(x=678, y=860, width=120, height=201),
                               self.game.spritesheet.get_image(x=692, y=1458, width=120, height=207))

        self.walk_frames_l = [pygame.transform.flip(frame, True, False) for frame in self.walking_frames_r]

        self.jumping_frame = [self.game.spritesheet.get_image(x=382, y=763, width=150, height=181)]

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -15

    def update(self):
        self.animate()

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

    def animate(self):
        now = pygame.time.get_ticks()

        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now

                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)

                self.image = self.standing_frames[self.current_frame]

                bottom = self.rect.bottom
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom