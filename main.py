import pygame
import sys

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")

WIDTH = 600
HIGHT = 600
CH = 3
SCALE = WIDTH/CH
RADIUS = SCALE/2*(3/4)
LINE_WIDTH = 10
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARD = [[None]*CH for _ in range(CH)]

frame = pygame.display.set_mode((WIDTH,HIGHT))


def empty(x,y):
    if BOARD[x][y] == None:
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

def draw_symbol(x_,y_,player):
    point = {(0,0):(1,1),(0,1):(1,3),(0,2):(1,5),(1,0):(3,1),(1,1):(3,3),(1,2):(3,5),(2,0):(5,1),(2,1):(5,3),(2,2):(5,5)}
    x,y = point[(x_,y_)]
    o_color = (255,0,255)
    x_color = (0,204,204)
    if player == 'O':
        pygame.draw.circle(frame, o_color, (HIGHT*x//6,WIDTH*y//6), width=LINE_WIDTH, radius=RADIUS)
    else:
        p1,p2 = (HIGHT*x//6,WIDTH*y//6)
        pygame.draw.lines(frame, x_color, True, [(p1-RADIUS,p2-RADIUS),(p1+RADIUS,p2+RADIUS)], width=LINE_WIDTH)
        pygame.draw.lines(frame, x_color, True, [(p1-RADIUS,p2+RADIUS),(p1+RADIUS,p2-RADIUS)], width=LINE_WIDTH)

def check_win():
    color = (255,0,0)
    WIN_LINE=15
    #vertical
    if BOARD[0][0] == BOARD[0][1] == BOARD[0][2] and BOARD[0][0] != None:
        pygame.draw.line(frame, color,(HIGHT//6,0),(HIGHT//6,WIDTH), width=WIN_LINE)
        return True
    elif BOARD[1][0] == BOARD[1][1] == BOARD[1][2] and BOARD[1][0] != None:
        pygame.draw.line(frame, color,(HIGHT*3//6,0),(HIGHT*3//6,WIDTH),width=WIN_LINE)
        return True
    elif BOARD[2][0] == BOARD[2][1] == BOARD[2][2] and BOARD[2][0] != None:
        pygame.draw.line(frame, color,(HIGHT*5//6,0),(HIGHT*5//6,WIDTH),width=WIN_LINE)
        return True

    #horizontal
    elif BOARD[0][0] == BOARD[1][0] == BOARD[2][0] and BOARD[1][0] != None:
        pygame.draw.line(frame,color, (0,WIDTH//6),(HIGHT,WIDTH//6), width=WIN_LINE)
        return True
    elif BOARD[0][1] == BOARD[1][1] == BOARD[2][1] and BOARD[1][1] != None:
        pygame.draw.line(frame,color, (0,WIDTH*3//6),(HIGHT,WIDTH*3//6), width=WIN_LINE)
        return True
    elif BOARD[0][2] == BOARD[1][2] == BOARD[2][2] and BOARD[1][2] != None:
        pygame.draw.line(frame,color, (0,WIDTH*5//6),(HIGHT,WIDTH*5//6), width=WIN_LINE)
        return True

    #diagonal
    elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] and BOARD[1][1] != None:
        pygame.draw.line(frame,color, (0,0),(HIGHT,WIDTH), width=WIN_LINE)
        return True
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] and BOARD[1][1] != None:
        pygame.draw.line(frame,color,(0,HIGHT),(WIDTH,0), width=WIN_LINE)
        return True
    return False


def display_win(player):
    font = pygame.font.Font('freesansbold.ttf',size=HIGHT//8)
    if player == 'O':
        text = font.render('O Player WIN!!!', True, GREEN, BLUE)
    elif player == 'X' :
        text = font.render('X Player WIN!!!', True, GREEN, BLUE)
    
    textRect = text.get_rect()
    textRect.center = (HIGHT // 2, WIDTH // 2)
    frame.blit(text,textRect)

def display_tie():
    font = pygame.font.Font('freesansbold.ttf',size=HIGHT//8)
    text = font.render('Tie!!!', True, GREEN, BLUE)
    textRect = text.get_rect()
    textRect.center = (HIGHT // 2, WIDTH // 2)
    frame.blit(text,textRect)


def restart():
    frame.fill(BLACK)
    draw_grid()
    for row in range(len(BOARD)):
        for col in range(len(BOARD)):
            BOARD[row][col] = None


game_over = False
draw_grid()
player = 'X'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            (x,y) = event.pos
            x_,y_ = int(x//SCALE), int(y//SCALE)
            if empty(x_,y_):
                BOARD[x_][y_] = player
                draw_symbol(x_,y_,player)
                if check_win():
                    display_win(player)
                    game_over = True
                player = 'O' if player == 'X' else 'X'
            else:
                display_tie()
                game_over = True
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r' or event.unicode == 'R':
                restart()
                game_over = False
        
    pygame.display.update()