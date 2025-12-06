from os import *
print("UYGULAMA AÇMAYA HOŞ GELDİNİZ \n")
def uygulamaAcma() :
    global yol
    yol = input("yolu girin")
    if yol == "" :
        print("boş bırakma")
        return
    try :
        yol =  input("yolu gir")
        return
    except ValueError :
        print("bir yol girmen lazım")
    system(yol)
while True :
    if uygulamaAcma() :
        break
    else :
        global cikis
        cikis = int(input("çıkış 1 çıkma 0"))
        if cikis == "" :
            print("boş bırakmaman lazım")
            continue
        try :
            cikis = int(input("düzgünce 1 veya 0 gir "))
        except ValueError :
            print("hata oldu tekrar dene")
        if cikis == 0 :
            print("devam ediliyor")
            continue
        elif cikis == 1 :
            print("çıkılıyor")
            break
        else :
            print("yanlış bir şey oldugu için çıkılıyor")
            break
system("C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\pythonTest.py")
