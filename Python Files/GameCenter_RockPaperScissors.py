'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: GameCenter_RockPaperScissors.py
Description: Python GUI program that displays a window with 5 buttons that play different games: Number Guessing, Rock, Paper, Scissors,
Fun Fact Quiz, Create a Shape, and Tic-Tac-Toe
'''

# import widgets and modules that needed for the program to run
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from GameCenter_RockPaperScissors_SinglePlayer import singlePlayerNameEntries
# from GameCenter_RockPaperScissors_MultiPlayer import multiPlayerNameEntries

class RockPaperScissorsGame(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        self.title("Rock, Paper, Scissors")
        self.geometry("800x640+270+20")
        self.config(background = "#FFFF66")
        
        titleLabel = ttk.Label(self, text = "Rock, Paper, Scissors", style = "title.TLabel")
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        chooseLabel = ttk.Label(self, text = "Choose Your Game Type", style = "label.TLabel")
        chooseLabel.place(relx = 0.5, rely = 0.52, anchor = CENTER)
        
        # button for the single player version
        singlePlayerButton = ttk.Button(self, text = "Single Player", width = 23, style = "functionButtons.TButton", command = self.singlePlayerButtonClicked)
        singlePlayerButton.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        
        # button for the multiplayer version
        multiPlayerButton = ttk.Button(self, text = "Multiplayer", width = 23, style = "functionButtons.TButton", command = "self.multiPlayerButtonClicked")
        multiPlayerButton.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        
        # button for the user to go back to the main menu
        backToMenu = ttk.Button(self, text = "Back to Menu", width = 23, style = "functionButtons.TButton", command = self.destroy)
        backToMenu.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        
        # label that lists the directions for the game
        self.tellLabel = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game'!" +
            "\nIn this game, you will be asked to choose to play a single player or a" + 
            "\nmultiplayer game. In a single player game, you will play against the" +
            "\ncomputer. In a multiplayer game, you and another player will play" 
            "\nagainst each other. \nEnjoy Playing!", style = 'tellLabel.TLabel')
        self.tellLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        self.style.theme_use("alt")
        
        # style for labels, buttons, and entries
        self.style.configure('title.TLabel', font = ('courier', 30, 'bold'), background = '#FFFF66')
        self.style.configure('label.TLabel', font = ('courier', 25, 'bold'), background = '#FFFF66')
        self.style.configure('functionButtons.TButton', font = ('courier', 15, 'bold'), background = '#FF6666',
        foreground = 'black')
        self.style.configure('tellLabel.TLabel', font = ('courier', 13, 'bold'), background = '#FFFF66', borderwidth = 2, width = 69,
        height = 10, relief = SOLID)
        
    def singlePlayerButtonClicked(self):
        singlePlayerGame = singlePlayerNameEntries()
        singlePlayerGame.mainloop()

    def multiPlayerButtonClicked(self):
        self.new = multiPlayerNameEntries()
            
if __name__ == "__main__":
    master = RockPaperScissorsGame()
    master.mainloop()
