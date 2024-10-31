'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: GameCenter_RockPaperScissors_SinglePlayer.py
Description: Single Player game for the full Rock, Paper, Scissors game.
'''

# import needed modules
from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

# class for the name entry
class singlePlayerNameEntries(tk.Tk):
    
    def __init__(self):
    
        super().__init__()
        
        # attributes
        self.geometry("1000x650+200+20")
        self.title("Rock, Paper, Scissors: Single Player Entry")
        self.config(background = "#56D995")
        
        # variable to receive the string name input
        self.player1SVar = StringVar()
        
        # call the entries page function to display the player's name
        self.singleEntryPage()
        
        # style
        self.style = ttk.Style(self)
        self.style.theme_use("alt")
        
        self.style.configure("singleTitle.TLabel", font = ("courier", 22, "bold"), background = "#56D995")
        self.style.configure("player1.TLabel", font = ("courier", 15, "bold"), background = "#56D995")
        self.style.configure("player1.TEntry", font = ("courier", 20), width = 15)
        self.style.configure("playRPS.TButton", font = ("courier", 15, "bold"), width = 15, background = "#A556D9", foreground = "black")
        self.style.configure("singleWelcomeLabel.TLabel", font = ("courier", 13, "bold"), background = "#56D995", borderwidth = 2, width = 66,
        height = 7, relief = SOLID)
        
    # function to accept the player's name entry
    def singleEntryPage(self):
        # title
        self.singleRPSLabel = ttk.Label(self, text = "Rock, Paper, Scissors: Single Player Entry", style = "singleTitle.TLabel")
        self.singleRPSLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label and entry for player 1
        self.singlePlayer1NameLabel = ttk.Label(self, text = "Enter Name for User", style = "player1.TLabel")
        self.singlePlayer1NameLabel.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        
        self.singlePlayerNameEntry = ttk.Entry(self, style = "player1.TEntry", textvariable = self.player1SVar, font = ("Courier", 20))
        self.singlePlayerNameEntry.place(relx = 0.5, rely = 0.55, relheight = 0.05, anchor = CENTER)
        
        # button that leads to the game page
        self.playSingleRPSGame = ttk.Button(self, text = "Play Game", style = "playRPS.TButton", command = self.displaySinglePlayerRPSGame)
        self.playSingleRPSGame.place(relx = 0.3, rely = 0.89, anchor = CENTER)
        
        # bind the enter key to that same button
        self.bind("<Return>", self.displaySinglePlayerRPSGame)
        
        # back to the menu (rps)
        self.singleBackToMenu = ttk.Button(self, text = "Back to Menu", style = "playRPS.TButton", command = self.destroy)
        self.singleBackToMenu.place(relx = 0.7, rely = 0.89, anchor = CENTER)
        
        self.welcome = ttk.Label(self, text = "Welcome to 'Rock, Paper, Scissors'!" +
        "\nFirst, input your name. Once that is done, click the" +
        "\n'Play Game' button, which will then lead you to the rock, paper," +
        "\nscissors game.", style = "singleWelcomeLabel.TLabel")
        self.welcome.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
    # function to display the user's name and play the game
    def displaySinglePlayerRPSGame(self, event = None):
        
        # get the entries of the user's name
        player1Name = self.player1SVar.get()
        
        # if the user entered their name
        if (player1Name):
            # destroy the current page
            self.withdraw()
            # open the single player game
            game2SinglePlayerWindow(self, player1Name)
        
        # if the user hasn't entered their name
        else:
            # frame
            self.fieldFrame = ttk.Frame(self, borderwidth = 10, relief = SOLID, style = "CheckFrameWidget.TFrame")
            # self.fieldFrame.place(relx = 0.37, rely = 0.32, relheight = 0.38, relwidth = 0.5)
            self.fieldFrame.place(relx = 0.1, rely = 0.32, relheight = 0.38, relwidth = 0.8)
            
            # warning label
            self.fieldFrameLabel = ttk.Label(self.fieldFrame, text = "Please enter your name. \nYou cannot continue to the game without it.", style = "CheckFrameLabelWidget.TLabel")
            # self.fieldFrameLabel.place(relx = 0.5, rely = 0.43, anchor = CENTER)
            self.fieldFrameLabel.place(relx = 0.5, rely = 0.43, anchor = CENTER)
            
            # exit button
            self.fieldFrameExitButton = ttk.Button(self.fieldFrame, text = "Exit", style = "CheckFrameButton.TButton", command = self.fieldFrame.destroy)
            # self.fieldFrameExitButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)
            self.fieldFrameExitButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)
            
            # bind the backspace button to the function that exits the fieldFrame
            # self.bind("<BackSpace>", self.backspaceExit)
            
            self.frameStyle()
            
    # function that binds the backspace button to destroying a window
    # def backspaceExit(self):
        # destroy the frame, not the window
        # self.fieldFrame.destroy()
            
    # function for the error frame styles
    def frameStyle(self):
        # style
        self.style = ttk.Style(self)
        self.style.theme_use("alt")
        
        self.style.configure("CheckFrameWidget.TFrame", background = "#328421")
        self.style.configure("CheckFrameButton.TButton", background = "#E6B930", width = 20, font = ("courier", 12, "bold"))
        self.style.configure("CheckFrameLabelWidget.TLabel", background = "#328421", font = ("Courier", 18, "bold"))
    
# class that plays the single player game
class game2SinglePlayerWindow(tk.Toplevel):
    
    def __init__(self, root, player1Name):
        
        super().__init__()
        self.title("Rock, Paper, Scissors: Single Player")
        self.geometry("880x670+270+15")
        self.config(background = "#58AD38")
        self.win = "Click 'rock', 'paper', or 'scissors'."
        
        self.root = root
        
        self.p1SVar = StringVar()
        
        # variables
        self.userCount = 0
        self.compCount = 0
        self.tieCount = 0
        
        self.trial = 1
        
        self.choices = ["rock", "paper", "scissors"]
        
        # loads the image for rock
        rock_image = r"C:\Users\akiny\OneDrive\Code Files\Python Files\GameCenterProgram\r1pic.png"
        rock_img = Image.open(rock_image)
        rock_img = rock_img.resize((65, 65)) # adjust the size if needed
        self.rock_photo = ImageTk.PhotoImage(rock_img)
        
        # loads the image for paper
        paper_image = r"C:\Users\akiny\OneDrive\Code Files\Python Files\GameCenterProgram\p1pic.png"
        paper_img = Image.open(paper_image)
        paper_img = paper_img.resize((65, 65))
        self.paper_photo = ImageTk.PhotoImage(paper_img)
        
        # loads image for scissors
        scissors_image = r"C:\Users\akiny\OneDrive\Code Files\Python Files\GameCenterProgram\s1pic.png"
        scissors_img = Image.open(scissors_image)
        scissors_img = scissors_img.resize((65, 65))
        self.scissors_photo = ImageTk.PhotoImage(scissors_img)

        # labels, entries, and buttons
        # title
        self.singleRPSLabel = ttk.Label(self, text = "Rock, Paper, Scissors: Single Player", style = "singleTitle.TLabel")
        self.singleRPSLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that updates with the results of each round
        self.resultPlayLabel = ttk.Label(self, text = "Click on Start Game", style = "singleGameLabels.TLabel")
        self.resultPlayLabel.place(relx = 0.5, rely = 0.63, anchor = CENTER)
        
        # represent the user
        self.uLabel = ttk.Label(self, text = f'{player1Name}', style = 'singleCount.TLabel')
        self.uLabel.place(relx = 0.32, rely = 0.74, anchor = CENTER)
        
        # temporary label for user's score
        self.uTempLabel = ttk.Label(self, text = '0', style = 'singleGameLabels.TLabel')
        self.uTempLabel.place(relx = 0.32, rely = 0.82, anchor = CENTER)
        
        # represents the tie 
        self.tLabel = ttk.Label(self, text = '   Tie    ', style = 'singleCount.TLabel')
        self.tLabel.place(relx = 0.5, rely = 0.74, anchor = CENTER)
        
        # temporary label for the tie score
        self.tTempLabel = ttk.Label(self, text = '0', style = 'singleGameLabels.TLabel')
        self.tTempLabel.place(relx = 0.5, rely = 0.82, anchor = CENTER)
        
        # represents the computer 
        self.cLabel = ttk.Label(self, text = ' Computer  ', style = 'singleCount.TLabel')
        self.cLabel.place(relx = 0.68, rely = 0.74, anchor = CENTER)
        
        # temporary label for computer's score
        self.cTempLabel = ttk.Label(self, text = '0', style = 'singleGameLabels.TLabel')
        self.cTempLabel.place(relx = 0.68, rely = 0.82, anchor = CENTER)
        
        # button that allows you to begin the game and enables, rock, paper, and scissors
        self.singleStartGameButton = ttk.Button(self, text = 'Start Game', style = 'singleUseButtons.TButton', command = self.rpsStart)
        self.singleStartGameButton.place(relx = 0.25, rely = 0.92, anchor = CENTER)
        
        # button that resets the game
        self.resetGameButton = ttk.Button(self, text = "Reset Game", style = "singleUseButtons.TButton", command = self.resetValues)
        self.resetGameButton.place(relx = 0.5, rely = 0.92, anchor = CENTER)
        
        # button that allows you to exit the game2Window and return to the main menu
        self.backMenuButton = ttk.Button(self, text = 'Back to Menu', style = 'singleUseButtons.TButton', command = self.destroy)
        self.backMenuButton.place(relx = 0.75, rely = 0.92, anchor = CENTER)
        
        # buttons for each separate choice
        self.rockButton = ttk.Button(self, image = self.rock_photo, style = "rpsGameButtons.TButton", state = DISABLED, command = lambda: self.playGameRound("rock"), compound = tk.LEFT)
        self.rockButton.place(relx = 0.34, rely = 0.5, anchor = CENTER)
        
        self.paperButton = ttk.Button(self, image = self.paper_photo, style = "rpsGameButtons.TButton", state = DISABLED, command = lambda: self.playGameRound("paper"))
        self.paperButton.place(relx = 0.52, rely = 0.5, anchor = CENTER)
        
        self.scissorsButton = ttk.Button(self, text = "Scissors", image = self.scissors_photo, style = "rpsGameButtons.TButton", state = DISABLED, command = lambda: self.playGameRound("scissors"))
        self.scissorsButton.place(relx = 0.68, rely = 0.5, anchor = CENTER)
        
        self.userMoveLabel = ttk.Label(self, text = f"{player1Name}'s Move", style = "moveLabel.TLabel")
        self.userMoveLabel.place(relx = 0.13, rely = 0.5, anchor = CENTER)
        
        # the user's move will be appended to this text box
        self.userMoveHistory = Text(self, height = 12, width = 20)
        self.userMoveHistory.place(relx = 0.13, rely = 0.7, anchor = CENTER)
        
        self.computerMoveLabel = ttk.Label(self, text = "Computer's Move", style = "moveLabel.TLabel")
        self.computerMoveLabel.place(relx = 0.87, rely = 0.5, anchor = CENTER)
        
        # the computer's move will be appended to this text box
        self.computerMoveHistory = Text(self, height = 12, width = 20)
        self.computerMoveHistory.place(relx = 0.87, rely = 0.7, anchor = CENTER)
        
        # welcomeLabel that lists the directions for the game
        self.welcomesingleRPSLabel = ttk.Label(self, text = "Welcome to 'Rock, Paper, Scissors: Single Player'!" +
            "\nIn this game, you will play against the computer. If either" + 
            "\nyou or the computer gets 5 points, the game will end and" +
            "\nyou will have the option to play again." 
            "\nEnjoy playing!", style = 'welcomeLabel.TLabel')
        self.welcomesingleRPSLabel.place(relx = 0.5, rely = 0.25, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        self.style.theme_use("alt")
        
        # style for labels, buttons, and entries
        self.style.configure('singleTitle.TLabel', font = ('courier', 25, 'bold'), background = '#58AD38')
        self.style.configure('singleCount.TLabel', font = ('courier', 13, 'bold'), background = '#58AD38', foreground = 'black',
        borderwidth = 2, width = 10, height = 2, relief = SOLID)
        self.style.configure('singleGameLabels.TLabel', font = ('courier', 10, 'bold'), background = '#58AD38')
        self.style.configure('singleUseButtons.TButton', font = ('courier', 15, 'bold'), background = '#33EFF2', foreground = 'black',
        width = 12)
        self.style.configure('gameEntry.TEntry', font = ('courier', 15), width = 15)
        self.style.configure('welcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#58AD38', borderwidth = 2, width = 68,
        height = 7, relief = SOLID)
        self.style.configure("moveLabel.TLabel", font = ("courier", 13, "bold"), width = 16, background = "#58AD38", borderwidth = 2,
        height = 70, relief = SOLID)
        self.style.configure("rpsGameButtons.TButton", font = ("courier", 10, "bold"), background = "#A38DD1", foreground = "black",
        width = 3)
        self.style.map("Main.TButton", background = [("active", "#d3d3d3")])
    
    # function that updates each label
    def playUpdate(self, text, u, t, c):
        self.resultPlayLabel.configure(text = text)
        self.uTempLabel.configure(text = u)
        self.tTempLabel.configure(text = t)
        self.cTempLabel.configure(text = c)
        
    # function that enables and disables the game buttons based on who's turn it is
    def rpsStart(self):
        # player 1's (user) turn comes first - state of the game buttons are normal, but the play button for the computer is disabled
        self.rockButton.config(state = NORMAL)
        self.paperButton.config(state = NORMAL)
        self.scissorsButton.config(state = NORMAL)
        self.singleStartGameButton.config(state = DISABLED)
        
        # ask the user (player 1) to press a button
        self.resultPlayLabel.configure(text = "Click rock, paper, or scissors to begin playing.") 
        
        # set the scores to default - 0
        self.uTempLabel["text"] = "0"
        self.tTempLabel["text"] = "0"
        self.cTempLabel["text"] = "0"
        
    # function that clears the textboxes
    def clearTextBoxes(self):
        self.userMoveHistory.config(state = NORMAL)
        self.userMoveHistory.delete("1.0", tk.END)
        self.userMoveHistory.config(state = DISABLED)
        
        self.computerMoveHistory.config(state = NORMAL)
        self.computerMoveHistory.delete("1.0", tk.END)
        self.computerMoveHistory.config(state = DISABLED)
        
    # function that plays a round of the game by generating the computer's random move, determining the winner, 
    # displaying the results in their respective textboxes, and checking if either player has reached 5 points
    def playGameRound(self, userChoice):
        # the computer's random move
        compChoice = random.choice(self.choices)
        
        # insert the play results into the textboxes
        self.game_results = self.rpsGame(userChoice, compChoice)
        
        self.userMoveHistory.config(state = NORMAL)
        self.userMoveHistory.insert(tk.END, f"{userChoice}\n")
        self.userMoveHistory.config(state = DISABLED)
        
        self.computerMoveHistory.config(state = NORMAL)
        self.computerMoveHistory.insert(tk.END, f"{compChoice}\n")
        self.computerMoveHistory.config(state = DISABLED)
        
        # check if either player has reached 5 points yet
        if ((self.userCount == 5) or (self.compCount == 5)):
            # end the game
            self.endRPSGame()
        
    # function that plays the game
    def rpsGame(self, userChoice, compChoice):
        
        if (compChoice == userChoice):
            self.win = f"Trial {self.trial}. \nIt's a tie!"
            
            # update the tie point count
            self.tieCount += 1
            self.tTempLabel["text"] = str(self.tieCount)
            self.trial += 1
        
        # conditional statements for each possible play
        elif (compChoice == "rock" and userChoice == "scissors") or (compChoice == "paper" and userChoice == "rock") or (compChoice == "scissors" and userChoice == "paper"):
            
            self.win = (f"Trial {self.trial}. \nComputer -> " + compChoice + f".\n{self.uLabel["text"]} -> " + userChoice + "." + 
            "\nThe computer wins a point!")
            
            # update the computer point count
            self.compCount += 1
            self.cTempLabel["text"] = str(self.compCount)
            self.trial += 1
            
        else:
            self.win = (f"Trial {self.trial}. \nComputer -> " + compChoice + f".\n{self.uLabel["text"]} -> " + userChoice + "." +
            f"\n{self.uLabel["text"]} wins a point!")
            
            # update player 1's point count
            self.userCount += 1
            self.uTempLabel["text"] = str(self.userCount)
            self.trial += 1
        
        # update the result text
        self.playUpdate(self.win, self.uTempLabel["text"], self.tTempLabel["text"], self.cTempLabel["text"])
        
    # disable the play buttons
    def disablePlayButtons(self):
        self.rockButton.config(state = DISABLED)
        self.paperButton.config(state = DISABLED)
        self.scissorsButton.config(state = DISABLED)
    
    # function that ends the game
    def endRPSGame(self):
        # if the user gets 5 points
        if (self.userCount == 5):
            self.win = (f"Looks like {self.uLabel['text']} has reached 5 points, which \nmeans" +
            " the computer lost! Thank you for playing! \nPlease click 'Reset Game'." + 
            "\nOR to go back to the menu, click 'Back to Menu'.")
            
            self.disablePlayButtons()
            
        # if the computer gets 5 points
        elif (self.compCount == 5):
            self.win = (f"Looks like the computer has reached 5 points, which \nmeans" + 
            f" {self.uLabel['text']} lost! Thank you for playing! \nPlease click 'Reset Game'." +
            "\nOR to go back to the menu, click 'Back to Menu'.")
            
            self.disablePlayButtons()
            
        # update the result text
        self.playUpdate(self.win, self.uTempLabel["text"], self.tTempLabel["text"], self.cTempLabel["text"])
            
    # function to reset the values
    def resetValues(self):
        self.singleStartGameButton.configure(state = NORMAL)
        self.rockButton.configure(state = DISABLED)
        self.paperButton.configure(state = DISABLED)
        self.scissorsButton.configure(state = DISABLED)
        self.uTempLabel["text"] = 0
        self.tTempLabel["text"] = 0
        self.cTempLabel["text"] = 0
        self.clearTextBoxes()
        self.resultPlayLabel.config(text = "Click on Start Game")
        self.trial = 1
        self.userCount = 0
        self.tieCount = 0
        self.compCount = 0
            
    # function for the error frame styles
    def frameStyle(self):
        # style
        self.style = ttk.Style(self)
        self.style.theme_use("alt")
        
        self.style.configure("CheckFrameWidget.TFrame", background = "#328421")
        self.style.configure("CheckFrameButton.TButton", background = "#E6B930", width = 20, font = ("courier", 12, "bold"))
        self.style.configure("CheckFrameLabelWidget.TLabel", background = "#328421", foreground = "white", font = ("Courier", 18, "bold"))
            
if __name__ == "__main__":
    master = singlePlayerNameEntries()
    master.mainloop()
