import pygame

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")

WIDTH = 600
HIGHT = 600
CH = 3
SCALE = WIDTH/CH
frame = pygame.display.set_mode((WIDTH,HIGHT))

board = [[None]*CH for _ in range(CH)]

def empty(x,y):
    if board[x][y] == None:
        return True
    return False

def draw_grid():
    color = (255,255,255)
    ### vertical ###
    for i in range(1,3):
        pygame.draw.line(frame,color,(HIGHT * i//3,0),(HIGHT *i //3,WIDTH),width=6)
    ### horizontal ###
    for i in range(1,3):
        pygame.draw.line(frame,color,(0,WIDTH*i//3),(HIGHT,WIDTH*i//3),width=6)

def draw_symbol(x,y,player):
    color = (255,255,255)   
    if player == "X":
        pass
    else:
        pygame.draw.circle(frame,color,(x*SCALE,y*SCALE),radius=50)
        


running = True
draw_grid()
player = 'X'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = event.pos
            x_,y_ = int(x//SCALE), int(y//SCALE)
            print(x_,y_)
            if empty(x_,y_):
                board[x_][y_] = player
                print(board)
                draw_symbol(x_,y_,player)
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
    pygame.display.update()