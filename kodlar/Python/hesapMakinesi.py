import time
opDegeri = int()
opDegeri = 1
while  opDegeri == 1 :
    birinciSayi = input("sayı girin\n")
    ikinciSayi = input("sayı gir birdaha\n")
    time.sleep(1)
    sayiBir = int(birinciSayi)
    sayiBaska = int(ikinciSayi)
    kararSayisi = input("ne işlemi 1 toplama 2 çıkarma 3 çarpma 4 bölme 5 üslü\n")
    if kararSayisi == "1" :
        print(sayiBaska + sayiBir)
    elif kararSayisi == "2" :
        print(sayiBir - sayiBaska)
    elif kararSayisi == "3" :
        print(sayiBir*sayiBaska)
    elif kararSayisi == "4" : 
        print(sayiBir/sayiBaska)
    elif kararSayisi == "5" :
        print(sayiBir ** sayiBaska)
    else : 
        print("hatalı giriş yaptınız")
    time.sleep(1)
    kararSayisi = input("devam etmek istiyomusunuz 1/0")
    kararSayisiWhile = int(kararSayisi)
    if  kararSayisiWhile == 0 :
        print("çıkıs yapılıyor")
        opDegeri = 0


        
