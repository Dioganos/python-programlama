from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup
import requests

###############Variables###################
window = Tk()
url = requests.get("https://www.doviz.com/").content

###############Variables End###############

###############Functions##################
def Dolargetir():
    soup = BeautifulSoup(url, "html.parser")
    kurd = soup.find("span", attrs={"data-socket-key": "USD"})
    outd.delete(0,END)
    outd.insert(END,kurd.text+' ₺')
def Eurogetir():
    soup = BeautifulSoup(url, "html.parser")
    kure = soup.find("span", attrs={"data-socket-key": "EUR"})
    oute.delete(0, END)
    oute.insert(END, kure.text + ' ₺')
def Sterlingetir():
    soup = BeautifulSoup(url, "html.parser")
    kurs = soup.find("span", attrs={"data-socket-key": "GBP"})
    outs.delete(0, END)
    outs.insert(END, kurs.text + ' ₺')
def Btcgetir():
    soup = BeautifulSoup(url, "html.parser")
    kurdprev = soup.find("span", attrs={"data-socket-key": "USD"})
    kurd = kurdprev.text.replace(",",".")
    kurbtcprev = soup.find("span", attrs={"data-socket-key": "bitcoin"})
    kurbtcprev2 = kurbtcprev.text.split('$')
    kurbtcprev3 = kurbtcprev2[1].split(',')
    kurbtcprev4 = kurbtcprev3[0].split('.')
    kurbtc = kurbtcprev4[0] + kurbtcprev4[1] + "." + kurbtcprev3[1]
    outbtc.delete(0, END)
    outbtc.insert(END, str(float(kurbtc) * float(kurd)) + ' ₺')
def Altingetir():
    soup = BeautifulSoup(url, "html.parser")
    kuraltin = soup.find("span", attrs={"data-socket-key": "gram-altin"})
    outaltin.delete(0, END)
    outaltin.insert(END, kuraltin.text + ' ₺')
def Gumusgetir():
    soup = BeautifulSoup(url, "html.parser")
    kurgumus = soup.find("span", attrs={"data-socket-key": "gumus"})
    outgumus.delete(0, END)
    outgumus.insert(END, kurgumus.text + ' ₺')
###############Functions End##############

###############Designer####################
window.title("Kur Hesaplayici")
window.config(bg= "#FFFAFA")
window.resizable(0,0)
window.geometry("290x275")
##Title
title = tk.Label(master = window,text = 'Kur Hesaplayiciya Hos Geldiniz!',bg="#FFFAFA",fg="black")
title.place(x=70,y=210)
##Dolar
btnd = tk.Button(master=window, text='Kur getir!',command = Dolargetir,bg="#85bb65")
btnd.place(x=5,y=5)
outd = tk.Entry(master=window,bg="#85bb65")
outd.place(x=145,y=9)
signd = tk.Label(master=window, text='Dolar($) - TL',bg="#85bb65")
signd.place(x=70,y=8)
##Euro
btne = tk.Button(master=window, text='Kur getir!',command = Eurogetir,bg="darkorchid")
btne.place(x=5,y=35)
oute = tk.Entry(master=window,bg="darkorchid")
oute.place(x=145,y=39)
signe = tk.Label(master=window, text='Euro(€) - TL',bg="darkorchid")
signe.place(x=70,y=38)
##Sterlin
btns = tk.Button(master=window, text='Kur getir!',command = Sterlingetir,bg="#00FF7F")
btns.place(x=5,y=65)
outs = tk.Entry(master=window,bg="#00FF7F")
outs.place(x=155,y=69)
signs = tk.Label(master=window, text='Sterlin(£) - TL',bg="#00FF7F")
signs.place(x=70,y=68)
##BTC
btnbtc = tk.Button(master=window, text='Kur getir!',command = Btcgetir,bg="#f2a900")
btnbtc.place(x=5,y=95)
outbtc = tk.Entry(master=window,bg="#f2a900")
outbtc.place(x=125,y=99)
signbtc = tk.Label(master=window, text='BTC - TL',bg="#f2a900")
signbtc.place(x=70,y=98)
##Altin
btnaltin = tk.Button(master=window, text='Kur getir!',command = Altingetir,bg="#FFD700")
btnaltin.place(x=5,y=125)
outaltin = tk.Entry(master=window,bg="#FFD700")
outaltin.place(x=160,y=129)
signaltin = tk.Label(master=window, text='Gram Altin - TL',bg="#FFD700")
signaltin.place(x=70,y=128)
##Gumus
btngumus = tk.Button(master=window, text='Kur getir!',command = Gumusgetir,bg="#C0C0C0")
btngumus.place(x=5,y=155)
outgumus = tk.Entry(master=window,bg="#C0C0C0")
outgumus.place(x=145,y=159)
signgumus = tk.Label(master=window, text='Gumus - TL',bg="#C0C0C0")
signgumus.place(x=70,y=158)
###############Designer End################

window.mainloop()