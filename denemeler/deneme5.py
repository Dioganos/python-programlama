from tkinter import *
import tkinter as tk

###############Variables###################
window = Tk()
###############Variables End###############

###############Functions##################
def Hesapla():
    gno = (float(vizein.get()) *0.4)+ (float(finalin.get())*0.6)
    if gno < 50:
        gnoout.insert(END, str(gno) + " FF")
    elif gno < 60:
        gnoout.insert(END, str(gno) + " CC")
    elif gno < 70:
        gnoout.insert(END,str(gno) + " CB")
    elif gno < 80:
        gnoout(END,str(gno) + " BB")
    elif gno < 90:
        gnoout.insert(END, str(gno) + " AB")
    elif gno >= 90 and gno <=100:
        gnoout.insert(END,str(gno) + " AA")
    else:
        gnoout.insert(END, "Hata")
###############Functions End##############

###############Designer####################
window.title("GNO Hesaplayici")
window.config(bg= "#FFFAFA")
window.resizable(0,0)
window.geometry("290x275")
##Titles
vizebu = tk.Label(master = window,text = 'Vize Notu :',bg='white')
vizebu.place(x=5,y=5)
finalbu = tk.Label(master = window,text = 'Final Notu :',bg='white')
finalbu.place(x=5,y=45)
gnobu = tk.Label(master=window,text='GNO : ',bg='white')
gnobu.place(x=5,y=125)
##Vize
vizein = tk.Entry(master = window)
vizein.place(x=75,y=5)
##Final
finalin = tk.Entry(master = window)
finalin.place(x=75,y=45)
##Hesapla
hesapla = tk.Button(master = window,text = 'Hesapla',command = Hesapla,width = 25)
hesapla.place(x=10,y=85)
##GNO
gnoout = tk.Entry(master=window)
gnoout.place(x=45,y=125)
###############Designer End################

window.mainloop()