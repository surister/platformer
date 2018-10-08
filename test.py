import pygame as pg


class Game:

    def __init__(self):
        self.running = True

        self.screen = pg.display.set_mode((600, 500))
        self.screen.fill((0, 155, 155))
        self.clock = pg.time.Clock()
        self.font = pg.font.match_font('arial')

        pg.init()

        self.all_sprites = pg.sprite.Group()

        self.test = test(self, (300, 200), 100, 15, (255, 255, 255))
        self.test_2 = test(self, (275, 200), 75, 15, (255, 2, 0), 1)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def draw(self):
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def update(self):
        self.all_sprites.update()


class test(pg.sprite.Sprite):

    def __init__(self, game, cords, width, height, color, opt=None):
        super().__init__()
        self.game = game
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = cords
        self.add(self.game.all_sprites)
        self.opt = opt

    def update(self):
        self.key = pg.key.get_pressed()
        print(self.rect.width)
        if self.key[pg.K_LEFT]:
            print(1)
            if self.opt == 1:
                self.rect.width -= 30
        if self.key[pg.K_RIGHT]:
            print(2)
            if self.opt == 1:
                self.rect.width += 30

a = Game()
a.run()

