import pygame
from settings import Color, WIDTH, HEIGHT, PLAYER_ACC, WORLD_ACC, PLAYER_FRICTION, PLAYER_JUMP


def vector(*args):
    return pygame.math.Vector2(args)


class Player(pygame.sprite.Sprite):

    __slots__ = ['game']

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.add(self.game.all_sprites)

        self.can_move = True
        self.walking = self.jumping = self.down = False

        self.current_frame = 0
        self.last_update = 0

        self.load_images()
        self.image = self.standing_frames[0]

        self.rect = self.image.get_rect()
        self.feet = self.rect.copy().inflate(-15, -30)

        self.pos = vector(30, HEIGHT - 30)
        self.vel = vector(0, 0)
        self.acc = vector(0, WORLD_ACC)

    def load_images(self):

        self.standing_frames = (self.game.spritesheet.get_image(x=614, y=1063, width=120, height=191),
                                self.game.spritesheet.get_image(x=690, y=406, width=120, height=201))

        self.walking_frames_r = (self.game.spritesheet.get_image(x=678, y=860, width=120, height=201),
                                 self.game.spritesheet.get_image(x=692, y=1458, width=120, height=207))

        self.walking_frames_l = [pygame.transform.flip(frame, True, False)
                                 for frame in self.walking_frames_r]

        self.jumping_frame = self.game.spritesheet.get_image(x=382, y=763, width=150, height=181)

        self.down_frame = self.game.spritesheet.get_image(x=382, y=763, width=150, height=181)

    def jump(self):
        self.rect.x += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits and not self.jumping:
            #self.game.jump_sound.play()
            self.jumping = True
            self.vel.y = PLAYER_JUMP

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -4

    def update(self):
        self.animate()
        self.acc.x = 0

        #  MOVEMENT STUFF
        self.keys = pygame.key.get_pressed()

        if self.can_move:
            if self.keys[pygame.K_LEFT]:
                self.acc.x = -PLAYER_ACC
            if self.keys[pygame.K_RIGHT]:
                self.acc.x = PLAYER_ACC
            if self.keys[pygame.K_SPACE]:
                if not self.jumping:
                    pass
                    #  self.game.jump_sound.play()
                self.jump()

        if self.keys[pygame.K_DOWN]:
            self.acc.y = 1.4
            self.down = True
            self.can_move = False
        else:
            self.acc.y = WORLD_ACC
            self.down = False
            self.can_move = True

        #  FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #  MOTION

        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + WORLD_ACC * self.acc

        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        self.rect.midbottom = self.pos

    def _stick_player(self):

        """We redefine the players position in every animation so it sticks regardless of the
        new players frame"""

        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom

    def animate(self):
        now = pygame.time.get_ticks()

        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking and not self.jumping:
            if now - self.last_update > 200:
                self.last_update = now

                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_r)
                if self.vel.x > 0:
                    self.image = self.walking_frames_r[self.current_frame]
                else:
                    self.image = self.walking_frames_l[self.current_frame]

                self._stick_player()

        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now

                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)

                self.image = self.standing_frames[self.current_frame]

                self._stick_player()

        if self.jumping:

            self.image = self.jumping_frame

            self._stick_player()

        if self.down:
            self.image = self.down_frame
            self._stick_player()
