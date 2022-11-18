import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import requests
from instabot import  Bot
from PIL import Image, ImageFont, ImageDraw
import os
window = tk.Tk()
window.title("Soz botu")
window.config(bg= "#FFFAFA")
window.resizable(0,0)
window.geometry("700x700")
bot = Bot()
sayfa = Label(master=window,text = 'Kacinci sayfada islem yapacaksiniz (1-100) : ',bg='#FFFAFA')
sayfa.place(x=5,y=5)
sayfaal = Entry(master=window)
sayfaal.place(x=240,y=5)
sayi = Label(master=window,text = 'Kac tane alinti yapacaksiniz?: ',bg='#FFFAFA')
sayi.place(x=5,y=30)
sayial = Entry(master=window)
sayial.place(x=165,y=30)
def basinca():
    url = requests.get("https://www.goodreads.com/quotes?page={}".format(sayfaal.get())).content
    veri = BeautifulSoup(url, "html.parser")
    quotes = [i.text for i in veri.find_all(class_='quoteText', limit=int(sayial.get()))]
    for k in range(int(sayial.get())):
        img = Image.new('RGB', (1280, 1024), 'black')
        quotebu = quotes[k]
        quoteo = quotebu.replace('.','\n').replace('\"',"")
        quotesu = quoteo.replace('“','').replace("”",'')
        font = ImageFont.truetype("arial.ttf", 20)
        w, h = font.getsize(quotesu)
        draw = ImageDraw.Draw(img)
        draw.text((2,  h/2), quotesu, font=font, fill="white")
        img.save('{}quote.jpg'.format(k))
def basinca2():
    bot.login(username="denemequotebot1", password="123456789x")
    for k in range(int(sayial.get())):
        bot.upload_photo("{}quote.jpg".format(k), caption="Gunluk Quote")
        os.remove("{}quote.jpg.REMOVE_ME".format(k))
    os.remove('config/denemequotebot1_uuid_and_cookie.json')
buton = Button(master=window,text='Quote Cek',command = basinca)
buton.place(x=10,y=60)
buton = Button(master=window,text='Quote Paylas',command = basinca2)
buton.place(x=90,y=60)
window.mainloop()
