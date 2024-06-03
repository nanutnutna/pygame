# Taken from husano896's PR thread (slightly modified)
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                #mouseX = event.pos[0]
                #mouseY = event.pos[1]
                #print(mouseX,mouseY)
        pygame.display.update()

# Execute game:
main()