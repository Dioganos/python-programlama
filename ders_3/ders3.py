"""                                              Ders-3                                                              """

# Soru - 1

"""
    kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu 
    toplamdan çıkaran ve geri döndürne python script yazınız.(düz ve ters okunuşu aynı olan sayılar)


sayilar = []

a = int(input("Kac tane sayi girmek istersiniz ? : "))

for x in range(0,a):
    sayilar.append(int(input(str(x+1)+". sayiyi giriniz: ")))

def polBul(dizi):
    toplam = 0
    for polMu in dizi:
        if str(polMu)[::-1] == str(polMu):
            toplam += polMu
        else:
            toplam -= polMu
    return toplam

print(polBul(sayilar))

"""


# Class

"""

class sinif:
    a = 0
    b= "ads"
    c = [1,3,5]

nesne = sinif()
print(nesne.a)
nesne.a = 999
print(nesne.a)

"""

# Metot

"""

class sinif:
    a = 5
    b = "ads"
    c=[1,3,5]

    def yazdir(self):
        d = 100
        print(d,self.a)
    def yazdir2(self,t):
        self.yazdir()
        print(t)

nesne = sinif()
nesne.yazdir()
nesne.yazdir2("gafasd")

"""

# Class __init__ -> constructor (yapıcı) metot | __del__ -> nesne bellekten silinirken çalışacak fonksiyon
#   __str__ -> nesne yazdirilirsa döndürülecek string

"""

class sinif:
    metin = ""
    def __init__(self,a):
        self.metin = a
    def __str__(self):
        return "Yazdırılan : " + self.metin
    def __del__(self):
        print("Beni siliyorlar")

nesne = sinif("Metin")
print(nesne.metin)
nesne2 = sinif("Civa")
print(nesne2)

"""

# Module import

"""

import module

print(module.topla(3,5))
print(module.carp(module.e,5))
print(module.w)
print(module.e[0])

from module import topla # Kütüphanenin içinden sadece belli bir bölümü çekmek için kullanılır.

print(topla(4,5))

import module as mdl

print(mdl.topla(5,5))

"""

# Try - Except

"""

x = "asd"
try:
    y = 5 + x
except:
    print("Hemşerim string ile integer'ı toplayamazsın")

"""

# Kütüphane dahil etme ve kullanma

"""

from termcolor import colored

print(colored("Hello, World!", "red", attrs=["reverse", "blink"]))

import os

dosya = open("ders3_metin.txt",'r')

for satir in dosya:
    print(satir[:-1])

dosya2 = open("ders3_cop.txt",'w')

print("Koyluler",file=dosya2)
dosya2.close()

dosyaCode = open("ders3_dosyaCode.txt",'w')
print(("print('efsane python')"),file=dosyaCode)
dosyaCode.close()


dosyaCodeOku = open("ders3_dosyaCode.txt",'r')
satir = dosyaCodeOku.readline()
eval(satir)

"""





