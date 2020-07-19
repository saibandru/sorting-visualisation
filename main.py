import pygame
from objects import Button, Bar
import random

# Creating colours
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (49, 49, 49)

# Initialising pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Making the caption
pygame.display.set_caption("Sort Visualisation")

# Inserting an icon
icon = pygame.image.load("./art/bar-chart-icon.jpg")
font = pygame.font.SysFont("Oxygen", 35)
pygame.display.set_icon(icon)

# Function for multiline
def blit_text(text, pos, font=font, color=WHITE, surface=screen):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, _ = surface.get_size()
    max_width -= 75
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Bubble Sort
bub_sort_x = 84
bub_sort_y = 119
bubble_sort = Button(screen, bub_sort_x, bub_sort_y, "./art/Bubble Sort Btn.png", "./art/Bubble Sort Btn (Hover State).png")

# Insertion Sort
ins_sort_x = 84
ins_sort_y = 204
insert_sort = Button(screen, ins_sort_x, ins_sort_y, "./art/Insert Sort Btn (Insert Sort Btn).png", "./art/Insert Sort Btn.png")

# Merge Sort
mer_sort_x = 84
mer_sort_y = 289
merge_sort = Button(screen, mer_sort_x, mer_sort_y, "./art/Merge Sort Btn.png", "./art/Merge Sort Btn (Hover State).png")

# Shell Sort
she_sort_x = 84
she_sort_y = 374
shell_sort = Button(screen, she_sort_x, she_sort_y, "./art/Shell Sort Btn.png", "./art/Shell Sort Btn (Hover State).png")

# Selection Sort
sel_sort_x = 84
sel_sort_y = 459
selection_sort = Button(screen, sel_sort_x, sel_sort_y, "./art/Selection Sort Btn.png", "./art/Selection Sort Btn (Hover State).png")


# Starting the game loop
loop1 = True
loop2 = True

while loop1: 
    # Background
    screen.fill(BACKGROUND)
    img = pygame.image.load("./art/Rectangle 10.png")
    screen.blit(img, (45, 30))
    img_2 = pygame.image.load("./art/Sorting Visualisation.png")
    screen.blit(img_2, (225, 47))
    img_2 = pygame.image.load("./art/Description.png")
    screen.blit(img_2, (400, 125))

    # List of Buttons
    buttons_list = [bubble_sort, insert_sort, merge_sort, shell_sort, selection_sort]
    sort_description = {
        bubble_sort: "Bubble Sort (or Sinking Sort) is the simplest sorting algorithm. It traverses through a list, swapping adjacent elements if they are in the wrong order. It has a Big \'O\' complexity of O(n^2)", 
        insert_sort: "The Insert(ion) Sort algorithm traverses through a list, slotting the number into a spot where the number before it is smaller and the number after, greater. It has a Big \'O\' complexity of O(n^2)",
        merge_sort: "Merge Sort is a an algorithm that splits up a list of number into individual numbers before comparing and combining these individual numbers together. It has a Big \'O\' complexity of O(n log(n))",
        shell_sort: "The Shell Sort algorithm takes a number and compares it with another number in a list and switches them accordingly. It can be visualised as a mix of Bubble and Insert Sort. It has a Big \'O\' complexity of O(n (log(n))^2)",
        selection_sort: "A Selection Sort algorithm finds the smallest value in a list and puts in front. Next it finds the second smallest value and places it in the second slot. This goes on until the list in finally sorted It has a Big \'O\' complexity of O(n^2)"
    }

    for button in buttons_list:
        button.load()

    for button in buttons_list:
        x = button.mouse_hover()
        if x is True:
            blit_text(sort_description[button], (400, 180))

    # Checking whether buttons have been pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False
            loop2 = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in buttons_list:
                if button.mouse_hover() == True:
                    loop1 = False

    pygame.display.update()

bars = []
for i in range(10):
    bars.append([random.randrange(10, 300), 20])

print(bars)

while loop2:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop2 = False
    pos_y = 50
    for bar in bars:
        x = Bar(bar[0], bar[1], 50, pos_y, screen)
        pos_y += 50
        x.load()

    pygame.display.update()
