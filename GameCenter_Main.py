'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: MainMultiGame.py
Description: Python GUI program that displays a window with 5 buttons that play different games: Number Guessing, Rock, Paper, Scissors,
Fun Fact Quiz, Create a Shape, and Tic-Tac-Toe
'''

# import all widgets and modules needed
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint
import json
from PIL import ImageTk, Image
from GameCenter_NumberGuessing import NumberGuessingGame
from GameCenter_RockPaperScissors import RockPaperScissorsGame

class mainWindow(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        # geometry can be set as "lengthxwidth+x-pos+y-pos" to make the position open on a set surface when the GUI gets opened
        self.geometry("690x600+350+50")
        self.title("MultiGame")
        self.config(background = "#F2D4CC")
        
        titleLabel = ttk.Label(self, text = "Welcome to the MultiGame!", style = "Main.TLabel")
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        chooseLabel = ttk.Label(self, text = "Choose Your Game", style = "Main.TLabel")
        chooseLabel.place(relx = 0.5, rely = 0.21, anchor = CENTER)
        
        # button for game 1: Number Guessing
        game1PlayButton = ttk.Button(self, text = "Number Guessing", compound = tk.LEFT, width = 25, style = "Main.TButton", command = self.game1ButtonClicked)
        game1PlayButton.place(relx = 0.5, rely = 0.32, anchor = CENTER)
        
        # button for game 2: Rock, Paper, Scissors
        game2PlayButton = ttk.Button(self, text = "Rock, Paper, Scissors", compound = tk.LEFT, width = 25, style = "Main.TButton", command = self.game2ButtonClicked)
        game2PlayButton.place(relx = 0.5, rely = 0.42, anchor = CENTER)
        
        # create a style object
        self.style = ttk.Style(self)
        
        # add color to a ttk button
        self.style.theme_use("alt")
        
        # this will add style for the Labels and will be named "TLabel"
        self.style.configure("Main.TLabel", font = ("courier", 20, "bold"), background = "#F2D4CC")
        
        # style for the buttons
        self.style.configure("Main.TButton", height = 8, font = ("courier", 12, "bold"), background = "#FF99FF", foreground = "black")
        
        # for when the buttons are active
        self.style.map("Main.TButton", background = [("active", "#D3D3D3")])
        
    # functions that will be called once their respective button is clciked
    def game1ButtonClicked(self):
        game1_Window = NumberGuessingGame()
        game1_Window.mainloop()
        
    def game2ButtonClicked(self):
        game2_Window = RockPaperScissorsGame()
        game2_Window.mainloop()
        
        
# run the main window
if __name__ == "__main__":
    master = mainWindow()
    master.mainloop()