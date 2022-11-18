n = input("kac dizi girmek istersiniz ? : ")
u = ""
q = ""
t = ""
def yazdir(*a):
    toplam = 0
    sayi = 0
    for z in a:
        for x in z.split(","):
            toplam += int(x)
            sayi += 1
    return print(toplam / sayi)

dosya = open("a.txt", 'r')
kod = dosya.read()

for c in range(0,int(n)):
    exec(kod.replace("{}", str(c)).replace("[]",str(c+1)))
    r = "b"+str(c)
    q += (eval("{}".format(r))+ " ")
    t += r+","

eval("yazdir({})".format(t[:-1]))


dosya.close()


