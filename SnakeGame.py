import tkinter as tk
import random

class SnakeGame():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.configure(bg = "black")
        self.window.geometry("600x600")
        self.window.resizable(False, False)

        self.makeArea(self)
        self.window.mainloop()

    def makeArea(self, x):
        for i in range(300):
            self.window.columnconfigure(i, weight =1)
            self.window.rowconfigure(i, weight =1)
        #add snake character
        self.snake = tk.Frame(self.window, bg = "white", width = 20, height = 20)
        self.snake.grid(column =50, row =150)
        
        #add apple
        self.apple = tk.Frame(self.window, bg ="red", width = 20, height =20)
        self.apple.grid(column = 250, row =150)
        
run = SnakeGame()