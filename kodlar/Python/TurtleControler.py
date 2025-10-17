import time
import turtle
while True :
    a = input("kaplumbağa ne yapsın")
    if a == "ileri" :
        Num = int(input("ne kadar ileri gitsin"))
        if Num > 0 :
            turtle.forward(Num)
        else :
            print("bunu yapamam")
    elif a == "geri" :
        Num = int(input("ne kadar geri gitsin"))
        if Num > 0 :
            turtle.back(Num)
        else: 
            print("bunu yapamam")
    elif a == "renk değişimi" :
        Num = input("ne renk olsun")
        turtle.color(Num)
    elif a == "daire" :
        Num = int(input("yarı çapını yazın"))
        if Num > 0 :
            turtle.circle(Num)
        else :
            print("bunu yapamam")
    elif a == "bekle" :
        Num = int(input("nekadar beklesin"))
        if Num > 0 :
            turtle.delay(Num)
        else : 
            print("bunu yapamam")
    elif a == "klonla" :
        turtle.clone
    elif a == "dön" :
        nereye = input("nereye sağa mı sola mı")
        if nereye == "sağ" :
            Num = int(input("ne kadar dönsün"))
            if Num <= 90 and Num > 0 :
                turtle.right(Num)
        elif nereye == "sol" :
            Num = int(input("ne kadar dönsün"))
            if Num <= 90 and Num > 0 :
                turtle.left(Num)