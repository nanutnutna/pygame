#รอบแรก(ข้อเขียน): คณิตศาสตร์,, วิทยาศาสตร์ทั่วไป, Aptitude test, ภูมิศาสตร์, วิชาการบินเบื้องต้น, และวิชาความรู้เกี่ยวกับการบินไทย

import pygame,sys
from pygame.locals import *

pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
HEIGHT = 600
WIDTH = 600
SIZE = WIDTH//3
DISPLAYSURF = pygame.display.set_mode((HEIGHT,WIDTH))



pygame.display.set_caption("Hello World")


def drawgrid():
    #vertical
    for col in range(SIZE,HEIGHT,SIZE):
        pygame.draw.line(DISPLAYSURF,WHITE,(0,col),(WIDTH,col),width=5)
    #horizontal
    for row in range(SIZE,WIDTH,SIZE):
        pygame.draw.line(DISPLAYSURF,WHITE,(row,0),(row,HEIGHT),width=5)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    drawgrid()


