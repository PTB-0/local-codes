import time as zamanci


kitaplar = []    
çalışanlar = []
üyeler = []

def kitapEkle(kitaplar,kitapVerisi):
    kitapSozluk = {}
    kitapBilgileri = kitapVerisi.split(",")  # "suç ve ceza,1816"  -> ["bu","bir","metindir"]
    kitapSozluk["yazar"] = kitapBilgileri[0].strip()
    kitapSozluk["başlık"] = kitapBilgileri[1].strip()
    kitapSozluk["yayın yılı"] = kitapBilgileri[2].strip()
    kitapSozluk["kod"] = kitapBilgileri[3].strip()
    kitapSozluk["kategori"] = kitapBilgileri[4].strip()
    kitapSozluk["stok durumu"] = kitapBilgileri[5].strip()
    kitaplar.append(kitapSozluk)
    
    return kitapSozluk

def kitapSil(kitapAdi , kitapNum):
    kitapAdi = input("silmek istediğiniz kitapın adını yazınız")
    if kitaplar.count(kitapAdi) == 1 :
        kitaplar.remove(kitapAdi)
        print("kitap başarıyla silindi")
    elif kitaplar.count(kitapAdi) == 0 :
        print("bu kitap bulunamıyor")
        wanna = input("bu kitabı eklemek istermisiniz")
        if wanna == "evet" :
            kitapEkle()
    else :
        kitapNum = input("kitabın numarasınıda girermisiniz")
        if kitaplar.count(kitapNum) == 1 :
            kitaplar.remove(kitapNum)
    
    pass
def kitapListele():
    pass
def kitapAra():
    pass
def kitap_guncelle():
    pass    
def kitap_satin_al():
    pass
def calisan_ekle():
    pass
def calisan_sil():
    pass
def calisan_listele():
    pass
def calisan_ara():
    pass
def calisan_guncelle():
    pass
def uye_ekle():
    pass
def uye_sil():
    pass
def uye_listele():
    pass
def uye_ara():
    pass
def uye_guncelle():
    pass    
    
while True:
    print("Kütüphane Otomasyon Sistemine Hoşgeldiniz")
    print("1. Kitap İşlemleri")
    print("2. Çalışan İşlemleri")
    print("3. Üye İşlemleri")
    print("4. Çıkış")
    
    kullanici_secimi = input("Lütfen bir seçenek girin (1-4): ")
    
    if kullanici_secimi == "1":
        print("Kitap İşlemleri Seçildi.")
        # Kitap işlemleri fonksiyonları burada çağrılacak
        print("a. Kitap Ekle")
        print("b. Kitap Sil")
        print("c. Kitap Listele")
        print("d. Kitap Ara")
        print("e. Kitap Güncelle")
        print("f. Kitap Satın Al")
        kitap_islem_secimi = input("Lütfen bir seçenek girin (a-f): ")
        if kitap_islem_secimi == "a":
            print("Kitap Ekleme İşlemi Seçildi.")
            kitapVerisi = input("Kitap bilgilerini girin (yazar, başlık, yayın yılı, kod, kategori, stok durumu) virgülle ayrılmış şekilde: ")
            kitapSozluk = kitapEkle(kitaplar,kitapVerisi)
            
            print("Kitap başarıyla eklendi.")
            print("eklenen kitap : ",kitapSozluk)
            print("kitaplar verisi : ",kitaplar)
            
            """
            ödev 122-136 yapılacak 56-65 e kadar yapılacak
            """
        elif kitap_islem_secimi == "b":
            print("Kitap Silme İşlemi Seçildi.")
            # Kitap silme fonksiyonu burada çağrılacak
        elif kitap_islem_secimi == "c":
            print("Kitap Listeleme İşlemi Seçildi.")
            # Kitap listeleme fonksiyonu burada çağrılacak
        elif kitap_islem_secimi == "d":
            print("Kitap Arama İşlemi Seçildi.")
            # Kitap arama fonksiyonu burada çağrılacak
        elif kitap_islem_secimi == "e":
            print("Kitap Güncelleme İşlemi Seçildi.")
            # Kitap güncelleme fonksiyonu burada çağrılacak
        elif kitap_islem_secimi == "f":
            print("Kitap Satın Alma İşlemi Seçildi.")
            # Kitap satın alma fonksiyonu burada çağrılacak
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
        
    elif kullanici_secimi == "2":
        print("Çalışan İşlemleri Seçildi.")
        # Çalışan işlemleri fonksiyonları burada çağrılacak
    elif kullanici_secimi == "3":
        print("Üye İşlemleri Seçildi.")
        # Üye işlemleri fonksiyonları burada çağrılacak
    elif kullanici_secimi == "4":
        print("Sistemden çıkılıyor. İyi günler!")
        break
    print(kitaplar)
    
    
print(kitaplar)