global a 
global kullaniciSifre
global kullaniciAdi
global denemeler
import os
while True :
    kullaniciSifre = " "
    denemeler = 0
    a = input("hesaba girmekmi istersiniz hesapmı oluşturmak istersiniz")
    if a == "girmek" or a == "hesaba girmek" :
        kullaniciAdi = input("kullanıcı adını giriniz : \n")
        if kullaniciAdi == "python" :
            while denemeler < 3 :
                kullaniciSifre = input("lütfen hesabı için şifrenizi giriniz \n şifre : \n")
                if kullaniciSifre == "python123" :
                    print("DOĞRU ŞİFRE")
                    break
                elif denemeler == 3 :
                    print("hesap KİTLENDİ\n deneme hakkınızı doldurdunuz")
                    break
                else :
                    denemeler += 1
                    print("yanlış şifre kalan denemeler : \n" , 3 - denemeler )
        else :
            print("böyle bir kullanıcı bulunmamaktadır yeniden deneyiniz")
    elif a == "oluşturmak" :
        while True :
            kullaniciAdi = input("Kullanıcı adını girin lütfen")
            kullaniciAdiTxt = kullaniciAdi + ".txt"
            if os.path.exists(kullaniciAdiTxt):
                print("zaten böyle bir kullanıcı var tekrar deneyiniz")
            else:
                break
        open(kullaniciAdiTxt , "x")
        while True :
            kullaniciSifre = input("lütfen şifrenizi girin")
            if kullaniciSifre == "" or len(kullaniciSifre) < 5 :
                print("şifreniz çok kısa")
            else :
                break
        print("BAŞARILI\n")
        f = open(kullaniciAdiTxt , "a")
        f.write(kullaniciSifre + " " + kullaniciAdi)
        a  = input("hesaba girmek istermisiniz")
        if a == "evet" :
            kullaniciAdiRAM = input("Kullanıcı adı ney \n :")
            if kullaniciAdi == kullaniciAdiRAM :
                print("DOĞRU")
                kullaniciSifreRAM = input("Şifre neydi \n :")
                if kullaniciSifre == kullaniciSifreRAM :
                    print("doğru girişi yaptınız")
                else :
                    print("yanlış lütfen tekrar deneyiniz\n")
        else :
            print("devam ediliyor \n")        
    else :
        print("sanırım yanlış bişi girdiniz\n")
    devam = input("devam etmek istermisiniz\n")
    if devam == "evet" or devam == "1" or devam == "devam etmek isterim" :
        print("devam ediliyor")
    else :
        break
