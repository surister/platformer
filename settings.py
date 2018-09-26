# Game settings

WIDTH = 360
HEIGHT = 480
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = 'assets/spritesheet_jumper.png'
# PLayer settings

PLAYER_ACC = 0.5
WORLD_ACC = 0.5
PLAYER_FRICTION = -0.12

# Platform list

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (0, 155, 155)
    LIGHT_PURPLE = (122, 66, 221)
