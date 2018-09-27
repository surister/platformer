import random

from os import path

import pygame

from settings import WIDTH, HEIGHT, FPS, Color, PLATFORM_LIST, FONT_NAME, HS_FILE, SPRITESHEET
from sprites import Player, Platforms, art


class Game:

    def __init__(self):
        #  Basic flow control
        self.running = True
        self.playing = True

        #  Basic pygame vars
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font(FONT_NAME)

        # Basic py game initializations
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('SUPER JUEGO OMG')

        # Paths
        self.path = path.dirname(__file__)
        self.highscore_path = path.join(self.path, HS_FILE)
        self.spritesheet_path = path.join(self.path, SPRITESHEET)

        self._load_data()

    def _load_data(self):
        with open(self.highscore_path, 'r') as f:
            try:
                self.highscore = int(f.read())
            except Exception as e:
                print(e)
                self.highscore = 0

        self.spritesheet = art.Sheet(self.spritesheet_path)

    def new(self):
        self.score = 0
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player.Player(self)

        for platform in PLATFORM_LIST:

            p = Platforms.BasePlatform(*platform, self, 'small_grass')
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.all_sprites.add(self.player)

        self._run()

    def _run(self):

        while self.playing:

            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()

    def _update(self):

        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for platform in self.platforms:
                platform.rect.y += max(abs(self.player.vel.y), 2)
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

        # while len(self.platforms) < 4:
        #     p = Platforms.BasePlatform(random.randrange(0, WIDTH - random.randrange(60, 100)), 0, self)
        #     self.platforms.add(p)
        #     self.all_sprites.add(p)

    def _events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def _draw(self):

        self.screen.fill(Color.LIGHT_BLUE)
        self.all_sprites.draw(self.screen)
        self._draw_text(str(self.score), 22, Color.WHITE, WIDTH - 25, 15)
        self.screen.blit(self.player.image, self.player.rect) # makes the player to be in front of the platform
        pygame.display.flip()

    def show_start_screen(self):

        self.screen.fill(Color.LIGHT_PURPLE)
        self._draw_text('super juego increible', 25, Color.WHITE, WIDTH / 2, HEIGHT / 4)
        self._draw_text('Arrows to move, space to jump', 22, Color.RED, WIDTH / 2, HEIGHT * 3 / 4)
        self._draw_text(f'Higher score: {self.highscore}', 10, Color.GREEN, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()
        self._wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return

        self.screen.fill(Color.BLUE)
        self._draw_text('game over', 48, Color.RED, WIDTH / 2, HEIGHT / 4)
        self._draw_text('PUTO NOOB K HACES PERDIENDO', 20, Color.RED, WIDTH / 2, HEIGHT * 3 / 4)
        self._draw_text(f'You score score: {self.score}', 10, Color.GREEN, WIDTH / 2, HEIGHT / 2)

        pygame.display.flip()
        self._save_score()

        self._wait_for_key()

    def _save_score(self):
        if self.score > self.highscore:
            with open(f'{self.path}/{HS_FILE}', 'w') as f:
                f.write(str(self.score))

    def _draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def _wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
