"""                                              Ders-2                                                              """

#Ornek-1

"""
Kullanıcıdan alınan 5 tane sayının listeye atılması ve ardından karelerinin
20 azına göre sıralanması alıştırmasını yaptık.

a = []

for i in range(0,5):
    a.append(eval(input()))

def kare(n):
    return n*n-20

a.sort(key = kare)
print(a)

"""

#1-> if koşullu ifadesi

"""

# if __name__ == "__main__" ifadesi main function.!!!

a=5
c=4
d=-5
if a > c:
    print("a c'den büyüktür.")

if d < 0:
    print("d 0'dan küçüktür.")

if d>0: print("asdasd") ; print("eqgqwgqwg") ; d= 5

"""

#2-> elif (elseif) koşullu ifadesi

"""

a = 5
if a > 5:
    print("a 5'ten büyüktür.")
elif a==5:
    print("a 5'e eşittir.")
else:
    print("a 5'ten küçüktür.")
    
"""

#3-> ? (shortif) koşullu ifadesi

"""

# python'da herhangi bir shortif yoktur!

a = 5
b = 4

print("a ile b farklı") if a != b else print("a ile b aynı")

print("a büyük b") if a > b else print("a eşit b") if a==b else print("a küçük b")

"""

#4-> and / or koşullu ifadeleri

"""

a= 5
c=10
b=-4

if a<10 or c<10:
    print("a ya da c 10'dan küçük")
if a == 5 and c == 10:
    print("a 5e eşit ve c 10'a eşit")

"""

#5-> is koşulu

"""

a = 4
if a is 4:
    print("a 4'e eşit")
if a is not 4:
    print("a 4'e eşit değil")

"""

#6-> iç içe koşullu ifade

"""

a=4
c=11
if a<5:
    if c>10:
        print("Merhaba dünya!")
        
"""

#7-> pass koşullu ifade

"""

a=5

if a>5:
    pass
print("Hellooo!")

"""

#8-> while döngüsü

"""

a = 5
while a < 15:

    a += 1
    if a == 8:
        continue    #o aşamayı atlar.
    if a == 12:
        break   #bitirir.
    print(a)
else:
    print("a artık 15 ya da daha büyük")
    
"""

#9-> for döngüsü

"""
for i in range(0,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)

liste = ["as",True,1.9,5,["asdsa","sdf","assert"]]
for i in liste:
    print(i)
for i in liste[4]:
    print(i)
for i,eleman in enumerate(liste): #liste içindek index'i de çekmek için!
    print(i+1,". eleman: ", eleman, sep="") #sep(seperator) normalde boşluktur. Virgül ile ayrılan kısımlar boşluk olmasın diye bu şekilde kullanılabilir.

for i in range(0,3):
    print(i)
else:
    print("For bitti !")

"""

#10-> Fonksiyon (def)

"""

def yazdir():
    print("yazıyorum")

yazdir()

def topla(a,b):
    return a+b

print(topla(3,5))

def topla_carp(a,b):
    return a+b,a*b

print(topla_carp(3,5))

toplam, carpim = topla_carp(3,5)
print(toplam,carpim,sep=",")

def topla_ne_varsa_git(*a):
    toplamlar = 0
    for deger in a:
        toplamlar += deger
    return toplamlar

print(topla_ne_varsa_git(3,5,9,15,36))

def toplaa(*toplanacak,fazladan=0):
    toplaam = 0
    for deger in toplanacak:
        toplaam += deger + fazladan
    return toplaam

print(toplaa(3,5,9,15.2,36,fazladan=2))

def birim_islem(**birim):
    print("Birim adı : " + birim["ad"])
    print("Birim Tipi : " + birim["tip"])
    print("Birim Yılı : " + birim["yil"])

birim_islem(ad="Balıkesir",tip = "Üniversite", yil = "1992")

lambda_fonksiyonu = lambda a: a + 10

print(lambda_fonksiyonu(5))

cok_parametre = lambda a,b: a+b

print(cok_parametre(3,5))


def benim_fonskiyonum(n):
    return lambda a:a *n

katini_al = benim_fonskiyonum(2)        #BUNUN KLLANIMINI ÖĞREN!!
print(katini_al(5))

katini_al = benim_fonskiyonum(5)
print(katini_al(5))

"""
