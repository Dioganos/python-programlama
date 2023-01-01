from tkinter import *
import tkinter as tk
from tkinter import  messagebox
import  requests
from bs4 import BeautifulSoup
import os
import zipfile
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

program = tk.Tk(className="Main")
program.geometry("680x680")


def basinca():
    parite = clicked.get()
    bas_tarih = dateS.get()
    bit_tarih = dateE.get()
    print(parite)

    sorgu = "SELECT * FROM parite WHERE " \
            "(otime BETWEEN '" + bas_tarih + "' " \
                                             "AND '" + bit_tarih + "') " \
                                                                   "AND parite='" + parite + "'"
    cursor.execute(sorgu)
    sonuc = cursor.fetchall()
    liste_x = []
    liste_y = []
    for mum in sonuc:
        # print(mum)
        print(mum[6])
        liste_y.append(mum[6])
        liste_x.append(mum[2])

    plt.plot(liste_x, liste_y)
    plt.savefig("plt.png")
    image = tk.PhotoImage(file="plt.png")
    imageLabel.configure(image=image)
    imageLabel.image = image

options = []

kayitlar = pd.read_csv("hepsi.csv")
for kayit in kayitlar["parite"]:
    if not kayit in options:
        options.append(kayit)

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()



clicked = StringVar()
clicked.set("Select Parite")

pariteSLabel = Label(program,text="Select Parite").place(x="5",y="8")
drop = OptionMenu(program, clicked, *options).place(x="80",y="1")
datesLabel = Label(program,text="Start Date").place(x="5",y="50")
dateS = Entry(program,bg='white',fg='black')
dateS.place(x="65",y="50")
datesLabel = Label(program,text="End Date").place(x="5",y="75")
dateE= Entry(program,bg='white',fg='black')
dateE.place(x="65",y="75")
bringEntries = Button(program,text="Bring Entries",command=basinca).place(x="50",y="100")
imageLabel = tk.Label(program)
imageLabel.place(x="5",y="130")

program.mainloop()