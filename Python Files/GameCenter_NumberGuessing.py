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
import random
from random import randint
import json
from PIL import ImageTk, Image

class NumberGuessingGame(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        self.title("Number Guessing")
        self.geometry("850x650+290+30")
        self.config(background = "#99FFCC")
        
        # string data that is able to be retrieved
        self.sVar = StringVar()
        # count the number of trials used
        self.trial = 1
        
        # total number of trials
        self.total = 5
        
        # range of numbers to choose from
        self.randNum = randint(0, 100)
        
        # labels, entries, and buttons from the numberGuessingGame
        # title label
        self.nLabel = ttk.Label(self, text = "Number Guessing", style = "g1.TLabel")
        self.nLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that gets updated based on the number entered by the user
        self.startLabel = ttk.Label(self, text = "Click on Start Game", style = "start.TLabel")
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
        
        self.style.theme_use("alt")
        
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
        self.style.map("Main.TButton", background = [("active", "#d3d3d3")])
    
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

if __name__ == "__main__":
    master = NumberGuessingGame()
    master.mainloop()
