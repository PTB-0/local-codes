#BASIC
#V1
#ALRF
from random import *
import time
import os
global sayi
global girdiSayisi
global bEski
bEski = 0
sayi = 0
girdiSayisi = 0
global tur 
tur = 0
global sSkor
sSkor = 0
global bSkor
bSkor = 0
def cikis() :
    tekrar = input("tekrar oynamak istermisin")
    if tekrar == "evet" or  tekrar == "tabiki" :
        print("hadi oynayalım\n")
    elif  tekrar == "hayır" or tekrar == "yok" :
        return
    else :
        print("bir hata oluşmuş")
        return
mod = input("mod")
while True :
    print("sayı tutma oyununa hoş geldiniz  100 ile 0 arasında sayı bulman lazım")
    oT = input("oyun tipi seçiniz:  bilgisiyar bulsun = bb ben bulayım = beb").lower()
    if oT == "beb" :
        sayi = randrange(100)
        if mod == "dev" :
            print("sayı :" , sayi)
            
        while tur <= 3:
            try :
                girdiSayisi = int(input("sayıyı tahmin etmeyi deneyin 100 ile 0 arasında\n"))
            except ValueError :
                print("HATA VARRR")
                continue
            if girdiSayisi >= 100 or girdiSayisi <= 0 :
                print("100 ile 0 arası derken onları dahil etmemiştim\n")
                while (girdiSayisi  >= 100 ) == True or  (girdiSayisi <= 0) == True :
                    try:
                        girdiSayisi = int(input("sayı gir 100 - 0 arasında\n"))
                    except Exception as e :
                        d = str(e)
                        if os.path.exists("hataloglari.txt"):
                            f = open("hataloglari.txt" , "a")
                            f.write(d)
                        else :
                            open("hataloglari.txt" , "x")
                            f = open("hataloglari.txt" , "a")
                            f.write(d)
                        print("yanlış bişi girdiniz \n")
                        print("tekrar deneyiniz \n")
                        continue
            elif girdiSayisi == sayi :
                print("KAZANDIN !!! \n")
                sSkor = sSkor+1
                break
            elif girdiSayisi < sayi :
                print("senin sayın" , girdiSayisi , "daha küçük")
            elif girdiSayisi > sayi :
                print("senin sayın olan" , girdiSayisi , "daha büyük")
            else :
                print("bir hata var")
            tur = tur+1 
        else :
            print("bir hata oluşmuş")
            break
    elif oT == "bb" :
        sayi = int(input("hadi sayını seç : \n"))
        print("şimdi bilgisiyar sayını bulmayı deniyor")
        global b 
        b = 100
        tur = 0
        while (tur <= 3) == True :
            if tur == 3 :
                sSkor = sSkor+1 
                break
            girdiSayisi = randrange(100)
            if girdiSayisi == sayi :
                print("bilgisiyar kazandı")
                bSkor = bSkor + 1
                break
            elif girdiSayisi < sayi :
                b = bEski 
                print("bilgisiyar bunu :" , girdiSayisi , "tahmin etti ama bu sayı senin seçtiğin" , sayi , "sayısından küçük ")
                b = randrange(100) 
                while (b <= bEski) == False :
                    b = randrange(100)
                    print(b , bEski)
                    if b > bEski :
                        break
                    else :
                        print(b)
                        time.sleep(4)
                tur = tur+1
            elif girdiSayisi > sayi :
                b = bEski
                print("bilgisiyar bunu :" , girdiSayisi , "tahmin etti ama bu sayı senin seçtiğin" , sayi , "sayısından büyük ")
                b = randrange(100)
                while (b >= bEski) == False :
                    b = randrange(100)
                    print(b , bEski)
                    if b < bEski :
                        break
                    else :
                        print(b)
                        time.sleep(4)
                tur = tur+1
            else :
                print("bir hata olmuş olması lazım \n")
    print("\nsenin skorun : " , sSkor , "\n")
    print("bilgisiyarın skoru : " , bSkor , "\n")
    cikis()