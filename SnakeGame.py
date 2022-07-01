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
    theScore = 0
    id
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.configure(bg = "black")
        self.window.geometry("600x620")
        self.window.resizable(False, False)
        
        self.window.bind("<Left>", self.changeVelocity)
        self.window.bind("<Right>", self.changeVelocity)
        self.window.bind("<Up>", self.changeVelocity)
        self.window.bind("<Down>", self.changeVelocity)
        self.makeArea(self)
        self.window.mainloop()

    def makeArea(self, x):
        self.snakeBody.append(tk.Frame(self.window, bg = "white", width = 20, height = 20)) 
        self.snakeBody[0].place(x =100, y =140)
        self.apple = tk.Frame(self.window, bg ="red", width = 20, height =20)
        self.apple.place(x = 240, y =140)
        self.score = tk.Label(self.window, text = "Score: "+ str(self.theScore), fg = "white", bg = "black", font = ('Roboto',11))
        self.score.pack()
    #changes currDir and calls moveHelp after first input
    def changeVelocity(self, event):
        if(self.currDir == "none"):
            self.currDir = event.keysym
            self.moveHelp()
        elif(self.currDir != event.keysym and self.oppositeDir.count((event.keysym, self.currDir))==0):
            self.currDir = event.keysym
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
        self.move()
        self.id = self.window.after(80, self.moveHelp)
    #moves the snake 
    def move(self):
        if(self.snakeBody[0].winfo_y() + 20 >= 600 or self.snakeBody[0].winfo_x() + 20 >= 570):
            self.endGame()
        elif(self.snakeBody[0].winfo_y() - 20 <= 20 or self.snakeBody[0].winfo_x() - 20 <= 0):
            self.endGame()
        else:
            prevX = self.snakeBody[0].winfo_x()
            prevY = self.snakeBody[0].winfo_y()
            self.snakeBody[0].place(y= self.snakeBody[0].winfo_y() + self.yVelocity)
            self.snakeBody[0].place(x= self.snakeBody[0].winfo_x() + self.xVelocity)
            if(self.bodyCollision()):
                self.window.after_cancel(self.id)
            else:
                self.updateApple()
                for i in range(1, len(self.snakeBody)):
                    tempX = self.snakeBody[i].winfo_x()
                    tempY = self.snakeBody[i].winfo_y()
                    self.snakeBody[i].place(x = prevX, y = prevY)
                    prevX = tempX
                    prevY = tempY
    def bodyCollision(self):
        for i in range(1, len(self.snakeBody)):
            if((self.snakeBody[0].winfo_x() == self.snakeBody[i].winfo_x()) and (self.snakeBody[0].winfo_y()  == self.snakeBody[i].winfo_y())):
                print("I worked")
                self.endGame()
    #replaces apple in valid position after snake eats it
    def updateApple(self):
        if(self.snakeBody[0].winfo_x() == self.apple.winfo_x() and self.snakeBody[0].winfo_y() == self.apple.winfo_y()): 
            self.incSnake()
            self.theScore +=1
            self.score["text"]= "Score: " + str(self.theScore)
            self.apple.place(x = random.randint(2, 28)*20, y = random.randint(2, 29)*20)
    #adds length to the tail of the snake
    def incSnake(self):
        self.snakeBody.append(tk.Frame(self.window, bg = "white", width = 20, height = 20))
        if(self.currDir == "Right"):
                self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x() - 20, y = self.snakeBody[-2].winfo_y())
        elif(self.currDir == "Left"):
                self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x() + 20, y = self.snakeBody[-2].winfo_y())
        elif(self.currDir == "Down"):
                self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x(), y = self.snakeBody[-2].winfo_y()+20)
        elif(self.currDir == "Up"):
                self.snakeBody[-1].place(x= self.snakeBody[-2].winfo_x(), y = self.snakeBody[-2].winfo_y()-20)

    def endGame(self):
        self.window.after_cancel(self.id)
run = SnakeGame()