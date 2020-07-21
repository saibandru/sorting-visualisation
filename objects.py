import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
font = pygame.font.SysFont("Helvetica", 35)
running = True
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False


# noinspection PyAttributeOutsideInit
class Button:
    def __init__(self, screen, pos_x, pos_y, default, hover, height=286, width=73):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.default = default
        self.hover = hover
        self.screen = screen

    def mouse_hover(self):
        x, y = pygame.mouse.get_pos()
        if x in range(self.pos_x, self.pos_x + self.height) and y in range(self.pos_y, self.pos_y + self.width):
            self.img = pygame.image.load(self.hover)
            self.screen.blit(self.img, (self.pos_x, self.pos_y))
            return True
        return False

    def load(self):
        # noinspection PyAttributeOutsideInit
        self.img = pygame.image.load(self.default)
        self.screen.blit(self.img, (self.pos_x, self.pos_y))


class Bar:
    def __init__(self, width, height, pos_x, pos_y, screen):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen

    def load(self):
        pygame.draw.rect(self.screen, WHITE, (self.pos_x, self.pos_y, self.width, self.height))


# Sorting Algorithms
def bubble():
    pass


def insert():
    pass


def merge():
    pass


def shell():
    pass


def selection():
    pass
