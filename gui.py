from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
from advice import *

class UI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width= 900
        self.height= 500
        self.canvas = Canvas(self, width = self.width, height = \
        self.height)
        self.canvas.pack()
        self.hdog= PhotoImage(file='img/happy_doggo.png')
        self.prev= PhotoImage(file='img/previous.png')
        self.background= PhotoImage(file='img/sea_green.png')
        self.out= PhotoImage(file= "img/logout.png")
        self.coverScreen()

    def logoutScreen(self):
        self.exit= Button(self, command="")
        self.exit.config(image=self.out, compound= CENTER, width=30, height=30)
        self.canvas.create_window(self.width/15*14, self.height/15, window= self.exit)

    def mainBackScreen(self):
        self.back= Button(self, command=self.tocScreen)
        self.back.config(image=self.prev, compound= CENTER, width= 30, height=30)
        self.canvas.create_window(self.width/15, self.height/15, window= self.back)

    def coverScreen(self):
        self.canvas.delete('all')
        self.start = Image.open('img/background_final.jpg')
        self.startImg = ImageTk.PhotoImage(self.start)
        self.canvas.create_image(self.width/2, self.height/2, \
        image=self.startImg)
        self.startButton = Button(self, command=self.tocScreen)
        self.startButton.config(image=self.hdog, compound= CENTER, width=200, height=200)
        self.canvas.create_window(self.width/2, self.height/5*2, \
        window=self.startButton)

    def tocScreen(self):
        self.canvas.delete('all')
        self.canvas.create_image(self.width/2, self.height/2, image= self.background)
        self.logexp = Button(self, text="Log expenses", \
        command="self.dataProcScreen", width= 300)
        self.logexp.config(font=('ms serif', 32, 'bold'))
        self.canvas.create_window(self.width/4, self.height/4, \
        window=self.logexp)
        
        self.project = Button(self, text="Project savings", \
        command="self.dataProcScreen", width= 300)
        self.project.config(font=('ms serif', 32, 'bold'))
        self.canvas.create_window(self.width/4, self.height/2, \
        window=self.project)

        self.interact = Button(self, text="Interact w/ your pet", \
        command="self.dataProcScreen", width= 300)
        self.interact.config(font=('ms serif', 32, 'bold'))
        self.canvas.create_window(self.width/4, self.height/4*3, \
        window=self.interact)
        self.logoutScreen()

       
    def petScreen(self):
        self.canvas.delete('all')
        self.room = Image.open('img/room.jpg')
        self.pet_room = ImageTk.PhotoImage(self.room)
        self.canvas.create_image(self.width/2, self.height/2, \
        image=self.pet_room)
        self.advice = Button(self, text="Give me advice!", \
        command=self.give_advice, width= 15)
        self.advice.config(font=('ms serif', 20, 'bold'))
        self.canvas.create_window(self.width/6*5, self.height/8*7, \
        window=self.advice)
        self.logoutScreen()
        self.mainBackScreen()

    def give_advice(self):
        self.petScreen()
        self.canvas.create_oval(self.width/2-180, self.height/3-100, self.width/2+180, self.height/3+80, \
                                fill="white", outline="white")
        self.canvas.create_polygon(self.width/2-180, self.height/3, self.width/2-100, self.height/3+50, self.width/2-200, self.height/3 + 80, fill="white")
        self.canvas.create_text(self.width/2, self.height/3, text= generate_advice(), width=300)

arbUI = UI()
arbUI.mainloop()
