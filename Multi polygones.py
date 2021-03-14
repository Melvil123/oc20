import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode((640, 640))

start = (0, 0)
size = (0, 0)
drawing = False
line = []
list_lines = []


running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            line.append(start)
            drawing = True

        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            line.append(end)
            list_lines.append(line)
            line = []
            drawing = False

    screen.fill(GRAY)
    if len(list_lines)>0:
        for line_i in list_lines:
            pygame.draw.lines(screen, RED, True, line_i, 3)
    pygame.display.update()

pygame.quit()