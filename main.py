import pygame

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")

WIDTH = 600
HIGHT = 600
CH = 3
SCALE = WIDTH/CH
RADIUS = SCALE/2*(3/4)
LINE_WIDTH = 10
frame = pygame.display.set_mode((WIDTH,HIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

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

def draw_symbol(x_,y_,player):
    point = {(0,0):(1,1),(0,1):(1,3),(0,2):(1,5),(1,0):(3,1),(1,1):(3,3),(1,2):(3,5),(2,0):(5,1),(2,1):(5,3),(2,2):(5,5)}
    x,y = point[(x_,y_)]
    color = (255,255,255)
    if player == 'O':
        pygame.draw.circle(frame,color,(HIGHT*x//6,WIDTH*y//6),width=LINE_WIDTH,radius=RADIUS)
    else:
        p1,p2 = (HIGHT*x//6,WIDTH*y//6)
        pygame.draw.lines(frame, color, True, [(p1-RADIUS,p2-RADIUS),(p1+RADIUS,p2+RADIUS)], width=LINE_WIDTH)
        pygame.draw.lines(frame, color, True, [(p1-RADIUS,p2+RADIUS),(p1+RADIUS,p2-RADIUS)], width=LINE_WIDTH)

def check_win():
    color = (255,0,0)
    WIN_LINE=15
    #vertical
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != None:
        pygame.draw.line(frame, color,(HIGHT//6,0),(HIGHT//6,WIDTH), width=WIN_LINE)
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != None:
        pygame.draw.line(frame, color,(HIGHT*3//6,0),(HIGHT*3//6,WIDTH),width=WIN_LINE)
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != None:
        pygame.draw.line(frame, color,(HIGHT*5//6,0),(HIGHT*5//6,WIDTH),width=WIN_LINE)
        return True

    #horizontal
    elif board[0][0] == board[1][0] == board[2][0] and board[1][0] != None:
        pygame.draw.line(frame,color, (0,WIDTH//6),(HIGHT,WIDTH//6), width=WIN_LINE)
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[1][1] != None:
        pygame.draw.line(frame,color, (0,WIDTH*3//6),(HIGHT,WIDTH*3//6), width=WIN_LINE)
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[1][2] != None:
        pygame.draw.line(frame,color, (0,WIDTH*5//6),(HIGHT,WIDTH*5//6), width=WIN_LINE)
        return True

    #diagonal
    elif board[0][0] == board[1][1] == board[2][2] and board[1][1] != None:
        pygame.draw.line(frame,color, (0,0),(HIGHT,WIDTH), width=WIN_LINE)
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != None:
        pygame.draw.line(frame,color,(0,HIGHT),(WIDTH,0), width=WIN_LINE)
        return True
    return False


def display_win():
    pass

def restart():
    pass


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
                if check_win():
                    print('WIN')
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
    pygame.display.update()