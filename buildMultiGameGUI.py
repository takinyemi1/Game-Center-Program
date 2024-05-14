'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: MultiGameGUI.py
Description: Create a python program where the user has an 3 options for game buttons:
1. Number Guessing Game, 2. Rock, Paper, Scissors, or 3. Fun Fact Game. Each game will have a 
separate button that the user will click in order to open a new window that will play the game.
'''
# import all widgets and modules that are available in tkinter and ttk module
from tkinter import *
# import json to use the json file that holds the questions&answers data
import json
from tkinter import messagebox as mb
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
# import random
from random import randint
import random
import math

class mainWindow(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        # geometry can be set as "lengthxwidth+x-pos+y-pos" to make it open at a certain position
        self.geometry('690x600+350+50')
        self.title('MultiGame')
        self.config(background = '#F2D4CC')

        titleLabel = ttk.Label(self, text = "Welcome to the Multigame!", style = 'Main.TLabel')
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        chooseLabel = ttk.Label(self, text = "Choose Your Game", style = 'Main.TLabel')
        chooseLabel.place(relx = 0.5, rely = 0.21, anchor = CENTER)

        # button that allows user to choose game 1: Number Guessing Game
        game1PlayButton = ttk.Button(self, text = "Number Guessing", width = 23, style = 'Main.TButton',
        command = self.game1ButtonClicked)
        # game1PlayButton.bind("<Button>", lambda e: game1Window(master))
        game1PlayButton.place(relx = 0.5, rely = 0.32, anchor = CENTER)
        
        game2PlayButton = ttk.Button(self, text = "Rock, Paper, Scissors", width = 23, style = 'Main.TButton', command = self.game2ButtonClicked)
        # , height = 2
        # , font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game2PlayButton.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        # button that allows the user to choose game 3: Fun Fact Game
        game3PlayButton = ttk.Button(self, text = "Fun Fact Quiz", width = 23, style = 'Main.TButton', command = self.game3ButtonClicked)
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game3PlayButton.place(relx = 0.5, rely = 0.48, anchor = CENTER)

        # button that allows the user to choose game 4: Create Shapes
        game4PlayButton = ttk.Button(self, text = "Create a Shape", width = 23, style = 'Main.TButton', command = self.game4ButtonClicked)
        game4PlayButton.place(relx = 0.5, rely = 0.56, anchor = CENTER)

        # button that allows the user to choose game 5: Tic-Tac-Toe
        game5PlayButton = ttk.Button(self, text = "Tic-Tac-Toe", width = 23, style = 'Main.TButton', command = "")
        game5PlayButton.place(relx = 0.5, rely = 0.64, anchor = CENTER)
        
        # button that allows the user to choose game 6: Tetris 
        game6PlayButton = ttk.Button(self, text = "Tetris", width = 23, style = 'Main.TButton', command = '')
        game6PlayButton.place(relx = 0.5, rely = 0.72, anchor = CENTER)

        # button that allows you to exit the window
        exitButton = ttk.Button(self, text = "Exit Game", width = 10, style = 'Main.TButton', command = exit)
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = 'light blue', fg = 'black', width = 10, height = 2, command = exit)
        exitButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        # create a style object
        self.style = ttk.Style(self)
        # how to add color to a ttk button
        self.style.theme_use('alt')
        # this adds style for the the Labels and will be named 'TLabel' as that's the name for common ttk widget
        # classes
        self.style.configure('Main.TLabel', font = ('courier', 20, 'bold'), background = '#F2D4CC')
        # style for the buttons
        self.style.configure('Main.TButton', height = 3, font = ('courier', 12, 'bold'), background = '#FF99FF',
        foreground = 'black')
        # used for if the buttons are active 
        self.style.map('Main.TButton', background = [('active', '#d3d3d3')])
        
    # functions that will open the specified game once their designated buttons are clicked
    def game1ButtonClicked(self):
        self.new = game1Window()
        
    def game2ButtonClicked(self):
        self.new = game2Window()
        
    def game3ButtonClicked(self):
        self.new = game3Window()
        
    def game4ButtonClicked(self):
        game4Window(self)

class game1Window(Toplevel):
    
    def __init__(self):
        
        super().__init__() # master = master
        self.title("Number Guessing")
        self.geometry("850x650+290+30")
        self.config(background = '#99FFCC')
        
        # create variable sVar that holds your StringVar() which holds string data 
        # that is able to be retrieved
        self.sVar = StringVar()
        
        # create variable trial and set equal to 1
        self.trial = 1
        
        # create variable total and set it equal to 5
        self.total = 5
        
        # create variable randNum and set equal to the range of 0 to 100
        self.randNum = randint(0, 100)
        
        # labels, entries, and buttons for game1Window
        
        # title label
        self.nLabel = ttk.Label(self, text = 'Number Guessing', style = 'g1.TLabel')
        self.nLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # startLabel that is constantly updated based on the entry of the number guessed after the user 
        # clicks 'Guess Number'
        self.startLabel = ttk.Label(self, text = "Click on Start Game", style = 'start.TLabel') # font size 15
        self.startLabel.place(relx = 0.5, rely = 0.62, anchor = CENTER)
        
        # label for hints
        self.hintLabel = ttk.Label(self, text = '', style = 'hintLabel.TLabel')
        self.hintLabel.place(relx = 0.5, rely = 0.77, anchor = CENTER)
    
        # startButton allows you to start the guessing game
        self.startButton = ttk.Button(self, text = 'Start Game', style = 'g1.TButton', command = self.guessNum)
        # self.startButton.place(relx = 0.35, rely = 0.9, anchor = CENTER)
        self.startButton.place(relx = 0.29, rely = 0.9, anchor = CENTER)
        
        # hintButton that allows you to request hints
        self.hintButton = ttk.Button(self, text = "Hint", style = 'g1.TButton', state = DISABLED, command = self.updateHintLabel)
        self.hintButton.place(relx = 0.51, rely = 0.9, anchor = CENTER)
        
        # backButton allows you to exit the game1Window and return to the mainWindow
        self.backButton = ttk.Button(self, text = 'Back to Menu', style = 'g1.TButton', command = self.destroy)
        self.backButton.place(relx = 0.73, rely = 0.9, anchor = CENTER)
        
        # guessNumButton allows you to guess a number a get a result on whether it was too high,
        # too low, or if you got it correct
        # set the state of guessNumButton back to 'diabled' so the user won't be able to get headstart before 
        # they press 'Start Game'
        self.guessNumButton = ttk.Button(self, text = 'Guess Number', style = 'guess.TButton', state = DISABLED, command = self.guessingGame)
        self.guessNumButton.place(relx = 0.35, rely = 0.5, anchor = CENTER)
        
        # entry that allows user to input number guess
        self.guessEntry = ttk.Entry(self, style = 'g1.TEntry', textvariable = self.sVar)
        self.guessEntry.place(relx = 0.65, rely = 0.5, relheight = 0.05, anchor = CENTER)
        
        # label that lisst the directions of the game
        self.welcomeLabel = ttk.Label(self, text = "Welcome to the Number Guessing Game! " +
        "\nIn this game, you will be asked to input a random number" +
        "\nwhich will then be compared to the computer generated number." +
        "\nYou will have 5 trials to guess the number. " +
        "\nYou will be told if the number is too high, too low," + 
        "\nor if you guessed the number correctly. " +
        "\nEnjoy playing!", style = 'welcomeLabel.TLabel') # in order to put a border around a label, have height, width, borderwidth, and
        # relief = SOLID attributes set
        self.welcomeLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        # create a style object 
        self.style = ttk.Style(self)
        
        # style for labels
        self.style.configure('g1.TLabel', font = ('courier', 25, 'bold'), background = '#99FFCC')
        # style for buttons 
        self.style.configure('start.TLabel', font = ('courier', 13, 'bold'), background = '#99FFCC')
        self.style.configure('g1.TButton', font = ('courier', 15, 'bold'), background = '#006600', foreground = 'black',
        width = 12)
        self.style.configure('hintLabel.TLabel', font = ('courier', 11, 'bold'), background = '#99FFCC')
        self.style.configure('guess.TButton', font = ('courier', 13, 'bold'), background = '#006600', foreground = 'black',
        width = 12)
        # style for entry(ies)
        self.style.configure('g1.TEntry', font = ('courier', 15), width = 15)
        # welcomeLabel style
        self.style.configure('welcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#99FFCC',
        borderwidth = 2, width = 69, height = 5, relief = SOLID)
        
    # function that updates the start label by telling the user the game directions
    def updateResult(self, text):
        self.startLabel.configure(text = text)
        
    # function that will have the hint label appear when the hint button is pressed
    def updateHintLabel(self):
        # check if the user's entry is lower than the random number
        if (self.ask < self.randNum):
            hint = (f"Hint: Number is between {self.ask} and 100")
            # set the text of the hint label to the hint given
            self.hintLabel.configure(text = hint)
        # check if the user's entry is higher than the random number
        elif (self.ask > self.randNum):
            hint = (f"Hint: Number is between 0 and {self.ask}")
            # set the text of the hint label to the hint given
            self.hintLabel.configure(text = hint)
        # to check if the entry is empty, get the value of the widget, and then check if its length is = 0
        # elif (len(self.ask) == '0'):
        #     hint = ("Hint: Number has not been entered. Hint unavailable.")
        #     self.hintLabel.configure(text = hint)
    
    # function that's able to enable the Guess Number button and allow the user to begin guessing
    def guessNum(self):
        # set the button back to NORMAL once the user clicks 'Start Game'
        self.guessNumButton.config(state = NORMAL)
        self.hintButton.config(state = NORMAL)
        
        self.sVar = StringVar()
        
        self.trial = 1
        self.total = 5
        self.randNum = randint(0, 100)
        
        # set the text of updateResult
        self.updateResult(text = "Guess a random number between 0 and 100")
        
        # use the delete function to delete the entry after the user guessed the number correctly
        # or after the trials are finished
        # set it to start at 0 (index of the first number or letter), 'end' (function decides where
        # the entry ends)
        self.guessEntry.delete(0, END)
        self.hintLabel['text'] = ''
    
    # function that plays the guessing game
    def guessingGame(self):
        self.sVar = StringVar()
        
        self.trialRun = self.total - self.trial
        
        # since self.guessEntry textvariable is equal to the StringVar(), get the value of the input in the entry and
        # convert to an int
        self.ask = int(self.guessEntry.get()) 
        
        # set the outer statement to run as long as trial doesn't equal 5
        if (self.trial != 5):
            # if your input doesn't equal randNum, check if the user input is less than randNum
            if (self.ask < self.randNum):
                # format the numbers of trials left using f'{trial}'
                # try to format using .format() instead
                self.result = (f"Trial {self.trial}. Your guess {self.ask} was too low!" +
                f"\nYou have {self.trialRun} trials left.")
                self.trial += 1
                
                if (self.hintButton):
                    self.hint = (f"Hint: Number is between {self.ask} and 100.")
                    
            # if user input is greater than randNum
            elif (self.ask > self.randNum):
                self.result = (f"Trial {self.trial}. Your guess {self.ask} was too high!" +
                f"\nYou have {self.trialRun} trials left.")
                self.trial += 1
                
                if (self.hintButton):
                    self.hint = (f"Hint: Number is between 0 and {self.ask}")
             
        # problem: the program kept printing "sorry..." even if the player guessed the random number correctly.
        # solution: put the elif statement for if the number is guessed correctly outside of the inside if statement  
        # if user input is equal to randNum
        elif (self.ask == self.randNum):
            # self.trialRun = self.total - self.trial
            self.result = ("Congratulations! You guessed " + str(self.randNum) + " correctly!" + 
            f"\nYou used {self.trial} trials! \nClick on 'Start Game' to play again or " + 
            "\n'Back to Menu' to return to the main menu.")
            self.guessNumButton.configure(state = DISABLED)    
            self.hintButton.configure(state = DISABLED)  
            
        # check if an entry is valid
        elif (self.ask == ""):
            self.result = ("That is not a valid entry. \nPlease enter a number between 0 and 100.")  
        
        # if the trial reaches zero and you haven't correctly guessed randNum
        else:
            self.result = ("Sorry! You have exhausted the number of trials! " + f"\nThe number was {self.randNum}. "
            + "Thank you for playing!" + "\nClick on 'Start Game to play again or 'Back to Menu' " + 
            "\nto return to the menu.")
            # if you exhaust all your trials, set the state of guessNumButton back to DISABLED, command = ""
            self.guessNumButton.configure(state = DISABLED)
            self.hintButton.configure(state = DISABLED)
            
        # update the result with the text of the condition that gets looped through
        self.updateResult(self.result)
        self.guessEntry.delete(0, END)
        
# this class opens a new window that will display three buttons for three different game options: single player, multiplayer, or back to menu
class game2Window(Toplevel):
    
    def __init__(self):
        
        super().__init__()
        self.title("Rock, Paper, Scissors")
        self.geometry("800x640+270+20")
        self.config(background = '#FFFF66')
        
        titleLabel = ttk.Label(self, text = "Rock, Paper, Scissors", style = 'title.TLabel')
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        chooseLabel = ttk.Label(self, text = "Choose Your Game Type", style = 'label.TLabel')
        chooseLabel.place(relx = 0.5, rely = 0.52, anchor = CENTER)

        # button that allows user to choose the first game type: Single Player
        singlePlayerButton = ttk.Button(self, text = "Single Player", width = 23, style = 'functionButtons.TButton',
        command = self.singlePlayerButtonClicked)
        singlePlayerButton.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        
        # button that allows the user to choose the second game type: Multiplayer
        multiPlayerButton = ttk.Button(self, text = "Multiplayer", width = 23, style = 'functionButtons.TButton', command = self.multiPlayerButtonClicked)
        multiPlayerButton.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        
        # button that allows the user to go back to the main menu
        backTOMenu = ttk.Button(self, text = 'Back to Menu', width = 23, style = 'functionButtons.TButton', command = self.destroy)
        backTOMenu.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        
        # label that lists the directions for the game
        self.tellLabel = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game'!" +
            "\nIn this game, you will be asked to choose to play a" + 
            "\nsingle player game or a multiplayer game." +
            "\nOnce chosen, you will be led to a new window that will allow you to" +
            "\nplay those games based off what was chosen. A single player game will" +
            "\nlet you play against the computer. A multiplayer game will let you \nand another player play" 
            " against each other. \nEnjoy Playing!", style = 'tellLabel.TLabel')
        self.tellLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and entries
        self.style.configure('title.TLabel', font = ('courier', 30, 'bold'), background = '#FFFF66')
        self.style.configure('label.TLabel', font = ('courier', 25, 'bold'), background = '#FFFF66')
        self.style.configure('functionButtons.TButton', font = ('courier', 15, 'bold'), background = '#FF6666',
        foreground = 'black')
        self.style.configure('tellLabel.TLabel', font = ('courier', 13, 'bold'), background = '#FFFF66', borderwidth = 2, width = 69,
        height = 10, relief = SOLID)
        
    def singlePlayerButtonClicked(self):
        self.new = game2SinglePlayerWindow()
    def multiPlayerButtonClicked(self):
        self.new = playerNameEntries()
        
# this function plays the rock, paper, scissors single player game
class game2SinglePlayerWindow(Toplevel):
    
    def __init__(self):
        
        super().__init__()
        self.title("Rock, Paper, Scissors: Single Player")
        self.geometry("840x670+270+15")
        self.config(background = '#58AD38')
        self.win = "Enter 'rock', 'paper', or 'scissors'"
        
        # create variables userCount, compCount, and tieCount that will hold the scores for each win
        self.userCount = 0
        self.compCount = 0
        self.tieCount = 0
        
        # variable sVar that is set equal to StringVar() which will receive the entry of the user's input
        self.sVar = StringVar()
        
        # labels, entries, and buttons for game2Window
        
        # title label
        self.rpsLabel = ttk.Label(self, text = 'Rock, Paper, Scissors Game: Single Player', style = 'multiTitle.TLabel')
        self.rpsLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that gets updated with a new text based on your input of rock, paper, or scissors
        self.playLabel = ttk.Label(self, text = 'Click on Start Game', style = 'gameLabels.TLabel')
        self.playLabel.place(relx = 0.5, rely = 0.59, anchor = CENTER)
        
        # represents the user's score
        self.uLabel = ttk.Label(self, text = '   User    ', style = 'count.TLabel')
        self.uLabel.place(relx = 0.3, rely = 0.72, anchor = CENTER)
        
        # temporary label for user
        self.uTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.uTempLabel.place(relx = 0.3, rely = 0.82, anchor = CENTER)
        
        # represents the tie score
        self.tLabel = ttk.Label(self, text = '   Tie    ', style = 'count.TLabel')
        self.tLabel.place(relx = 0.5, rely = 0.72, anchor = CENTER)
        
        # temporary label for the tie
        self.tTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.tTempLabel.place(relx = 0.5, rely = 0.82, anchor = CENTER)
        
        # represents the computer score
        self.cLabel = ttk.Label(self, text = ' Computer  ', style = 'count.TLabel')
        self.cLabel.place(relx = 0.72, rely = 0.72, anchor = CENTER)
        
        # temporary label for computer
        self.cTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.cTempLabel.place(relx = 0.72, rely = 0.82, anchor = CENTER)
        
        # button that allows you to begin the game
        self.playButton = ttk.Button(self, text = 'Start Game', style = 'useButtons.TButton', command = self.rpsStart)
        self.playButton.place(relx = 0.35, rely = 0.92, anchor = CENTER)
        
        # button that allows you to exit the game2Window and return to the main menu
        self.backMenuButton = ttk.Button(self, text = 'Back to Menu', style = 'useButtons.TButton', command = self.destroy)
        self.backMenuButton.place(relx = 0.65, rely = 0.92, anchor = CENTER)
        
        # button that allows your to submit your input of rock, paper, or scissors, and lets you know if you won,
        # the computer won, or if there was a tie
        # state of the button will be set to disabled until the user clicks 'Start Game'
        self.rpsPlayButton = ttk.Button(self, text = 'Play', style = 'useButtons.TButton', state = DISABLED, command = self.rpsGame)
        self.rpsPlayButton.place(relx = 0.35, rely = 0.5, anchor = CENTER)
        
        # entry that allows you to input rock, paper, or scissors
        self.rpsEntry = ttk.Entry(self, style = 'gameEntry.TEntry', textvariable = self.sVar)
        self.rpsEntry.place(relx = 0.65, rely = 0.5, relheight = 0.05 ,anchor = CENTER)
        
        # buttons for each separate choice
        # self.rockButton = ttk.Button(self, text = "Rock", style = "useButtons.TButton", state = DISABLED, command = "")
        # self.rockButton.place(relx = 0.65, rely = 0.5, anchor = CENTER)
        
        # welcomeLabel that lists the directions for the game
        self.welcomeRPSLabel = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game: Single Player'! " +
            "\nIn this game, you will be asked to input 'rock', 'paper', or " + 
            "\n'scissors'. Once you do, the user's choice will be compared to the " +
            "\ncomputer's choice. For every computer win, user win, or tie, " +
            "\nthose points will be recorded. If either the user or the computer" +
            "\ngets 10 points, the game will end." 
            "\nEnjoy playing!", style = 'welcomeLabel.TLabel')
        self.welcomeRPSLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and entries
        self.style.configure('multiTitle.TLabel', font = ('courier', 25, 'bold'), background = '#58AD38')
        self.style.configure('count.TLabel', font = ('courier', 13, 'bold'), background = '#58AD38', foreground = 'black',
        borderwidth = 2, width = 10, height = 2, relief = SOLID)
        self.style.configure('gameLabels.TLabel', font = ('courier', 13, 'bold'), background = '#58AD38')
        self.style.configure('useButtons.TButton', font = ('courier', 15, 'bold'), background = '#33EFF2', foreground = 'black',
        width = 12)
        self.style.configure('gameEntry.TEntry', font = ('courier', 15), width = 15)
        self.style.configure('welcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#58AD38', borderwidth = 2, width = 66,
        height = 7, relief = SOLID)
        
    # function that updates the play label
    def playUpdate(self, text, u, t, c):
        self.playLabel.configure(text = text)
        self.uTempLabel.configure(text = u)
        self.tTempLabel.configure(text = t)
        self.cTempLabel.configure(text = c)
        
    # function that enables the 'Play' button and allows the user to begin inputting their response
    def rpsStart(self):
        # set the state of rpsPlayButton back to NORMAL
        self.rpsPlayButton.configure(state = NORMAL)
        # self.rockButton.configure(state = NORMAL)
        
        # set trial to 1
        # set compChoice equal to randint(0, 2) so that you can have 0 = rock, 1 = paper, 2 = scissors
        self.compChoice = randint(0, 2)
        self.c = '0'
        self.u = '0'
        self.t = '0'
        self.trial = 1
        
        # set the text that will continue to be updated depending on the entry
        self.playUpdate(text = "Enter 'rock', 'paper', or 'scissors'", u = '0', c = '0', t = '0')
        
        # delete the entry after either the user or the computer wins 10 times/points
        self.rpsEntry.delete(0, END)
        self.uTempLabel['text'] = '0'
        self.tTempLabel['text'] = '0'
        self.cTempLabel['text'] = '0'
        
    # main function that runs the rpsGame
    def rpsGame(self):
        # get the value from rpsEntry and make sure all user inputs are lowercase
        self.userChoice = self.rpsEntry.get().lower()
        
        # problem: for whatever reason after the first entry, it gets deleted and the program prints "Invalid Entry" even though I put rock
        # resolution: in order to fix that problem, i had to remove self.iVar = IntVar() and self.sVar = StringVar() because they had already been initialized in the __init__ function
        
        # create if-elif-else statement that set the int values as their concurring strings
        if (self.compChoice == 0):
            self.compChoice = 'rock'
        elif (self.compChoice == 1):
            self.compChoice = 'paper'
        else:
            self.compChoice = 'scissors'
            
        # in order to fix the issue of the game not stopping after 10 points was reached by either the user or the computer, you have to first account for if the entry is invalid and then
        # account for the rest of the game
        # first check if the entry is valid
        if (self.userChoice != 'rock' and self.userChoice != 'paper' and self.userChoice != 'scissors'):
            self.win = ("Your entry is invalid. Please enter 'rock', 'paper', or 'scissors'.")
            
            self.uTempLabel['text'] = str(self.userCount)
            self.tTempLabel['text'] = str(self.tieCount)
            self.cTempLabel['text'] = str(self.compCount)
            
        # account for the rest of the game
        else:
            # set the outer if statement to run for as long as userCount and compCount != 10
            if (self.compCount != 10 or self.userCount != 10):
                # in order to update compChoice to a random variable after each trial, even if the userChoice stays the same
                self.compChoice = random.choice(['rock', 'paper', 'scissors'])
                
                # conditional statements for each choice 
                # find a way to change the repsonse of each user if the same choice is played
                if (self.compChoice == 'rock' and self.userChoice == 'scissors') or (self.compChoice == 'paper' and self.userChoice == 'rock') or (self.compChoice == 'scissors' and self.userChoice == 'paper'):
                    self.win = (f"Trial {self.trial}. The computer chose " + self.compChoice + " and the user chose " + self.userChoice + "." +
                    "\nThe computer wins a point!")
                    
                    # call temporary text of cTempLabel and set it equal to the update of compCount
                    self.compCount += 1
                    self.cTempLabel['text'] = str(self.compCount)
                    self.trial += 1
                
                # have the order of conditions match the first if statement
                elif (self.compChoice == 'scissors' and self.userChoice == 'rock') or (self.compChoice == 'rock' and self.userChoice == 'paper') or (self.compChoice == 'paper' and self.userChoice == 'scissors'):
                    self.win = (f"Trial {self.trial}. The computer chose " + self.compChoice + " and the user chose " + self.userChoice + "." +
                    "\nThe user wins a point!")
                    
                    # call the temporary text of uTempLabel and set it equal to the update of userCount
                    self.userCount += 1
                    self.uTempLabel['text'] = str(self.userCount)
                    self.trial += 1
                
                # solution: i had to account for a tie in the game for the entry of 'scissors' to be accepted
                elif (self.compChoice == self.userChoice):
                    self.win = ("It's a tie!")
                    
                    # update tieCount
                    self.tieCount += 1
                    self.tTempLabel['text'] = str(self.tieCount)
                    self.trial += 1
                
                # problem: game doesn't stop after 10 points have been reached
                # solution: instead of an else statement for the outside loop, put an if statement in the game loop 
                if (self.compCount == 10):
                    self.win = ("Looks like the computer has reached 10 points, which means" + 
                    "\nthe user lost! Thank you for playing! To play again, Click" +
                    "\n'Start Game'. To go back to the menu, click 'Back to Menu'.")
            
                    self.rpsPlayButton.configure(state = DISABLED)
                    self.uTempLabel['text'] = '0'
                    self.tTempLabel['text'] = '0'
                    self.cTempLabel['text'] = '0'
                    
                elif (self.userCount == 10):
                    self.win = ("Looks like the user has reached 10 points, which means" +
                    "\nthe computer lost! Thank you for playing! To play again, Click" +
                    "\n'Start Game'. To go back to the menu, click 'Back to Menu'.")
                    
                    self.rpsPlayButton.configure(state = DISABLED)
                    self.uTempLabel['text'] = '0'
                    self.tTempLabel['text'] = '0'
                    self.cTempLabel['text'] = '0'
                
        # update the text of playUpdate by calling the text of win, cTemp, tTemp, uTemp
        self.playUpdate(self.win, self.uTempLabel['text'], self.tTempLabel['text'], self.cTempLabel['text'])
            
# this function displays the page for both users to input their names
class playerNameEntries(tk.Toplevel):
    
    def __init__(self, root = None):
        
        super().__init__(root)
        self.title("Rock, Paper, Scissors: Multiplayer Entries")
        self.geometry("840x670+270+15")
        self.config(background = '#B54FC6')
        
        # create your style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and entries
        self.style.configure('multiTitle.TLabel', font = ('courier', 22, 'bold'), background = '#B54FC6')
        self.style.configure('player1.TLabel', font = ('courier', 15, 'bold'), background = '#B54FC6')
        self.style.configure('player1.TEntry', font = ('courier', 20), width = 15)
        self.style.configure('player2.TLabel', font = ('courier', 15, 'bold'), background = '#B54FC6')
        self.style.configure('player2.TEntry', font = ('courier', 20), width = 15)
        self.style.configure('playRPS.TButton', font = ('courier', 15, 'bold'), width = 15, background = '#6F93E5', foreground = 'black')
        self.style.configure('multiWelcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#B54FC6', borderwidth = 2, width = 66,
        height = 7, relief = SOLID)
        
        # separate variables that will receive the string inputs of the user's entries
        self.player1SVar = StringVar()
        self.player2SVar = StringVar()
        
        # call the entriesPage function which will display the entry options for the first and last name
        self.entriesPage()

    def entriesPage(self):
        # title label
        self.rpsLabel = ttk.Label(self, text = 'Rock, Paper, Scissors Game: Multiplayer Entries', style = 'multiTitle.TLabel')
        self.rpsLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label and entry for player 1 name
        self.player1NameLabel = ttk.Label(self, text = 'Enter Name for Player 1', style = 'player1.TLabel')
        self.player1NameLabel.place(relx = 0.3, rely = 0.45, anchor = CENTER)
        
        self.player1NameEntry = ttk.Entry(self, style = 'player1.TEntry', textvariable = self.player1SVar)
        self.player1NameEntry.place(relx = 0.3, rely = 0.55, relheight = 0.05 ,anchor = CENTER)
        
        # label and entry for player 2 name
        self.player2NameLabel = ttk.Label(self, text = 'Enter Name for Player 2', style = 'player2.TLabel')
        self.player2NameLabel.place(relx = 0.73, rely = 0.45, anchor = CENTER)
        
        self.player2NameEntry = ttk.Entry(self, style = 'player2.TEntry', textvariable = self.player2SVar)
        self.player2NameEntry.place(relx = 0.73, rely = 0.55, relheight = 0.05, anchor = CENTER)
        
        # button that moves to the game page
        self.playRPSGame = ttk.Button(self, text = 'Play Game', style = 'playRPS.TButton', command = self.displayMultiplayerGame)
        self.playRPSGame.place(relx = 0.3, rely = 0.89, anchor = CENTER)
        
        # button that moves back to the rps menu
        self.backRPS = ttk.Button(self, text = 'Back to Menu', style = 'playRPS.TButton', command = self.destroy)
        self.backRPS.place(relx = 0.7, rely = 0.89, anchor = CENTER)
        
        self.welcome = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game'! " +
            "\nFirst, input player 1's name and then input player 2's name." + 
            "\nOnce that is done, click the 'Play Game' button, which will" +
            "\nthen lead you to the rock, paper, scissors game.", style = 'multiWelcomeLabel.TLabel')
        self.welcome.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        
    # this function will get both player 1 and player 2's names and display them in the actual game
    def displayMultiplayerGame(self):
        # get the entries of each player entry so that it can be displayed on the next page
        player1Name = self.player1SVar.get()
        player2Name = self.player2SVar.get()
        
        # check if the user entered both player's names
        if (player1Name and player2Name):
            # destroy the current page 
            self.destroy()
            # and open the "page" (class) that will play the actual game
            # use self.master to match with the mainWindow
            game2MultiPlayerWindow(self.master, player1Name, player2Name)
        # if they have not entered any names, display a label that alerts them that they cannot move to the next page (game page) until they enter a name
        else:
            self.nameLabel = ttk.Label(self, text = 'Please enter names for both players. \nYou cannot move to the game page otherwise.', style = 'player2.TLabel')
            self.nameLabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)
            
# this function plays the rock, paper, scissors single player game
class game2MultiPlayerWindow(tk.Toplevel):
    
    def __init__(self, root, player1Name, player2Name):
        
        # change each option into a button with an image
        
        super().__init__(root)
        self.title("Rock, Paper, Scissors: Multiplayer")
        self.geometry("900x670+270+15")
        self.config(background = '#B54FC6')
        self.win = "Enter 'rock', 'paper', or 'scissors'"
        
        # create variables player1Count, player2Count, and tieCount that will hold the scores for each win
        self.player1Count = 0
        self.player2Count = 0
        self.tieCount = 0
        
        # for the player entries
        self.p1sVar = StringVar()
        self.p2sVar = StringVar()
    
        # labels, entries, and buttons for game2Window
        
        # title label
        self.rpsLabel = ttk.Label(self, text = 'Rock, Paper, Scissors Game: Multiplayer', style = 'multiT.TLabel')
        self.rpsLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that gets updated with a new text based on your input of rock, paper, or scissors
        self.playLabel = ttk.Label(self, text = 'Click on Start Game', style = 'playerName.TLabel')
        self.playLabel.place(relx = 0.5, rely = 0.59, anchor = CENTER)
        
        # represents player 1's score
        self.player1Label = ttk.Label(self, text = (f' Player 1: {player1Name}    '), style = 'score.TLabel')
        self.player1Label.place(relx = 0.2, rely = 0.72, anchor = CENTER)
        
        # temporary label for player 1
        self.player1TempLabel = ttk.Label(self, text = '0', style = 'counter.TLabel')
        self.player1TempLabel.place(relx = 0.2, rely = 0.82, anchor = CENTER)
        
        # represents the tie score
        self.tLabel = ttk.Label(self, text = '        Tie    ', style = 'score.TLabel')
        self.tLabel.place(relx = 0.49, rely = 0.72, anchor = CENTER)
        
        # temporary label for the tie
        self.tTempLabel = ttk.Label(self, text = '0', style = 'counter.TLabel')
        self.tTempLabel.place(relx = 0.49, rely = 0.82, anchor = CENTER)
        
        # represents player 2's score
        self.player2Label = ttk.Label(self, text = (f'   Player 2: {player2Name}  '), style = 'score.TLabel')
        self.player2Label.place(relx = 0.75, rely = 0.72, anchor = CENTER)
        
        # temporary label for player 2
        self.player2TempLabel = ttk.Label(self, text = '0', style = 'counter.TLabel')
        self.player2TempLabel.place(relx = 0.75, rely = 0.82, anchor = CENTER)
        
        # button that allows you to begin the game
        self.playButton = ttk.Button(self, text = 'Start Game', style = 'rpsbtn.TButton', command = self.rpsStart)
        self.playButton.place(relx = 0.35, rely = 0.92, anchor = CENTER)
        
        # button that allows you to exit the game2Window and return to the main menu
        self.backMenuButton = ttk.Button(self, text = 'Back to Menu', style = 'rpsbtn.TButton', command = self.destroy)
        self.backMenuButton.place(relx = 0.65, rely = 0.92, anchor = CENTER)
        
        # button that allows your to submit your input of rock, paper, or scissors, and lets you know if you won,
        # the computer won, or if there was a tie
        # state of the button will be set to disabled until the user clicks 'Start Game'
        self.rpsPlayButton = ttk.Button(self, text = 'Play', style = 'rpsbtn.TButton', state = DISABLED, command = self.mutliRPSGame)
        self.rpsPlayButton.place(relx = 0.72, rely = 0.5, anchor = CENTER)
        
        # label that displays player 1's name
        self.player1_Name = ttk.Label(self, text = f'{player1Name}', style = 'playerName.TLabel')
        self.player1_Name.place(relx = 0.27, rely = 0.45, anchor = CENTER)
        
        # entry that allows player 1 to input rock, paper, or scissors
        self.player1Entry = ttk.Entry(self, style = 'enterRPS.TEntry', textvariable = self.p1sVar)
        self.player1Entry.place(relx = 0.27, rely = 0.5, relheight = 0.05, anchor = CENTER)
        
        # label that displays player 2's name
        self.player2_Name = ttk.Label(self, text = f'{player2Name}', style = 'playerName.TLabel')
        self.player2_Name.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        
        # entry that allows player 2 to input rock, paper, or scissors
        self.player2Entry = ttk.Entry(self, style = 'enterRPS.TEntry', textvariable = self.p2sVar)
        self.player2Entry.place(relx = 0.5, rely = 0.5, relheight = 0.05, anchor = CENTER)
        
        # welcomeLabel that lists the directions for the game
        self.welcomeRPSLabel = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game'! " +
            "\nIn this game, both players will be prompted to enter 'rock', 'paper', or" + 
            "\n'scissors'. Once that is done, player 1's choice will be compared to" +
            "\nplayer 2's choice. For every player 1 win, player 2 win, or tie, " +
            "\nthose points will be recorded. If either player 1 or player 2" +
            "\nobtain 10 points, the game will end." 
            "\nEnjoy playing!", style = 'multiWelcome.TLabel')
        self.welcomeRPSLabel.place(relx = 0.5, rely = 0.27, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and entries
        self.style.configure('multiT.TLabel', font = ('courier', 25, 'bold'), background = '#B54FC6')
        self.style.configure('score.TLabel', font = ('courier', 11, 'bold'), background = '#B54FC6', foreground = 'black',
        borderwidth = 2, width = 18, height = 2, relief = SOLID)
        self.style.configure('counter.TLabel', font = ('courier', 13, 'bold'), background = '#B54FC6')
        self.style.configure('rpsbtn.TButton', font = ('courier', 15, 'bold'), background = '#6F93E5', foreground = 'black',
        width = 12)
        self.style.configure('enterRPS.TEntry', font = ('courier', 15), width = 15)
        self.style.configure('multiWelcome.TLabel', font = ('courier', 13, 'bold'), background = '#B54FC6', borderwidth = 2, width = 68,
        height = 8, relief = SOLID)
        self.style.configure('playerName.TLabel', font = ('courier', 12, 'bold'), background = '#B54FC6')
        
    # function that updates the play label
    def playUpdate(self, text, p1, t, p2):
        self.playLabel.configure(text = text)
        self.player1TempLabel.configure(text = p1)
        self.tTempLabel.configure(text = t)
        self.player2TempLabel.configure(text = p2)
        
    # function that enables the 'Play' button and allows the user to begin inputting their response
    def rpsStart(self):
        # set the state of rpsPlayButton back to NORMAL
        self.rpsPlayButton.configure(state = NORMAL)
        
        # set each playUpdate variable to its default values
        self.p1 = '0'
        self.t = '0'
        self.p2 = '0'
        self.trial = 1
        
        # set the text that will continue to be updated depending on the entry
        self.playUpdate(text = "Enter 'rock', 'paper', or 'scissors'", p1 = '0', t = '0', p2 = '0')
        
        # delete the entry after either the user or the computer wins 10 times/points
        self.player1Entry.delete(0, END)
        self.player2Entry.delete(0, END)
        self.player1TempLabel['text'] = '0'
        self.tTempLabel['text'] = '0'
        self.player2TempLabel['text'] = '0'
        
    # main function that runs the rpsGame
    def mutliRPSGame(self):
        # get the values from player 1 and make sure all user inputs are lowercase
        self.player1Choice = self.player1Entry.get().lower()
        
        # get the values from player 2 and make sure all user inputs are lowercase
        self.player2Choice = self.player2Entry.get().lower()
            
        # check if player 1's entries are not valid
        if (self.player1Choice != 'rock' and self.player1Choice != 'paper' and self.player1Choice != 'scissors'):
            self.win = (f"{self.player1_Name['text']}'s entry is invalid. Please enter 'rock', 'paper', or 'scissors'.")
            
            self.player1TempLabel['text'] = str(self.player1Count)
            self.tTempLabel['text'] = str(self.tieCount)
            self.player2TempLabel['text'] = str(self.player2Count)
            
        # check if player 2's entries are not valid
        elif (self.player2Choice != 'rock' and self.player2Choice != 'paper' and self.player2Choice != 'scissors'):
            self.win = (f"{self.player2_Name['text']}'s entry is invalid. Please enter 'rock', 'paper', 'scissors'.")
            
            self.player1TempLabel['text'] = str(self.player1Count)
            self.tTempLabel['text'] = str(self.tieCount)
            self.player2TempLabel['text'] = str(self.player2Count)
            
        # account for the rest of the game
        else:
            # set the outer if statement to run for as long as player1Count and player2Count != 10
            if (self.player1Count != 10 or self.player2Count != 10):
                # in order to update player1 and player2 to a random variable after each trial, even if the one of the other choices stays the same
                
                # to get both player's name entry since it is not an original variable of this class, you must use the .cget method which will obtain the string literal 
                # also because both player's names are labels
                # check if player 1 wins
                if (self.player1Choice == 'rock' and self.player2Choice == 'scissors') or (self.player1Choice == 'paper' and self.player2Choice == 'rock') or (self.player1Choice == 'scissors' and self.player2Choice == 'paper'):
                    self.win = (f"Trial {self.trial}. {self.player1_Name.cget('text')} chose " + self.player1Choice + f" and {self.player2_Name.cget('text')} chose " + self.player2Choice + "." +
                    f"\n{self.player1_Name.cget('text')} wins a point!")
                    
                    # call temporary text of cTempLabel and set it equal to the update of compCount
                    self.player1Count += 1
                    self.player1TempLabel['text'] = str(self.player1Count)
                    self.trial += 1
                
                # check if player 2 wins
                elif (self.player1Choice == 'scissors' and self.player2Choice == 'rock') or (self.player1Choice == 'rock' and self.player2Choice == 'paper') or (self.player1Choice == 'paper' and self.player2Choice == 'scissors'):
                    self.win = (f"Trial {self.trial}. {self.player1_Name.cget('text')} chose " + self.player1Choice + f" and {self.player2_Name.cget('text')} chose " + self.player2Choice + "." +
                    f"\n{self.player2_Name.cget('text')} wins a point!")
                    
                    # call the temporary text of uTempLabel and set it equal to the update of userCount
                    self.player2Count += 1
                    self.player2TempLabel['text'] = str(self.player2Count)
                    self.trial += 1
                
                elif (self.player1Choice == self.player2Choice):
                    self.win = ("It's a tie!")
                    
                    # update tieCount
                    self.tieCount += 1
                    self.tTempLabel['text'] = str(self.tieCount)
                    self.trial += 1
                
                if (self.player1Count == 10 or self.player2Count == 10):
                    if (self.player1Count == 10):
                        self.win = (f"Looks like 10 points have been reached by {self.player1_Name.cget('text')}!" +
                        f"\nThank you {self.player1_Name.cget('text')} and {self.player2_Name.cget('text')} for playing! To play again, click 'Start Game'." +
                        "\nTo go back to the menu, click 'Back to Menu'.")
                    elif (self.player2Count == 10):
                        self.win = (f"Looks like 10 points have been reached by {self.player2_Name.cget('text')}!" +
                        f"\nThank you {self.player1_Name.cget('text')} and {self.player2_Name.cget('text')} for playing! To play again, click 'Start Game'." +
                        "\nTo go back to the menu, click 'Back to Menu'.")
                        
                    self.rpsPlayButton.configure(state = DISABLED)
                    self.player2TempLabel['text'] = '0'
                    self.tTempLabel['text'] = '0'
                    self.player1TempLabel['text'] = '0'
                
        # since you are also checking to see if both entries are valid befiore playing the actual game, move this to the outer for loop so 
        # that the self.win label is updated accordingly
        
        # update the text of playUpdate by calling the text of win, cTemp, tTemp, uTemp
        self.playUpdate(self.win, self.player1TempLabel['text'], self.tTempLabel['text'], self.player2TempLabel['text'])
            
class game3Window(Toplevel):
    # method that will set the question count to 0 and initialize all the other methods that will display the content
    # and make all the other functionalities available.
    def __init__(self):
        
        super().__init__()
        self.title("Fun Fact Quiz")
        self.geometry("1050x650+170+30")
        self.config(background = '#CCCC99')
        
        # converting your json array to a python list
        with open('multiGameQuizData.json') as f:
            data = json.load(f)
            
        self.questions = (data['questions'])
        self.options = (data['options'])
        self.answers = (data['answers'])
        
        # set the number of questions to 0
        self.questionNumber = 0
        
        # these functions will be updated later as the next button is clicked
        self.displayQuizTitle()
        self.displayQuizQuestion()
        
        # set quizOptionSelected equal to Intvar() will allow the variable to hold an integer value that
        # is used for a selected option in a question
        self.quizOptionSelected = IntVar()
        
        # displays the radio button for the current questions and will display the options for the current question
        self.opt = self.radioButtons()
        
        # this function will display the options (text wise) for the current question
        self.displayQuizOptions()
        
        # number of questions
        self.dataSize = len(self.questions)
        
        # this will keep count of the number of correct answers
        self.correctAnswers = 0
        
        # keeps count of wrong answers
        self.wrongAnswers = 0
        
        self.answerLabel = ttk.Label(self, text = "Click on 'Start Quiz' to begin the quiz.", style = 'answer.TLabel')
        self.answerLabel.place(relx = 0.5, rely = 0.78, anchor = CENTER)
        
        # button that starts the quiz game overall
        self.doStartButton = ttk.Button(self, text = 'Start Quiz', command = self.startGame, style = 'nextAndBackButtons.TButton')
        self.doStartButton.place(relx = 0.17, rely = 0.89, anchor = CENTER)
        
        # the next button that allows you to move to the next question
        self.nextQuestionButton = ttk.Button(self, text = 'Next Question', state = DISABLED, command = self.nextQuestion, style = 'nextAndBackButtons.TButton')
        self.nextQuestionButton.place(relx = 0.51, rely = 0.89, anchor = CENTER)
        
        # button that allows you to go back to the menu
        self.goBacktoMenuButton = ttk.Button(self, text = 'Back to Menu', style = 'nextAndBackButtons.TButton', command = self.destroy)
        self.goBacktoMenuButton.place(relx = 0.83, rely = 0.89, anchor = CENTER)
        
        # welcome label
        self.stateLabel = ttk.Label(self, text = "Welcome to the Fun Fact Quiz Game! In this game," + 
        "\nyou will be asked random questions that vary from topic to topic. For each question" + 
        "\nyou get right, your score increases by 2 points. " +
        "\nYour quiz summary will be shown at the end of the quiz." +
        "\nTo begin the quiz, click on 'Start Quiz'." +
        "\nEnjoy playing!", style = 'stateLabel.TLabel')
        self.stateLabel.place(relx = 0.5, rely = 0.212, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and maybe entries
        self.style.configure('title.TLabel', font = ('courier', 25, 'bold'), background = '#CCCC99')
        self.style.configure('nextAndBackButtons.TButton', font = ('courier', 15, 'bold'), background = '#FF6633',
        foreground = 'black', width = 14)
        self.style.configure('question.TLabel', font = ('courier', 14, 'bold'), background = '#CCCC99', width = 72)
        self.style.configure('stateLabel.TLabel', font = ('courier', 13, 'bold'), background = '#CCCC99',
        borderwidth = 2, width = 66, height = 6, relief = SOLID)
        self.style.configure('answer.TLabel', font = ('courier', 14, 'bold'), background = '#CCCC99')
        self.style.configure('radio.TRadiobutton', font = ('courier', 13, 'bold'))
        
        # create json file that will holds your questions and answers for the quiz
        # they will hold name/value pairs and contain an array of values

        '''
        To create this Fun Fact Quiz Game:
        1. Create your json file that holds your questions, answers and options for the quiz.
        Problem Encountered: json file would not load with error message as: "No such file or directory" so to make it work, create the json file
        outside of the Python File folder.
        2. Import modules: tkinter and json
        3. Convert your json array to your python list
        4. Create the main variables and functions for your quiz program
        '''
        
    # function that updates the answer label
    def updateAnswer(self, text):
        self.answerLabel.configure(text = text)
        
    # function that will start the game once 'Start Game' is clicked
    def startGame(self):
        # set the state of next question to normal
        self.nextQuestionButton.configure(state = NORMAL)
        
        # set the text that will continue to be updated depending on the radio button chosen
        self.updateAnswer(text = "Choose your answer and then click the 'Next Question' button")
        
    # this function will display the quiz result
    # it will count the number of correct answers and wrong answers, which will then be displayed at the end in a message box
    def displayQuizResult(self):
        # calculate the number of wrong answers
        wrongAnswers = self.dataSize - self.correctAnswers
        correctAnswers = (f"Correct Answers: {self.correctAnswers}")
        wrong = (f"Wrong Answers: {wrongAnswers}")
        
        # calculate the score percentage of correct answers
        totalScore = int((self.correctAnswers / self.dataSize) * 100)
        quizResult = (f"Total Score: {totalScore}%")
        
        # messagebox that will display the result
        # mb.showinfo("Quiz Summary", f"{quizResult} \n{correctAnswers} \n{wrong}")
        
        # create a new window that will simply display the test results
        quizResultWindow = tk.Toplevel(self)
        quizResultWindow.title("Quiz Result Display")
        quizResultWindow.geometry("400x300")
        quizResultWindow.configure()
        
        # create style object
        style = ttk.Style(self)
        
        style.configure("quizWindowTitle.TLabel", font = ('courier', 23, 'bold'), background = '#e4ee98')
        style.configure("quizCorrectAnswers.TLabel", font = ("courier", 15, "bold"), background = '#e4ee98')
        style.configure("quizWrongAnswers.TLabel", font = ("courier", 15, "bold"), background = '#e4ee98')
        style.configure("quizScoreResult.TLabel", font = ("courier", 18, "bold"), background = '#e4ee98')
        style.configure("quizCloseButton", font = ("courier", 15, "bold"), background = "white", foreground = "black")
        
        # labels that will display each result
        windowTitle = ttk.Label(quizResultWindow, text = "Quiz Result", style = "quizWindowTitle.TLabel")
        windowTitle.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        correctAnswerResult = ttk.Label(quizResultWindow, text = f"{correctAnswers}", style = "quizCorrectAnswers.TLabel")
        correctAnswerResult.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        
        wrongAnswerResult = ttk.Label(quizResultWindow, text = f"{wrong}", style = "quizWrongAnswers.TLabel")
        wrongAnswerResult.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        
        totalScoreResult = ttk.Label(quizResultWindow, text = f"{quizResult}", style = "quizScoreResult.TLabel")
        totalScoreResult.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        
        # button that will close the result window as well as the game window
        closeButton = ttk.Buttons(quizResultWindow, text = "Exit Window", command = quizResultWindow.destroy, style = "quizCloseButton.TButton")
        closeButton.place(relx = 0.5, rely = 0.85, relheight = 0.03, anchor = CENTER)
        
    # this function will check the answer after the next button is clicked
    def checkAnswer(self, questionNumber):
        # check if the selected option is correct
        if (self.quizOptionSelected.get() == self.answers[questionNumber]):
            # update the text of updateAnswer by calling the text of answerCorrect
            self.answerCorrect = "Your answer was correct!"
        
        # check if the user chooses the incorrect answer
        else:
            self.answerCorrect = "Sorry, your answer was incorrect."
            
        # update the text of updateAnswer
        self.updateAnswer(self.answerCorrect)
        
    # this function will check the answer of the current question by calling checkAnswer() and questionNumber.
    # if the question is correct, the user's correctAnswer score will increase by 2 and then increase the question number by 1.
    # if it's the last question, it calls the displayQuizResult() function which will show the message box.
    # otherwise, the next question will be shown.
    def nextQuestion(self):
        # check to see if the user selected an option
        if (self.quizOptionSelected.get() == 0):
            # if an option does not get selected, display a message notifying the user of that
            self.updateAnswer("You did not select an answer choice. Please select one or you won't be \nable to move to the next question.")
            return
        
        # check if the answer is correct
        if (self.checkAnswer(self.questionNumber)):
            # if the answer is correct, correctAnswer count will be incremented by 2
            self.correctAnswers += 2
    
        # the next question will be moved to by incrementing the questionNumber counter
        self.questionNumber += 1
        
        # this will check if the questionNumber size is equal to the dataSize
        if (self.questionNumber == self.dataSize):
            # if it is correct, then it will display the quiz score
            self.displayQuizResult()
            
            # that window will then be destroyed
            self.destroy()
            
        else:
            # otherwise, show the next question
            self.displayQuizQuestion()
            self.displayQuizOptions()
            
    # this function will deselect the radio button on the screen
    # it will then be used to display the options available for the current question which will be
    # obtained through the question number and updates each of the options for the current question of 
    # the radio button
    def displayQuizOptions(self):
        
        val = 0
        # this will deselect the options
        self.quizOptionSelected.set(0)
        
        # this will loop over the options to be displayed for the text of the radio buttons
        for option in self.options[self.questionNumber]:
            self.opt[val]['text'] = option
            val += 1
            
    # this function will show the current question on the screen
    def displayQuizQuestion(self):
        # set the question properties
        questionNumber = ttk.Label(self, text = self.questions[self.questionNumber], style = 'question.TLabel')
        questionNumber.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        
    # this function will display the quiz title
    def displayQuizTitle(self):
        # title label
        factTitleLabel = ttk.Label(self, text = 'Fun Fact Game', style = 'title.TLabel')
        factTitleLabel.place(relx = 0.5, rely = 0.08, anchor = CENTER)
        
    # this function will show the radio buttons to select the question on the screen at the specified position.
    # it will also return a list of the radio buttons which are later used to add the quiz options to them
    def radioButtons(self):
        # initialize the list with an empty list of options
        qList = []
        
        # this is the option of the first option
        y_pos = 0.4
        
        # add the options to the list
        while len(qList) < 4:
            # set the radio button properties
            radioBtn = ttk.Radiobutton(self, text = " ", variable = self.quizOptionSelected, value = len(qList) + 1, style = 'radio.TRadiobutton')
            # radioBtn.configure(state = DISABLED)
            
            # add the button to the list
            qList.append(radioBtn)
            
            # place the button
            radioBtn.place(relx = 0.1, rely = y_pos)
            # increment the y_pos by 0.09
            y_pos += 0.09
            
        # return the radio buttons
        return qList
    
# this function displays the directions for the fourth games: Create a Shape
class game4Window(tk.Toplevel):
    
    def __init__(self, main_window):
        
        super().__init__()
        self.title("Create a Shape")
        self.geometry("800x640+270+20")
        self.config(background = '#7BE396')
        
        self.main_window = main_window
        
        # title label
        self.canvasTitle = ttk.Label(self, text = "Create a Shape", style = 'canvasT.TLabel')
        self.canvasTitle.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that prompts the user to click on start game and will get updated as the user plays
        self.starts = ttk.Label(self, text = "Click on Start Game", style = 'canvasStart.TLabel')
        self.starts.place(relx = 0.5, rely = 0.68, anchor = CENTER)
        
        # label that gives the user directions
        self.welcomeLabel = ttk.Label(self, text = ("Welcome to the 'Create a Shape' game!" + 
        "\nIn this game, you will be prompted to click 'Start Game' which will lead" +
        "\nyou to a new page where you will be presented 6 buttons that will allow" +
        "\nyou to perform 5 different functions. The buttons will be: Create a" +
        "\nRectangle, Create a Circle, Create a Line, Create a Polygon, Move a Shape," + 
        "\nand Delete a Shape. Those last two functions will be specific for each" +
        "\nshape. You can exit the game at any time using the 'Back to Menu'" +
        "\nbutton or play again using the 'Start Game' button. \nEnjoy Playing!"), style = 'canvasWelcomeLabel.TLabel')
        self.welcomeLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        
        # button to open a new page
        self.canvasStartButton = ttk.Button(self, text = "Start Game", style = 'canvasGameButtons.TButton', command = self.open_createTheShapesCanvas)
        self.canvasStartButton.place(relx = 0.35, rely = 0.82, anchor = CENTER)
        
        # button to go back to the menu
        self.canvasBacktoMenu = ttk.Button(self, text = "Back to Menu", style = 'canvasGameButtons.TButton', command = self.destroy)
        self.canvasBacktoMenu.place(relx = 0.65, rely = 0.82, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # styles for labels, buttons, and entries
        self.style.configure('canvasT.TLabel', font = ('courier', 25, 'bold'), background = '#7BE396')
        self.style.configure('canvasGameButtons.TButton', font = ('courier', 13, 'bold'), background = '#88AFC7', foreground = 'black', width = 14)
        self.style.configure('canvasStart.TLabel', font = ('courier', 14, 'bold'), background = '#7BE396')
        self.style.configure('canvasWelcomeLabel.TLabel', font = ('courier', 12, 'bold'), background = '#7BE396', foreground = 'black', borderwidth = 2, width = 74, 
        height = 5, relief = SOLID)
        
    def open_createTheShapesCanvas(self):
        # hides the main window
        self.withdraw()
        createTheShapesCanvas(self)
        
# this class will open a new window that will display the buttons
class createTheShapesCanvas(tk.Toplevel):
    
    def __init__(self, game4_window):
        
        super().__init__()
        
        self.title("Canvas Window")
        self.geometry("1000x640+210+20")
        self.config(background = '#7BE396')
        
        self.game4_window = game4_window
        
        # create the canvas
        self.canvas = tk.Canvas(self, width = 1000, height = 640, background = '#7BE396')
        # don't use .place() use .pack() instead or else you will get a Tk_GetPixmap Error
        self.canvas.pack()
        
        # create style object
        style = ttk.Style()
        
        style.configure('canvasGameButtons.TButton', font = ('courier', 11, 'bold'), background = '#C0B4F3', foreground = 'black', width = 18)
        style.configure('canvasActionButtons.TButton', font = ('courier', 11, 'bold'), background = '#9380E8', foreground = 'black', width = 18)
        style.configure('canvasTitle.TLabel', font = ('courier', 13, 'bold'), background = '#7BE396')
        style.configure('canvasBackButton.TButton', font = ('courier', 13, 'bold'), background = '#88AFC7', foreground = 'black', width = 14)
        
        # title label
        canvasTitle = ttk.Label(self, text = "Click any of these buttons to create, move, or delete the designated shape", style = 'canvasTitle.TLabel')
        canvasTitle.place(relx = 0.5, rely = 0.06, anchor = CENTER)
        
        # button to go back to the menu
        canvasBacktoMenu = ttk.Button(self, text = "Back to Menu", style = 'canvasBackButton.TButton', command = self.destroy)
        canvasBacktoMenu.place(relx = 0.5, rely = 0.92, anchor = CENTER)
        
        # button to create a rectangle
        # relx = 0.87 or 0.12
        createRectangle = ttk.Button(self, text = "Create a Rectangle", style = 'canvasGameButtons.TButton', command = self.createRectangle_Canvas)
        createRectangle.place(relx = 0.12, rely = 0.17, anchor = CENTER)
        
        # button to move a rectangle
        moveRectangle = ttk.Button(self, text = "Move Rectangle", style = 'canvasActionButtons.TButton', command = self.moveRectangle_Canvas)
        moveRectangle.place(relx = 0.12, rely = 0.22, anchor = CENTER)
        
        # button to create a circle
        createCircle = ttk.Button(self, text = "Create a Circle", style = 'canvasGameButtons.TButton', command = self.createCircle_Canvas)
        createCircle.place(relx = 0.12, rely = 0.27, anchor = CENTER)
        
        # button to move a circle
        moveCircle = ttk.Button(self, text = "Move Circle", style = 'canvasActionButtons.TButton', command = self.moveCircle_Canvas)
        moveCircle.place(relx = 0.12, rely = 0.32, anchor = CENTER)
        
        # button to create a line
        createLine = ttk.Button(self, text = "Create a Line", style = 'canvasGameButtons.TButton', command = self.createLine_Canvas)
        createLine.place(relx = 0.12, rely = 0.37, anchor = CENTER)
        
        # button to move a line
        moveLine = ttk.Button(self, text = "Move Line", style = 'canvasActionButtons.TButton', command = '')
        moveLine.place(relx = 0.12, rely = 0.42, anchor = CENTER)
        
        # button to create a polygon
        createPolygon = ttk.Button(self, text = "Create a Polygon", style = 'canvasGameButtons.TButton', command = '')
        createPolygon.place(relx = 0.12, rely = 0.47, anchor = CENTER)
        
        # button to move a polygon
        movePolygon = ttk.Button(self, text = "Move Polygon", style = 'canvasActionButtons.TButton', command = '')
        movePolygon.place(relx = 0.12, rely = 0.52, anchor = CENTER)
        
        # button to delete a shape
        
    # function that will create a rectangle
    def createRectangle_Canvas(self):
        # top left - x,y - top right x,y
        self.rectangle = self.canvas.create_rectangle(350, 350, 450, 400, outline = 'black', width = 2, fill = '#7ECED6')
        
    # function to move the rectangle
    def moveRectangle_Canvas(self):
        # x,y
        self.canvas.move(self.rectangle, 50, 15)
        # moves the rectangle automatically after 50ms (0.050s)
        # self.canvas.after(50, self.moveRectangle_Canvas)
        
    # function that will create a circle
    def createCircle_Canvas(self):
        self.circle = self.canvas.create_oval(500, 400, 600, 300, outline = 'black', width = 2, fill = '#7ECED6')
        
    # function to move the circle
    def moveCircle_Canvas(self):
        self.canvas.move(self.circle, 25, 15)
        
    # function to create a line
    def createLine_Canvas(self):
        self.line = self.canvas.create_line(300, 500, 600, 450, fill = 'black', width = 4)
        
    # function to move the line
    def moveLine_Canvas(self):
        self.canvas.move(self.line, 15, 5)
        
        
# runs the mainWindow
if __name__ == "__main__":
    master = mainWindow()
    master.mainloop()