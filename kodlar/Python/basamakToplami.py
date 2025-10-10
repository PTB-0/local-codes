global c
global a
a = 0
c = 0
global rem
global basamakSayisi
global b
while True :
    a = 0
    rem = 0
    c = 0
    basamakSayisi = 0
    b = 0
    try :
        a = input("bir sayı giriniz")
        b = int(a)
    except ValueError :
        print("sayı girmeniz lazım")
        continue
    basamakSayisi = len(a)
    for i in range(len(a)+1) :
        ram = (b // (10 ** basamakSayisi)) % 10
        c = c + ram
        basamakSayisi = basamakSayisi-1
    print(c)