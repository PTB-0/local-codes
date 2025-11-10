import os

if os.path.exists("sözlük") == False :
    os.mkdir("sözlük")

print("Kişisel sözlüğe hoş geldiniz")
while True:
    mod = input("Ne yapmak istersiniz ? \n")
    if mod == "yazmak" :
        kelime = input("Kelimeniz nedir? \n")
        pathK = kelime + ".txt"
        if os.path.exists("C:\\Users\\USER\\Desktop\\local-codes\\sözlük\\" + pathK) :
            print("Böyle bir kelime var")
            do = input("ne yapmak istersiniz")
            if do == "silmek" :
                os.remove(pathK)
                print("başarı ile silindi")
            elif do == "eklemek" :
                pathTam = "C:\\Users\\USER\\Desktop\\local-codes\\sözlük\\" + pathK
                yazi = input("\n ne yazmak istersiniz ? \n")
                f = open(pathTam , "+a")
                f.write(yazi)
        else :
            f = open(pathK , "a")
            yazi = input("yazmak stediğinizi yazınız")
            f.write(yazi)
#çalışmıyor dosya döngüsü var