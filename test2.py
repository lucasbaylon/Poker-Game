from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("1280x720")
root.title("test")

canv = Canvas(root, width=1280, height=720, bg='white')
canv.grid(row=2, column=3)

# img = ImageTk.PhotoImage(Image.open("table.png"))  # PIL solution
img = ImageTk.PhotoImage(Image.open("img/table.png").resize((1280, 720), Image.ANTIALIAS))  # PIL solution
canv.create_image(0, 0, anchor=NW, image=img)

card1_p0 = Label(canv)
card1_p0.place(x=200, y=50)
card2_p0 = Label(canv)
card2_p0.place(x=250, y=50)

card1_p1 = Label(canv)
card1_p1.place(x=950, y=50)
card2_p1 = Label(canv)
card2_p1.place(x=1000, y=50)

card1 = ImageTk.PhotoImage(
    Image.open("cards\\Ace of Diamonds.png").resize((85, 130), Image.ANTIALIAS))
card1_p0.image = card1
card1_p0.configure(image=card1)
card2 = ImageTk.PhotoImage(
    Image.open("cards\\Ace of Hearts.png").resize((85, 130), Image.ANTIALIAS))
card2_p0.image = card2
card2_p0.configure(image=card2)

card1_2 = ImageTk.PhotoImage(
    Image.open("cards\\Ace of Clubs.png").resize((85, 130), Image.ANTIALIAS))
card1_p1.image = card1_2
card1_p1.configure(image=card1_2)
card2_2 = ImageTk.PhotoImage(
    Image.open("cards\\Ace of Spades.png").resize((85, 130), Image.ANTIALIAS))
card2_p1.image = card2_2
card2_p1.configure(image=card2_2)

cc_1 = Label(canv)
cc_1.place(x=395, y=285)
card_d1 = ImageTk.PhotoImage(
    Image.open("cards\default0.png").resize((85, 130), Image.ANTIALIAS))
cc_1.image = card_d1
cc_1.configure(image=card_d1)

cc_2 = Label(canv)
cc_2.place(x=495, y=285)
card_d2 = ImageTk.PhotoImage(
    Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
cc_2.image = card_d2
cc_2.configure(image=card_d2)

cc_3 = Label(canv)
cc_3.place(x=595, y=285)
card_d3 = ImageTk.PhotoImage(
    Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
cc_3.image = card_d3
cc_3.configure(image=card_d3)

cc_4 = Label(canv)
cc_4.place(x=695, y=285)
card_d4 = ImageTk.PhotoImage(
    Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
cc_4.image = card_d4
cc_4.configure(image=card_d4)

cc_5 = Label(canv)
cc_5.place(x=795, y=285)
card_d5 = ImageTk.PhotoImage(
    Image.open("cards\default1.png").resize((85, 130), Image.ANTIALIAS))
cc_5.image = card_d5
cc_5.configure(image=card_d5)

mainloop()
