#WLOOK sonra bak
kullanicilar = []
def hesapEkle(kullaniciSifre , kullaniciAdi):
    kullanici = {}
    kullaniciAdi = input("kulllanıcı adını yazın").lower
    if kullanicilar.count(kullaniciAdi) >= 1 :
        print("üzgünüz ama bu hesap zaten oluşturulmuş \n")
        karar = input("başka bir ad denemek istermisiniz yoksa çıkmakmı istersiniz")
        if karar == "çıkmak" :
            return 1
    kullaniciSifre = input("şifrenizi giriniz")
    kullanici = kullaniciAdi , kullaniciSifre
    kullanicilar.append(kullanici)
    kullanicilar.append(kullaniciAdi)
    print(kullanicilar.count((kullaniciAdi , kullaniciSifre)))
def hesapSil(ad , sifre):
    ad = input("kullanıcı adını girin")
    sifre = input("şifrenizi girin")
    if kullanicilar.count((ad , sifre)) == 1 :
        kullanicilar.remove((ad , sifre))
        kullanicilar.remove(ad)
    elif kullanicilar.count((ad , sifre)) > 1 :
        karar = input("bu hesaptan" , kullanicilar.count((ad , sifre)) , "kadar bulunuyor hesapları silelimmi yoksa birleştirelimmi")
        if karar == "sil" :
            kullanicilar.remove((ad , sifre))
        else :
            kullanicilar.remove((ad , sifre))
            kullanicilar.append((ad , sifre))
def hesapGir(ad , sifre) :
    ad = input("hesap adını giriniz")
    if kullanicilar.count(ad) == 1 :
        sifre = input("şifreyi giriniz")
        kullanicilar.pop()
        if sifre == k
while True :
    