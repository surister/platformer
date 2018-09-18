import pygame
from settings import WIDTH, HEIGHT, FPS, Color


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
        self._run()

    def _run(self):
        # Game loop

        while self.playing:

            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()
        pass

    def _update(self):
        # Game loop - Update
        self.all_sprites.update()

    def _events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            self.running = False
        pass

    def _draw(self):

        self.screen.fill(Color.BLACK)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_go_screen()
while g.running:
    g.new()

pygame.quit()
