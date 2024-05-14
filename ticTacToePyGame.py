# import the required libraries of pygame, time, and the sys library of python
# time will keep tract of the the time and the sleep() function that will be used
import pygame as pg
import sys
import time
from pygame.locals import *

# declare the global variables

# for storing 'x' or 'o' values as a character
XO = 'x'

# stor the winner's value at any instant of code
winner = None

# check if the game is a draw
draw = None

# set the width of the game window
width = 400

# set the height of the game window
height = 400

# background color of the game window
white = (255, 255, 255)

# color of the straightlines on the white game board, dividing the board into 9 parts
lineColor = (0, 0, 0)

# set up the 3 * 3 board in canvas
board = [[None] * 3, [None * 3], [None * 3]]

# design the game display

# initialize the pygame window
pg.init()

# set the fps (frame per second) manually
fps = 30

# used to track time
clock = pg.time.Clock()

# method used to build the infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# set up the nametag for the game window
pg.display.set_caption("Tic Tac Toe")

# load the images as python objects
initiatingWindow = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")

def gameInitializingWindow():
    
    # display over the screen
    screen.blit(initiatingWindow, (0,0))
    
    # update the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)
    
    # draw the vertical lines
    pg.draw.line(screen, lineColor, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, lineColor, (width / 3 * 2, 0),
                 (width / 3 * 2, height), 7)
    
    # draw the horizontal lines
    pg.draw.line(screen, lineColor, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, lineColor, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    
    drawStatus()
    
def drawStatus():
    
    # get the global variable draw into action
    global draw
    
    if (winner is None):
        message = XO.upper() + "'s Turn!"
    else:
        message = winner.upper() + " won!"
    if (draw):
        message = "Game Draw!"
        
    # set up a font object
    font = pg.font.Font('Courier', 30)
    
    # set up the font properties such as color and width
    text = font.render(message, 1, (255, 255, 255))
    
    # copy the rendered message onto the board by creating a small block at the bottom of the main display
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    textRect = text.get_rect((center = (width / 2), 500 - 50))
    screen.blit(text, textRect)
    pg.display.update()
    
# main algorithm
    
def checkWin():
    
    global board, winner, draw
    
    # check for winning rows
    for row in range(0,3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6),
                         4)
            break
    # check for winning columns
    for col in range(0,3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break
        
    # check for diagonal winners
    for col in range(0,3):
        if ((board[0][col] == ))    
        