import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (49, 49, 49)

pygame.init()
font = pygame.font.SysFont("Helvetica", 35)
running = True
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

screen = pygame.display.set_mode((800, 600))

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
def bubble(bars):
    for i in range(0, len(bars)-1):
        if bars[i] > bars[i+1]:
            bars[i], bars[i+1] = bars[i+1], bars[i]
            screen.fill(BACKGROUND)
            pos_y = 50
            for bar in bars:
                x = Bar(bar, 20, 50, pos_y, screen)
                pos_y += 50
                x.load()

            pygame.display.update()
            pygame.time.wait(200)



def insert(bars):
    for i in range(1, len(bars)):
        number = bars[i]
        comparing = i - 1
        while comparing >= 0 and number < bars[comparing]:
            bars[comparing+1] = bars[comparing]
            comparing -= 1
        bars[comparing+1] = number
        screen.fill(BACKGROUND)
        pos_y = 50
        for bar in bars:
            x = Bar(bar, 20, 50, pos_y, screen)
            pos_y += 50
            x.load()

        pygame.display.update()
        pygame.time.wait(300)

def merge(bars):
    if len(bars) > 1:
        left_bars = bars[:len(bars)//2]
        right_bars = bars[len(bars)//2:]
        merge(left_bars)
        merge(right_bars)

        element_final = 0
        element_left = 0
        element_right = 0
        while element_left < len(left_bars) and element_right < len(right_bars):
            if left_bars[element_left] < right_bars[element_right]:
                bars[element_final] = left_bars[element_left]
                element_left += 1 
            else:
                bars[element_final] = right_bars[element_right]
                element_right += 1
            element_final += 1
 
        while element_left < len(left_bars):
            bars[element_final] = left_bars[element_left]
            element_left += 1
            element_final += 1

        while element_right < len(right_bars):
            bars[element_final] = right_bars[element_right]
            element_right += 1
            element_final += 1
        screen.fill(BACKGROUND)
        pos_y = 50
        for bar in bars:
            x = Bar(bar, 20, 50, pos_y, screen)
            pos_y += 50
            x.load()
        pygame.display.update()
        pygame.time.wait(300)

def shell(bars):
    lenbars = len(bars)
    interval = len(bars) // 2
    while interval > 0:
        for first_num in range(interval, lenbars):
            temp = bars[first_num]
            second_num = first_num
            while second_num >= interval and bars[second_num - interval] > temp:
                bars[second_num] = bars[second_num - interval]
                second_num -= interval
                screen.fill(BACKGROUND)
                pos_y = 50
                for bar in bars:
                    x = Bar(bar, 20, 50, pos_y, screen)
                    pos_y += 50
                    x.load()
                pygame.display.update()
                pygame.time.wait(500)   
            bars[second_num] = temp
        interval //= 2
        screen.fill(BACKGROUND)
        pos_y = 50
        for bar in bars:
            x = Bar(bar, 20, 50, pos_y, screen)
            pos_y += 50
            x.load()
        pygame.display.update()
        pygame.time.wait(500)

def selection(bars):
    for i in range(len(bars)):
        minimum_index = i
        for j in range(i+1, len(bars)):
            if bars[j] < bars[minimum_index]:
                minimum_index = j

        bars[minimum_index], bars[i] = bars[i], bars[minimum_index]
        screen.fill(BACKGROUND)
        pos_y = 50
        for bar in bars:
            x = Bar(bar, 20, 50, pos_y, screen)
            pos_y += 50
            x.load()
        pygame.display.update()
        pygame.time.wait(200)