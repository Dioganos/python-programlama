import smtplib
from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Mail Gonderici")
window.config(bg= "#FFFAFA")
window.resizable(0,0)
window.geometry("350x400")

def gonderr():
    smtplibObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login("denemeotomailbotu1@gmail.com", "snsijipewmfmwenj")
    mesajne = """Subject:{0}
        {1}
        """.format(baslik.get(), mesaj.get("1.0", END))
    smtplibObj.sendmail("denemeotomailbotu1@gmail.com", kime.get(), mesajne)
    smtplibObj.quit()

label1 = Label(master=window,text = 'Kime : ',bg='#FFFAFA')
label1.place(x=5,y=5)
kime = Entry(master=window,width = 40)
kime.place(x=45,y=5)
label3 = Label(master=window,text = 'Baslik : ',bg='#FFFAFA')
label3.place(x=5,y=35)
baslik = Entry(master=window,width = 40)
baslik.place(x=50,y=35)

label2 = Label(master=window,text = 'Mesaj : ',bg='#FFFAFA')
label2.place(x=5,y=65)
mesaj = Text(master=window,width=30,height =15)
mesaj.place(x=50,y=65)
gonder = Button(master=window,text = 'Gonder!',bg='red',width='35',command = gonderr)
gonder.place(x=50,y=320)


window.mainloop()