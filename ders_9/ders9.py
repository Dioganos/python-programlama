import pyautogui
from tkinter import *
import tkinter as tk
from tkinter import  messagebox
import  requests
from bs4 import BeautifulSoup

"""
MOUSE VE KLAVYE'YI OTOMATIK KONTROL ETMEK

for i in range(50):
    pyautogui.moveTo(50,500,duration=2,
                     tween = pyautogui.easeInOutCubic)
    pyautogui.moveTo(500,500,duration=2,
                     tween = pyautogui.easeInOutCubic)


sW,sH = pyautogui.size()
print(sW,sH)

curMoPosX , curMoPosY = pyautogui.position()
print(curMoPosX,curMoPosY)



distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)
    pyautogui.drag(-distance, 0, duration=0.5)
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)
    
"""

program = tk.Tk(className="Main")
program.geometry("512x512")
def basinca():
    id = userName.get()
    passw = passWord.get()
    if id == "Dio" and passw == "1234":
        dizi = tk.Tk()
        dizi.geometry("512x512")
        program.withdraw()
        def geri1():
            program.deiconify()
            dizi.destroy()
        geri = Button(master=dizi, text='Geri Dön', bg='blue', fg='red', command=geri1)
        geri.place(x=5, y=5)
    else:
        tk.messagebox.showerror(title="Hatali Deneme",message="Kullanici Adi ya da sifre hatali")

id = Label(master=program,text="Kullanici Adi : ")
id.place(x = 0,y = 0)
pw = Label(master=program,text="Sifre : ")
pw.place(x = 0,y = 35)
userName = Entry(master=program,bg='white',fg='black')
userName.place(x=80,y=0)
passWord = Entry(master=program,bg='white',fg='black',show="*")
passWord.place(x=40,y=35)
buton1 = Button(master=program,text = 'Dizi',bg = 'blue',fg ='red',command =basinca,width=5,height=1)
buton1.place(x=50,y=70)

program.mainloop()