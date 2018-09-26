import pygame


class Sheet:

    def __init__(self, fn):

        self.spritesheet = pygame.image.load(fn).convert()
        self.ratio = 3

    def get_image(self, x, y, width, height):

        #  grab an image out of larger spritesheet
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // self.ratio, height // self.ratio))
        return image
