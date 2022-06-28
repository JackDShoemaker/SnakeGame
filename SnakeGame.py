import tkinter as tk
import threading 
import multiprocessing
import time
import random
#x bound 0-580
#y bound 0-580
class SnakeGame():
    currMomentum = "none"
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.configure(bg = "black")
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        self.window.bind("<Left>", self.momentum)
        self.window.bind("<Right>", self.momentum)
        self.window.bind("<Up>", self.momentum)
        self.window.bind("<Down>", self.momentum)
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
    
    def left(self, event):
        if(self.snake.winfo_x() - 10 <= 0):
            self.endGame(self)
        else: 
            self.snake.place(x= self.snake.winfo_x() - 10)

    def right (self, event):
        if(self.snake.winfo_x() + 10 >= 580):
            self.endGame(self)
        else:
            self.snake.place(x= self.snake.winfo_x() + 10)

    def up(self,event):
        if(self.snake.winfo_y() - 10 <= 0):
            self.endGame(self)
        else:
            self.snake.place(y= self.snake.winfo_y() - 10)

    def down(self,event):
        if(self.snake.winfo_y() + 10 >= 570):
            self.endGame(self)
        else:
            self.snake.place(y= self.snake.winfo_y() + 10)
    def momentum(self, event):
        pass 
    def endGame(self, event):
        pass
run = SnakeGame()