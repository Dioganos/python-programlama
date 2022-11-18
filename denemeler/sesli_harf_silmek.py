kelime = list(input("kelime giriniz :"))
i = 0
sesliler = "aeıioöuü"

for x in kelime:
    for y in sesliler:
        if y == x:
            kelime[i] = ''
    i += 1

a = ""

for b in kelime:
    a += b

print(a)