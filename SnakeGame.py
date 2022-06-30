from ast import Pass
import tkinter as tk
import time
import random
#x bound 0-580
#y bound 0-580
class SnakeGame():
    currDir = "none"
    xVelocity = 0
    yVelocity = 0
    oppositeDir = [("Up", "Down"), ("Right", "Left"), ("Down", "Up"), ("Left", "Right")]
    snakeBody = []
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.configure(bg = "black")
        self.window.geometry("600x600")
        self.window.resizable(False, False)

        self.window.bind("<Left>", self.changeVelocity)
        self.window.bind("<Right>", self.changeVelocity)
        self.window.bind("<Up>", self.changeVelocity)
        self.window.bind("<Down>", self.changeVelocity)
        self.makeArea(self)
        #need to add after for momentum and movement 
        self.window.mainloop()

    def makeArea(self, x):
        #add snake character head
        self.snakeHead = tk.Frame(self.window, bg = "white", width = 20, height = 20)
        self.snakeHead.place(x =100, y =140)
        
        #add apple
        self.apple = tk.Frame(self.window, bg ="red", width = 20, height =20)
        self.apple.place(x = 240, y =140)
  
    #changes currDir and calls moveHelp after first input
    def changeVelocity(self, event):
        if(self.currDir == "none"):
            self.currDir = event.keysym
            self.moveHelp()
        elif(self.currDir != event.keysym and self.oppositeDir.count((event.keysym, self.currDir))==0):
            self.currDir = event.keysym
        else:
            pass
    #helper meant for changing velocity value
    def moveHelp(self):
        if(self.currDir == "Left"):
            self.xVelocity = -20
            self.yVelocity = 0
        elif(self.currDir == "Right"):
            self.xVelocity = 20
            self.yVelocity = 0
        elif(self.currDir == "Up"):
            self.xVelocity = 0
            self.yVelocity = -20
        elif(self.currDir == "Down"):
            self.xVelocity = 0
            self.yVelocity = 20
        self.moveHead()
        self.window.after(100, self.moveHelp)
    #moves the snake head
    def moveHead(self):
        if(self.snakeHead.winfo_y() + 10 >= 570 or self.snakeHead.winfo_x() + 10 >= 570):
            self.endGame()
        elif(self.snakeHead.winfo_y() - 10 <= 0 or self.snakeHead.winfo_x() - 10 <= 0):
            self.endGame()
        else:
            self.snakeHead.place(y= self.snakeHead.winfo_y() + self.yVelocity)
            self.snakeHead.place(x= self.snakeHead.winfo_x() + self.xVelocity)
            self.moveBody()
            self.updateApple()
    def moveBody(self):
        pass
    def updateApple(self):
        if(self.snakeHead.winfo_x() == self.apple.winfo_x() and self.snakeHead.winfo_y() == self.apple.winfo_y()): 
            self.incSnake()
            pass

    def incSnake(self):
        self.snakeBody.append(tk.Frame(self.window, bg = "white", width = 20, height = 20))
        if(len(self.snakeBody) == 1):
            if(self.currDir != "Up" or self.currDir != "Down"):
                if(self.currDir == "Right"):
                    self.snakeBody[0].place(x= self.snakeHead.winfo_x() - 20, y = self.snakeHead.winfo_y())
                else:
                     self.snakeBody[0].place(x= self.snakeHead.winfo_x() + 20, y = self.snakeHead.winfo_y())
            else: 
                if(self.currDir == "Down"):
                    self.snakeBody[0].place(x= self.snakeHead.winfo_x(), y = self.snakeHead.winfo_y()+20)
                else:
                    self.snakeBody[0].place(x= self.snakeHead.winfo_x(), y = self.snakeHead.winfo_y()-20)
        else:
            if(self.currDir != "Up" or self.currDir != "Down"):
                if(self.currDir == "Right"):
                    self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x() - 20, y = self.snakeBody[-2].winfo_y())
                else:
                     self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x() + 20, y = self.snakeBody[-2].winfo_y())
            else: 
                if(self.currDir == "Down"):
                    self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x(), y = self.snakeBody[-2].winfo_y()+20)
                else:
                    self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x(), y = self.snakeBody[-2].winfo_y()-20)

    def endGame(self):
        pass
run = SnakeGame()