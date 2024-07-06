import sys
import pygame
winner=None
pygame.init()
#set up display
width,height=300,300
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Toc Toe')
#colors
white=(255,255,255)
line_color=(0,0,0)
x_color=(46,204,113)
o_color=(255,127,80)
#game variables
player_turn="X"
board=[[None,None,None],[None,None,None],[None,None,None]]
game_over=False
#draw grid lines
def draw_lines():
    pygame.draw.line(screen,line_color,(0,100),(300,100),3)
    pygame.draw.line(screen, line_color, (0, 200), (300, 200), 3)
    pygame.draw.line(screen, line_color, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, line_color, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, line_color, (0, 0), (300, 0), 3)
    pygame.draw.line(screen, line_color, (0, 0), (0, 300), 3)
    pygame.draw.line(screen, line_color, (0, 300), (300, 300), 3)
    pygame.draw.line(screen, line_color, (300, 0), (300, 300), 3)
#draw x and o symbols
def draw_symbols(row,col,playerTurn):
    # for row in range(3):
    #     for col in range(3):
    print(row,col,playerTurn)
    if playerTurn=="X":
        pygame.draw.line(screen,x_color,(col*100,row*100),((col+1)*100,(row+1)*100),3)
        pygame.draw.line(screen, x_color, ((col+1) * 100, row * 100), ((col) * 100, (row + 1) * 100), 3)
    elif playerTurn=="O":
        pygame.draw.circle(screen,o_color,(col*100 + 50,row*100 + 50),50,3)
#check for win
def check_win():
    for row in board:
        if row[0]==row[1]==row[2]!=None:
            #print(row[0],row[1],row[2])
            return row[0]
    for col in range(3):
        #print(col)
        if board[0][col]==board[1][col]==board[2][col]!=None:
            print(board[0][2] , board[1][2] , board[2][2])
            return board[0][col]
        if board[0][0]==board[1][1]==board[2][2]!=None:
            return board[0][0]
        if board[0][2]==board[1][1]==board[2][0]!=None:
            return board[1][1]
    return None
#main game type
screen.fill(white)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over and event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            row,col=y//100,x//100
            #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(row * 100, col * 100, 100, 100))
            if board[row][col] is None:
                board[row][col]=player_turn
                player_turn="O" if player_turn=="X" else "X"
                draw_symbols(row,col,player_turn)
                winner=check_win()
                if winner or all(all(cell for cell in row) for row in board):
                    game_over=True
    # screen.fill(white)
    draw_lines()
    # draw_symbols()
    if game_over:
        font=pygame.font.Font(None,36)
        text=font.render("player {} wins!".format(winner) if winner else "It's a draw!",True,line_color)
        text_rect=text.get_rect(center=(width//2,height//2))
        #emoji_image=pygame.image.load("Andhavarapu Jahnavi\Desktop\image.jpg")
        #screen.blit(emoji_image,text_rect)
        screen.blit(text,text_rect)
    pygame.display.flip()