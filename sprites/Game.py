import pygame
from settings import WIDTH, HEIGHT, FPS, Color, PLATFORM_LIST
from sprites import Player, Platforms


class Game:

    def __init__(self):
        self.running = True
        self.playing = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Test')

    def new(self):
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

    def _events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            self.running = False

    def _draw(self):

        self.screen.fill(Color.BLACK)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
