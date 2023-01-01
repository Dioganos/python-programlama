from tkinter import *
import tkinter as tk
from tkinter import  messagebox
import  requests
from bs4 import BeautifulSoup
import os
import zipfile
import pandas as pd
import sqlite3
from cryptocmd import CmcScraper
import matplotlib.pyplot as plt

program = tk.Tk(className="Main")
program.geometry("680x680")


def basinca():
    parite = clicked.get()
    bas_tarih = dateS.get()
    bit_tarih = dateE.get()
    # initialise scraper with time interval
    scraper = CmcScraper(parite, bas_tarih, bit_tarih)

    headers, data = scraper.get_data()

    json_data = scraper.get_data("json")

    scraper.export("csv")

    df = scraper.get_dataframe()
    liste_x = []
    liste_y = []
    for mum in df.get(key="High"):
        liste_y.append(mum)
    for mum in df.get(key="Date"):
        liste_x.append(mum)
    liste_y.reverse()
    plt.plot(liste_x, liste_y)
    plt.savefig("plt.png")
    image = tk.PhotoImage(file="plt.png")
    imageLabel.configure(image=image)
    imageLabel.image = image
    plt.close()

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