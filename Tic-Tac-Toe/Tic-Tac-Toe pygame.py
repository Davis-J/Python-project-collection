import pygame
import sys
def map_mouse_to_board(x,y):
  if x<(gamesize/3):
    column=0
  elif (gamesize/3)<=x<(gamesize/3)*2:
    column=1
  else:
    column=2
  if y<(gamesize/3):
    row=0
  elif (gamesize/3)<=y<(gamesize/3)*2:
    row=1
  else:
    row=2
  return column,row
def draw_board(board):
  myfont=pygame.font.SysFont("Arial",gamesize//3)
  for y in range(3):
    for x in range(3):
      if board[y][x]==xMark:
        color=xcolor
      else:
        color=ocolor
      textsurface=myfont.render(board[y][x],False,color)
      screen.blit(textsurface,(y * (gamesize // 3) + margin + (gamesize // 18), x * (gamesize // 3) + margin-20))
def is_full(board):
  return not any(None in sublist for sublist in board)
def get_winner(board):
  if ((board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0])) and board[1][1] is not None:
    return board[1][1]
  for i in range(3):
    if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0] is not None:
      return board[i][0]
    if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i] is not None:
      return board[0][i]
  return None
def draw_lines():
  pygame.draw.line(screen,linecolor,(margin+gamesize//3,margin),(margin+gamesize//3,screensize-margin),linesize)
  pygame.draw.line(screen,linecolor,(margin+(gamesize//3)*2,margin),(margin+(gamesize//3)*2,screensize-margin),linesize)
  pygame.draw.line(screen,linecolor,(margin,margin+gamesize//3),(screensize-margin,margin+gamesize//3),linesize)
  pygame.draw.line(screen,linecolor,(margin,margin+(gamesize//3)*2),(screensize-margin,margin+(gamesize//3)*2),linesize)
screensize=600
margin=50
gamesize=600-(2*margin)
linesize=10
bgcolor=(0,0,0)
linecolor=(255,255,255)
xcolor=(200,0,0)
ocolor=(0,0,200)
xMark="X"
oMark="O"
board=[[None,None,None],[None,None,None],[None,None,None]]
currentMove="X"
pygame.init()
screen=pygame.display.set_mode((screensize,screensize))
pygame.display.set_caption("Tic Tac Toe")
pygame.font.init()
myfont=pygame.font.SysFont("Arial",gamesize//3)
screen.fill(bgcolor)
canPlay=True
draw_lines()
while(True):
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_RETURN:
        board = [[None, None, None], [None, None, None], [None, None, None]]
        screen.fill(bgcolor)
        draw_lines()
        canPlay = True
    if event.type == pygame.MOUSEBUTTONDOWN and canPlay:
        mouseX, mouseY = pygame.mouse.get_pos()
        row, column = map_mouse_to_board(mouseX - margin, mouseY - margin)
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] is None:
            board[row][column] = currentMove
            currentMove = oMark if currentMove == xMark else xMark
            screen.fill(bgcolor)
            draw_lines()
            draw_board(board)
            winner = get_winner(board)
            if winner is not None:
                myFont = pygame.font.SysFont('Tahoma', screensize // 5)
                text_surface = myFont.render(str(winner) + " has won!", False, linecolor)
                screen.blit(text_surface, (margin, screensize // 2 - screensize // 10))
                canPlay = False
            elif is_full(board):
                myFont = pygame.font.SysFont('Tahoma', screensize // 5)
                text_surface = myFont.render("Draw!", False, linecolor)
                screen.blit(text_surface, (screensize // 10, screensize // 2 - screensize // 10))
    pygame.display.update()