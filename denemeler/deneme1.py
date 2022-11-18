import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import os

program = tk.Tk(className="Main")
program.geometry("390x180+460+370")
def basinca():
    program.withdraw()
    dizi = tk.Tk(className="Dizi")
    dizi.geometry("390x500+460+150")
    def geri1():
        dizi.withdraw()
        program.deiconify()
    geri = Button(master=dizi, text='Geri Dön', bg='blue', fg='red', command=geri1)
    geri.place(x=5, y=5)
def basinca2():
    program.withdraw()
    film = tk.Tk(className="Film")
    film.geometry("390x500+460+150")
    def geri2():
        film.withdraw()
        program.deiconify()
    geri = Button(master=film, text='Geri Dön', bg='blue', fg='red', command=geri2)
    geri.place(x=5, y=5)


buton1 = Button(master=program,text = 'Dizi',bg = 'blue',fg ='red',command =basinca,width=20,height=10)
buton1.place(x=30,y=10)
buton2 = Button(master=program,text = 'Film',bg = 'blue',fg ='red',command =basinca2,width=20,height=10)
buton2.place(x=200,y=10)

program.mainloop()