from os import curdir
import tkinter as tk
import threading 
import multiprocessing
import time
import random
#x bound 0-580
#y bound 0-580
class SnakeGame():
    currMomentum = "none"
    oppositeDir = [("Up", "Down"), ("Right", "Left"), ("Down", "Up"), ("Left", "Right")]
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.configure(bg = "black")
        self.window.geometry("600x600")
        self.window.resizable(False, False)

        self.window.bind("<Left>", self.changeMomentum)
        self.window.bind("<Right>", self.changeMomentum)
        self.window.bind("<Up>", self.changeMomentum)
        self.window.bind("<Down>", self.changeMomentum)
        self.makeArea(self)
        #need to add after for momentum and movement 
        self.window.mainloop()

    def makeArea(self, x):
        #add snake character head
        self.snake = tk.Frame(self.window, bg = "white", width = 20, height = 20)
        self.snake.place(x =580, y =580)
        
        #add apple
        self.apple = tk.Frame(self.window, bg ="red", width = 20, height =20)
        self.apple.place(x = 250, y =150)
    
    def left(self):
        if(self.snake.winfo_x() - 10 <= 0):
            self.endGame(self)
        else: 
            self.snake.place(x= self.snake.winfo_x() - 5)

    def right (self):
        if(self.snake.winfo_x() + 10 >= 570):
            self.endGame(self)
        else:
            self.snake.place(x= self.snake.winfo_x() + 5)

    def up(self):
        if(self.snake.winfo_y() - 10 <= 0):
            self.endGame(self)
        else:
            self.snake.place(y= self.snake.winfo_y() - 5)

    def down(self):
        if(self.snake.winfo_y() + 10 >= 570):
            self.endGame(self)
        else:
            self.snake.place(y= self.snake.winfo_y() + 5)
    #contiunously checks for input change
    def changeMomentum(self, event):
        if(self.currMomentum == "none"):
            self.currMomentum = event.keysym
            self.momentum()
        elif(self.currMomentum != event.keysym and self.oppositeDir.count((event.keysym, self.currMomentum))==0):
            self.currMomentum = event.keysym
        else:
            pass

    def momentum(self):
        if(self.currMomentum == "Left"):
            self.left()
        elif(self.currMomentum == "Right"):
            self.right()
        elif(self.currMomentum == "Up"):
            self.up()
        elif(self.currMomentum == "Down"):
            self.down()
        self.window.after(20, self.momentum)
    def endGame(self, event):
        pass
run = SnakeGame()