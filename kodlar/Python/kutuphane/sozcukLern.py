kitaplar = []
def kitapEkle():
    kitapOzellikleri = {
        "kitapAdi" : input("kitabın adı ne"),
        "yazar" : input("yazar kim") ,
        "sayfa" : int(input("sayfa sayısı")) ,
        "tür" : input("türü ne") 
        }
    kitaplar.append(kitapOzellikleri)
def kitapSil() :
    kitapO = input("silmek istediğiniz kitabı giriniz")
    kitaplar.remove(kitapO)
    
def kitapAra():
    serching = input("aranan kitabın adını giriniz")
    for kitap in kitaplar :
        if  kitaplar["kitapAdi"].lower() == serching.lower():
            print(kitaplar)