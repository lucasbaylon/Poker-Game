from functions import *
from settings import *
from tkinter import *
from PIL import ImageTk, Image
import time


class GamePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.restart = False

        canv = Canvas(self, width=1280, height=720, bg='white')
        canv.grid(row=2, column=3)

        # img = ImageTk.PhotoImage(Image.open("img/table.png").resize((1280, 720), Image.ANTIALIAS))
        # canv.create_image(0, 0, anchor=NW, image=img)

        # On affiche la table
        self.table = Label(canv)
        self.table.place(x=0, y=0)
        table_img = ImageTk.PhotoImage(
            Image.open("img/table.png").resize((1280, 720), Image.ANTIALIAS))
        self.table.image = table_img
        self.table.configure(image=table_img)

        # On affiche les infos des joueurs
        self.name_label_p0 = Label(canv, font=("Courier", 10), bd=3)
        self.name_label_p0.place(x=230, y=30)
        self.chips_label_p0 = Label(canv, font=("Courier", 10), bd=3)
        self.chips_label_p0.place(x=230, y=200)
        self.card1_p0 = Label(canv)
        self.card1_p0.place(x=200, y=50)
        self.card2_p0 = Label(canv)
        self.card2_p0.place(x=250, y=50)
        self.stake_label_p0 = Label(canv, bd=1, relief="groove")
        self.stake_label_p0.place(x=350, y=210)

        self.name_label_p1 = Label(canv, font=("Courier", 10), bd=3)
        self.name_label_p1.place(x=980, y=30)
        self.chips_label_p1 = Label(canv, font=("Courier", 10), bd=3)
        self.chips_label_p1.place(x=980, y=200)
        self.card1_p1 = Label(canv)
        self.card1_p1.place(x=950, y=50)
        self.card2_p1 = Label(canv)
        self.card2_p1.place(x=1000, y=50)
        self.stake_label_p1 = Label(canv, bd=1, relief="groove")
        self.stake_label_p1.place(x=880, y=210)

        # On affiche le board avec les cartes retournées
        self.cc_1 = Label(canv)
        self.cc_1.place(x=395, y=285)
        card_d1 = ImageTk.PhotoImage(
            Image.open("cards\default0.png").resize((85, 130), Image.ANTIALIAS))
        self.cc_1.image = card_d1
        self.cc_1.configure(image=card_d1)

        self.cc_2 = Label(canv)
        self.cc_2.place(x=495, y=285)
        card_d2 = ImageTk.PhotoImage(
            Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
        self.cc_2.image = card_d2
        self.cc_2.configure(image=card_d2)

        self.cc_3 = Label(canv)
        self.cc_3.place(x=595, y=285)
        card_d3 = ImageTk.PhotoImage(
            Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
        self.cc_3.image = card_d3
        self.cc_3.configure(image=card_d3)

        self.cc_4 = Label(canv)
        self.cc_4.place(x=695, y=285)
        card_d4 = ImageTk.PhotoImage(
            Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
        self.cc_4.image = card_d4
        self.cc_4.configure(image=card_d4)

        self.cc_5 = Label(canv)
        self.cc_5.place(x=795, y=285)
        card_d5 = ImageTk.PhotoImage(
            Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
        self.cc_5.image = card_d5
        self.cc_5.configure(image=card_d5)

        self.pot_label = Label(canv, text="pot: ", font=("Courier", 12), bd=3)
        self.pot_label.place(x=590, y=430)

        self.actor_label = Label(canv, text="Actor: ", font=("Courier", 12), bd=3)
        self.actor_label.place(x=200, y=650)

        # On affiche les boutons d'actions

        self.fold_button = Button(canv, text="Passer", font=("Courier", 12),
                                  command=lambda: self.action_input("fold"))
        self.fold_button.place(x=400, y=650)

        self.check_button = Button(canv, text="Parole", font=("Courier", 12),
                                   command=lambda: self.action_input("check"))
        # self.check_button.place(x=400, y=650)
        self.check_button.place_forget()

        self.call_button = Button(canv, text="Suivre", font=("Courier", 12),
                                  command=lambda: self.action_input("call_exact"))
        # call_button.place(x=500, y=650)
        self.call_button.place_forget()

        self.raise_button = Button(canv, text="Relancer", font=("Courier", 12),
                                   command=lambda: self.action_input("raise"))
        # self.raise_button.place(x=600, y=650)
        self.raise_button.place_forget()

        self.call_and_raise_button = Button(canv, text="Relancer", font=("Courier", 12),
                                            command=lambda: self.action_input("call_and_raise"))
        # self.call_and_raise_button.place(x=600, y=650)
        self.call_and_raise_button.place_forget()

        self.raise_entry = Entry(canv, font=("Courier", 12), bd=3)
        # self.raise_entry.insert(END, 'Lucas')
        self.raise_entry.place(x=700, y=650)

        self.all_in_button = Button(canv, text="All in", font=("Courier", 12),
                                    command=lambda: self.action_input("all_in"))
        # self.all_in_button.place(x=800, y=650)
        self.all_in_button.place_forget()

        self.all_in_exact_button = Button(canv, text="All in", font=("Courier", 12),
                                          command=lambda: self.action_input("all_in_exact"))
        # self.all_in_exact_button.place(x=800, y=650)
        self.all_in_exact_button.place_forget()

        self.call_and_all_in_button = Button(canv, text="All in", font=("Courier", 12),
                                             command=lambda: self.action_input("call_and_all_in"))
        # self.all_in_exact_button.place(x=800, y=650)
        self.call_and_all_in_button.place_forget()

        self.winner_label = Label(canv, font=("Courier", 12), bd=3)
        # self.winner_label.place(x=520, y=160)
        self.winner_label.place_forget()

    def update(self, game):
        # self.new_round_label.lower(self.action_cover_label)
        # self.button_y.lower(self.action_cover_label)
        # self.button_n.lower(self.action_cover_label)
        # self.raise_entry.lower(self.action_cover_label)
        # self.winner_label.lower(self.action_cover_label)
        # self.raise_button.lower(self.action_cover_label)
        print(self.raise_entry.get())
        if self.restart:
            card1 = ImageTk.PhotoImage(Image.open(str("cards\default0.png")).resize((85, 130), Image.ANTIALIAS))
            self.cc_1.image = card1
            self.cc_1.configure(image=card1)

            card1 = ImageTk.PhotoImage(Image.open(str("cards\default0.png")).resize((85, 130), Image.ANTIALIAS))
            self.cc_2.image = card1
            self.cc_2.configure(image=card1)

            card1 = ImageTk.PhotoImage(Image.open(str("cards\default0.png")).resize((85, 130), Image.ANTIALIAS))
            self.cc_3.image = card1
            self.cc_3.configure(image=card1)

            card1 = ImageTk.PhotoImage(Image.open(str("cards\default0.png")).resize((85, 130), Image.ANTIALIAS))
            self.cc_4.image = card1
            self.cc_4.configure(image=card1)

            card1 = ImageTk.PhotoImage(Image.open(str("cards\default0.png")).resize((85, 130), Image.ANTIALIAS))
            self.cc_5.image = card1
            self.cc_5.configure(image=card1)
            self.restart = False
        if game.round_ended:
            time.sleep(0.3)
            # self.new_round_label.lift(self.action_cover_label)
            # self.button_y.lift(self.action_cover_label)
            # self.button_n.lift(self.action_cover_label)
            winners = []
            scores = []
            for player in game.list_of_players_not_out:
                if player.win:
                    winners.append(player)
                    scores.append(player.score)
            print(f"gui thinks winners are: {winners}")
            print(f"and thinks scores are: {scores}")
            if scores == [[]]:
                self.winner_label.place(x=520, y=160)
                self.winner_label["text"] = "Gagnant: " + str(winners)
            else:
                try:
                    for player in game.list_of_players_not_out:
                        if player.win:
                            if player.score == max(scores):
                                self.winner_label.place(x=520, y=160)
                                self.winner_label["text"] = "Gagnant: " + str(winners) + "\n" + score_interpreter(
                                    player)
                except IndexError:
                    pass
            # self.winner_label.lift(self.action_cover_label)

            self.restart = True

            return
        # if game.need_raise_info:
        #     self.raise_entry.lift(self.action_cover_label)
        #     self.raise_button.lift(self.action_cover_label)
        try:
            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.cards[0]) + ".png").resize((85, 130), Image.ANTIALIAS))
            self.cc_1.image = card1
            self.cc_1.configure(image=card1)

            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.cards[1]) + ".png").resize((85, 130), Image.ANTIALIAS))
            self.cc_2.image = card1
            self.cc_2.configure(image=card1)

            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.cards[2]) + ".png").resize((85, 130), Image.ANTIALIAS))
            self.cc_3.image = card1
            self.cc_3.configure(image=card1)

            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.cards[3]) + ".png").resize((85, 130), Image.ANTIALIAS))
            self.cc_4.image = card1
            self.cc_4.configure(image=card1)

            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.cards[4]) + ".png").resize((85, 130), Image.ANTIALIAS))
            self.cc_5.image = card1
            self.cc_5.configure(image=card1)
        except IndexError:
            pass
        try:
            self.name_label_p0["text"] = game.list_of_players[0]
            self.name_label_p1["text"] = game.list_of_players[1]
            # self.name_label_p2["text"] = game.list_of_players[2]
            # self.name_label_p3["text"] = game.list_of_players[3]
            # self.name_label_p4["text"] = game.list_of_players[4]
            # self.name_label_p5["text"] = game.list_of_players[5]
            # self.name_label_p6["text"] = game.list_of_players[6]
            # self.name_label_p7["text"] = game.list_of_players[7]
            # self.name_label_p8["text"] = game.list_of_players[8]
            # self.name_label_p9["text"] = game.list_of_players[9]
        except IndexError:
            pass
        try:
            self.chips_label_p0["text"] = "Chips:\n" + str(game.list_of_players[0].chips)
            self.chips_label_p1["text"] = "Chips:\n" + str(game.list_of_players[1].chips)
            # self.chips_label_p2["text"] = "Chips:\n" + str(game.list_of_players[2].chips)
            # self.chips_label_p3["text"] = "Chips:\n" + str(game.list_of_players[3].chips)
            # self.chips_label_p4["text"] = "Chips:\n" + str(game.list_of_players[4].chips)
            # self.chips_label_p5["text"] = "Chips:\n" + str(game.list_of_players[5].chips)
            # self.chips_label_p6["text"] = "Chips:\n" + str(game.list_of_players[6].chips)
            # self.chips_label_p7["text"] = "Chips:\n" + str(game.list_of_players[7].chips)
            # self.chips_label_p8["text"] = "Chips:\n" + str(game.list_of_players[8].chips)
            # self.chips_label_p9["text"] = "Chips:\n" + str(game.list_of_players[9].chips)
        except IndexError:
            pass
        try:
            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.list_of_players[0].cards[0]) + ".png").resize((85, 130),
                                                                                              Image.ANTIALIAS))
            self.card1_p0.image = card1
            self.card1_p0.configure(image=card1)

            card1 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.list_of_players[1].cards[0]) + ".png").resize((85, 130),
                                                                                              Image.ANTIALIAS))
            self.card1_p1.image = card1
            self.card1_p1.configure(image=card1)

            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[2].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p2.image = card1
            # self.card1_p2.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[3].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p3.image = card1
            # self.card1_p3.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[4].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p4.image = card1
            # self.card1_p4.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[5].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p5.image = card1
            # self.card1_p5.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[6].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p6.image = card1
            # self.card1_p6.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[7].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p7.image = card1
            # self.card1_p7.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[8].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p8.image = card1
            # self.card1_p8.configure(image=card1)
            #
            # card1 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[9].cards[0]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card1_p9.image = card1
            # self.card1_p9.configure(image=card1)
        except IndexError:
            pass
        try:
            card2 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.list_of_players[0].cards[1]) + ".png").resize((85, 130),
                                                                                              Image.ANTIALIAS))
            self.card2_p0.image = card2
            self.card2_p0.configure(image=card2)

            card2 = ImageTk.PhotoImage(
                Image.open("cards\\" + str(game.list_of_players[1].cards[1]) + ".png").resize((85, 130),
                                                                                              Image.ANTIALIAS))
            self.card2_p1.image = card2
            self.card2_p1.configure(image=card2)

            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[2].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p2.image = card2
            # self.card2_p2.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[3].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p3.image = card2
            # self.card2_p3.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[4].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p4.image = card2
            # self.card2_p4.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[5].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p5.image = card2
            # self.card2_p5.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[6].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p6.image = card2
            # self.card2_p6.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[7].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p7.image = card2
            # self.card2_p7.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[8].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p8.image = card2
            # self.card2_p8.configure(image=card2)
            #
            # card2 = ImageTk.PhotoImage(
            #     Image.open("cards\\" + str(game.list_of_players[9].cards[1]) + ".png").resize((55, 85), Image.ANTIALIAS))
            # self.card2_p9.image = card2
            # self.card2_p9.configure(image=card2)
        except IndexError:
            pass
        try:
            self.stake_label_p0["text"] = "Stake: " + str(game.list_of_players[0].stake)
            self.stake_label_p1["text"] = "Stake: " + str(game.list_of_players[1].stake)
            # self.stake_label_p2["text"] = "Stake: " + str(game.list_of_players[2].stake)
            # self.stake_label_p3["text"] = "Stake: " + str(game.list_of_players[3].stake)
            # self.stake_label_p4["text"] = "Stake: " + str(game.list_of_players[4].stake)
            # self.stake_label_p5["text"] = "Stake: " + str(game.list_of_players[5].stake)
            # self.stake_label_p6["text"] = "Stake: " + str(game.list_of_players[6].stake)
            # self.stake_label_p7["text"] = "Stake: " + str(game.list_of_players[7].stake)
            # self.stake_label_p8["text"] = "Stake: " + str(game.list_of_players[8].stake)
            # self.stake_label_p9["text"] = "Stake: " + str(game.list_of_players[9].stake)
        except IndexError:
            pass
        self.pot_label["text"] = "Pot: " + str(game.pot)
        if game.game_over:
            self.actor_label["text"] = "Winner!: " + str(game.winner.name)
            return
        print(f"round ended {game.round_ended}")

        self.actor_label["text"] = "Au tour de " + str(game.acting_player.name)

        # On affiche soit le bouton check, soit le bouton Suivre, en fonction des réponses possibles
        if "call_exact" in game.possible_responses:
            self.call_button.place(x=500, y=650)
            self.check_button.place_forget()
        elif "check" in game.possible_responses:
            self.check_button.place(x=500, y=650)
            self.call_button.place_forget()

        # On affiche les différents boutons de relance possible en fonction des réponses possible
        if "raise" in game.possible_responses:
            self.raise_button.place(x=600, y=650)
            self.call_and_raise_button.place_forget()
        elif "call_and_raise" in game.possible_responses:
            self.call_and_raise_button.place(x=600, y=650)
            self.raise_button.place_forget()

        # On affiche les différents boutons all in possible en fonction des réponses possible
        if "all_in" in game.possible_responses:
            self.all_in_button.place(x=800, y=650)
            self.all_in_exact_button.place_forget()
            self.call_and_all_in_button.place_forget()
        elif "all_in_exact" in game.possible_responses:
            self.all_in_exact_button.place(x=800, y=650)
            self.all_in_button.place_forget()
            self.call_and_all_in_button.place_forget()
            self.call_button.place_forget()
            self.check_button.place_forget()
            self.raise_button.place_forget()
        elif "call_and_all_in" in game.possible_responses:
            self.call_and_all_in_button.place(x=800, y=650)
            self.all_in_button.place_forget()
            self.all_in_exact_button.place_forget()

        # variable = StringVar(self.action_frame)
        # variable.initialize("ACTION")
        # w = OptionMenu(self.action_frame, variable, *game.possible_responses)
        # w.place(relx=0, rely=0.05, relheight=0.1, relwidth=0.3)
        # button_go = Button(self.action_frame, text="GO", font=("Courier", 10),
        #                    command=lambda: self.action_input(variable.get()))
        # button_go.place(relx=1, rely=1, relheight=0.3, relwidth=0.3, anchor="se")

    def action_input(self, entry0):
        response_q.put(entry0)
        game_event.set()
        time.sleep(0.1)
        if not game_info_q.empty():
            self.update(game_info_q.get())
