import random

import pygame

from settings import WIDTH, HEIGHT, FPS, Color, PLATFORM_LIST, FONT_NAME
from sprites import Player, Platforms


class Game:

    def __init__(self):
        self.running = True
        self.playing = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font(FONT_NAME)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Test')

    def new(self):
        self.score = 0
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player.Player(self)

        for platform in PLATFORM_LIST:
            p = Platforms.BasePlatform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.all_sprites.add(self.player)

        self._run()

    def _run(self):
        # Game loop

        while self.playing:

            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()

    def _update(self):
        # Game loop - Update
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)
                if platform.rect.top >= HEIGHT:
                    platform.kill()
                    self.score += 10

        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platforms) == 0:
            self.playing = False

        while len(self.platforms) < 6:
            p = Platforms.BasePlatform(random.randrange(0, WIDTH - random.randrange(60, 100)),
                                       0,
                                       random.randrange(50, 100),
                                       20
                                       )
            self.platforms.add(p)
            self.all_sprites.add(p)

    def _events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def _draw(self):

        self.screen.fill(Color.BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, Color.WHITE, WIDTH - 25, 15)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
