import pygame,sys
from pygame.locals import *

pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
HIGHT = 600
WIDTH = 600
SIZE = WIDTH//3
DISPLAYSURF = pygame.display.set_mode((HIGHT,WIDTH))



pygame.display.set_caption("Hello World")


def drawgrid():
    #vertical
    for col in range(SIZE,HIGHT,SIZE):
        pygame.draw.line(DISPLAYSURF,WHITE,(0,col),(WIDTH,col),width=5)
    #horizontal
    for row in range(SIZE,WIDTH,SIZE):
        pygame.draw.line(DISPLAYSURF,WHITE,(row,0),(row,HIGHT),width=5)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    drawgrid()
