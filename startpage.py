from gamepage import GamePage
from settings import *
from tkinter import *


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        height = 720
        width = 1280
        canvas = Canvas(self, height=height, width=width, bg="light green")
        canvas.pack()

        left_frame = Frame(canvas, bg='#2aa96d', bd=5)
        left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')
        name_frame = Frame(left_frame, bg="#41B77F", bd=5)
        name_frame.place(relx=0.5, rely=0.17, relwidth=0.9, relheight=0.7, anchor="n")
        self.entry_p0 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p0.insert(END, 'Lucas')
        self.entry_p0.place(relwidth=0.5, relheight=0.1)
        self.entry_p1 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p1.insert(END, 'Basto')
        self.entry_p1.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1)
        self.entry_p2 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p2.place(relx=0, rely=0.125, relwidth=0.5, relheight=0.1)
        self.entry_p3 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p3.place(relx=0.5, rely=0.125, relwidth=0.5, relheight=0.1)
        enter_player_label = Label(left_frame, text="Player Names:", font=("Courier", 12), bd=3)
        enter_player_label.place(relx=0.25, rely=0.07, relwidth=0.5, relheight=0.05)

        right_frame = Frame(canvas, bg='#41B77F', bd=5)
        right_frame.place(relx=1, rely=0, relwidth=0.5, relheight=1, anchor='ne')
        self.sc_label = Label(right_frame, text="Starting Chips:", font=("Courier", 12), bd=3)
        self.sc_label.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.05)
        self.sc_entry = Entry(right_frame, font=("Courier"), bd=3)
        self.sc_entry.insert(END, '2000')
        self.sc_entry.place(relx=0.5, rely=0.17, relwidth=0.5, relheight=0.07, anchor="n")

        self.sb_label = Label(right_frame, text="Small-Blind Chips:", font=("Courier", 12), bd=3)
        self.sb_label.place(relx=0.25, rely=0.33, relwidth=0.5, relheight=0.05)
        self.sb_entry = Entry(right_frame, font=("Courier"), bd=3)
        self.sb_entry.insert(END, '100')
        self.sb_entry.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.07, anchor="n")

        self.bb_label = Label(right_frame, text="Big-Blind Chips:", font=("Courier", 12), bd=3)
        self.bb_label.place(relx=0.25, rely=0.56, relwidth=0.5, relheight=0.05)
        self.bb_entry = Entry(right_frame, font=("Courier"), bd=3)
        self.bb_entry.insert(END, '200')
        self.bb_entry.place(relx=0.5, rely=0.63, relwidth=0.5, relheight=0.07, anchor="n")
        self.bb_entry.bind("<Return>", lambda _: self.button_click(self.entry_p0.get(), self.entry_p1.get(),
                                                                   self.entry_p2.get(), self.entry_p3.get(),
                                                                   self.sc_entry.get(), self.sb_entry.get(),
                                                                   self.bb_entry.get(), controller))

        button = Button(right_frame, text="START", font=("Courier", 12),
                        command=lambda: self.button_click(self.entry_p0.get(), self.entry_p1.get(),
                                                          self.entry_p2.get(), self.entry_p3.get(),
                                                          self.sc_entry.get(), self.sb_entry.get(),
                                                          self.bb_entry.get(), controller))
        button.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.1, anchor="n")

    def button_click(self, entry0, entry1, entry2, entry3, entrysc,
                     entrysb, entrybb, controller):
        entry_list = [entry0, entry1, entry2, entry3, entrysc, entrysb, entrybb]
        player_entry_list = [entry0, entry1, entry2, entry3]
        print(player_entry_list)
        player_entry_list = list(set(player_entry_list))
        for player in player_entry_list:
            if player == "":
                player_entry_list.remove(player)
        print(player_entry_list)
        if len(player_entry_list) < 2:
            print("not enough players")
            return
        chip_entry_list = [entrysc, entrysb, entrybb]
        for chips in chip_entry_list:
            try:
                chips = int(chips)
            except ValueError:
                print("Value Error")
                return
            if chips == "" or chips <= 0:
                print("chip entry error")
                return
        if not int(entrysc) > int(entrybb) > int(entrysb):
            print("chip entry error2 ")
            return
        setup = {
            "players": player_entry_list,
            "chips": chip_entry_list
        }
        response_q.put(setup)
        game_event.set()
        controller.show_frame(GamePage)
