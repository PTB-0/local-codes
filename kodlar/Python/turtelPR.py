import turtle
turtle.turtlesize(1)
global derece
derece = 0
global adim
adim = 0

def adimSecimi() :
    global adim
    try:
        adim = int(input("bu yöne ne kadar gitmek istersiniz negatif adım sayılmıyor"))
        if adim < 0 or adim > 99999:
            while adim < 0 or adim > 99999:
                try:
                    adim = int(input("sayı ya sıfırın altında yada üst sınır olan 100000 e eşit veya yüksek"))
                except ValueError:
                    print("düzgünce bir sayı gir")
        return
    except ValueError:
        print("düzgünce bir sayı yaz")
        return

                
    
def dereceSecimi() :
    global derece
    try:
        derece = int(input("tamam bana bir derece ver"))
        if derece > 360 or derece < 0:
            while derece > 360 or derece < 0:
                try:
                    derece = int(input("tamam bana bir derece ver ama 360 - 0  arasında olsun"))
                except ValueError:
                    print("düzgünce gir")
        return
    except ValueError:
        print("düzgünce sayı girmeni istedim sadece sayı")
        return

titleNe = input("title ne olsun")
turtle.title(titleNe)
while True :
    yon = input("sağ sol ileri geri veya çıkış ")
    if yon == "sağ" :
        dereceSecimi()
        turtle.right(derece)
    elif yon == "sol" :
        dereceSecimi()
        turtle.left(derece)
    elif yon == "ileri" :
        adimSecimi()
        turtle.forward(adim)
    elif yon == "geri" :
        adimSecimi()
        turtle.back(adim)
    elif yon == "çıkış" :
        break
mod = input("script yada full çıkış")
if mod == "script" :
    mod = int(input("1 , 2 , 3 , 4 , 5 , 6"))
    if mod == 1 :
        turtle.right(90)
        turtle.forward(100)
        