
# Kütüphane Otomasyon Sistemi

"""
    kitap : 
        yazar, başlık, yayın yılı, kod, kategori, stok durumu
    çalışan :
        ad, soyad, çalışan no, pozisyon, iletişim bilgileri
    üye :
        ad, soyad, üye no, iletişim bilgileri, üyelik tarihi
    
    kitaplar = []    
    çalışanlar = []
    üyeler = []
    
    kitap ekle()
    kitap sil()
    kitap listele()
    kitap ara()
    kitap guncelle()
    kitap satın al()
    
    çalışan ekle()
    çalışan sil()
    çalışan listele()
    çalışan ara()
    çalışan guncelle()
    
    üye ekle()
    üye sil()
    üye listele()
    üye ara()
    üye guncelle()
"""
"""
    osman = {
        "isim" : "name",
        "soyisim" : "sdfsdjf"
    }
    
    osman["isim"]
"""
def kitap_ekle(kitaplar,kitap_verisi):
    kitap_sozluk = {}
    kitap_bilgileri = kitap_verisi.split(",")  # "suç ve ceza,1816"  -> ["bu","bir","metindir"]
    kitap_sozluk["yazar"] = kitap_bilgileri[0].strip()
    kitap_sozluk["başlık"] = kitap_bilgileri[1].strip()
    kitap_sozluk["yayın yılı"] = kitap_bilgileri[2].strip()
    kitap_sozluk["kod"] = kitap_bilgileri[3].strip()
    kitap_sozluk["kategori"] = kitap_bilgileri[4].strip()
    kitap_sozluk["stok durumu"] = kitap_bilgileri[5].strip()
    kitaplar.append(kitap_sozluk)
    
    return kitap_sozluk

def kitap_sil():
    #sözlükten diziden veri silme
    pass
def kitap_listele():
    pass
def kitap_ara():
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

kitaplar = []    
çalışanlar = []
üyeler = []
    
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
            kitap_verisi = input("Kitap bilgilerini girin (yazar, başlık, yayın yılı, kod, kategori, stok durumu) virgülle ayrılmış şekilde: ")
            kitap_sozluk = kitap_ekle(kitaplar,kitap_verisi)
            
            print("Kitap başarıyla eklendi.")
            print("eklenen kitap : ",kitap_sozluk)
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