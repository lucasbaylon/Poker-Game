from tkinter import *
from startpage import StartPage
from gamepage import GamePage
import time
from settings import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.game_object = object

        self.title("Poker Game")
        self.geometry("1080x720")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        list_of_frames = [StartPage, GamePage]

        for F in list_of_frames:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.fresh = True
        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        print("waiting")
        if not self.fresh:
            time.sleep(0.1)
            frame.update(game_info_q.get())
        self.fresh = False
        frame.tkraise()
