# Game settings

WIDTH = 360
HEIGHT = 480
FPS = 60

# PLayer settings

PLAYER_ACC = 0.5
WORLD_ACC = 0.5
PLAYER_FRICTION = -0.12

# Platform list

PLATFORM_LIST = [
    (0, HEIGHT - 40, WIDTH, 40),
    (WIDTH / 2, 300, 30, 10)
]


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
