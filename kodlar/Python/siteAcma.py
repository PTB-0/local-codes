import os

import time
import urllib.request
c = 1
while c == 1 :
    siteAdress = input("\nsiteyi giriniz örn: http://google.com/blahblah \n\n")
    html = urllib.request.urlopen(siteAdress)
    int(c)
    time.sleep(2)
    istek = input("bunu bir txt dosyasına yazdırmak istermisin ?")
    yazi = html.read().decode("utf-8")
    if istek == "evet" or istek == "olur" or istek == "1" :
        dosyaAdi = input("dosyanın adı ne olsun lütfen sonuna .txt veya onun gibi birşey eklemeyin")
        if dosyaAdi == "" :
            print("boş olamaz otomatik olarak adını html.txt koyuyoruz")
            dosyaAdi = "html.txt"
            continue
        elif (dosyaAdi == "html.txt") == False:
            
                
            dosyaAdi = dosyaAdi + ".txt" 
            if os.path.exists(dosyaAdi) == False :
                f = open(dosyaAdi , "x")
                global bK
                bK = 1
                continue
            elif os.path.exists(dosyaAdi) == True :
                if bK != 1 :
                    print("bu dosya daha önceeden varmış içinde öenmli bilgiler olabilir")
                    temizlik = input(" yinede dosyanın silinip baştan yazılmasını istermisiniz")
                    if temizlik == "evet" or temizlik == "olur" or temizlik == "isterim" :
                        os.remove(dosyaAdi)
                        f = open(dosyaAdi , "x")
                    else :
                        continue
                    
                        
                f  = open(dosyaAdi , "a")
                f.write(yazi)
            else :
                print("path sorunu var")
                break
            os.system("C:\\Users\\USER\\Desktop\\kodlar\\Python\\" + dosyaAdi)
        else :
            if os.path.exists(dosyaAdi) == False :
                f = open(dosyaAdi , "x")
            elif os.path.exists(dosyaAdi) == True :
                f  = open(dosyaAdi , "a")
                f.write(yazi)
            
    elif istek == "hayır" or istek == "gerek yok" or istek == "0":
        print("tamam")
        print("şimdi sitenin kodunu atıyorum \n")
        print(html.read())
    else :
        print("dediğin anlaşılmadı normal şekilde devam ediliyor")
    b = input("hey devammi 1/0")
    a = int(b)
    
    if a == 0 :
        time.sleep(1)
        c = 0
    else :
        c = 1
