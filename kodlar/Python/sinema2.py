koltuklar = []
filmler = []
farkliHarflerSayisi = []
options = 2 #burda kaç atne seçenek varsa  o sayıyı bunla değiştirin yani eğer 3 seçenek varsa bu sayıyı 3 yapın

def filmDuzenlemek() :
    tekrar = int(input("kaç tane film gireceksiniz"))
    for i in range(tekrar):
        ad = input("filmin adı ney")
        kS = int(input("kaç koltuk olacak"))
        for i in range(kS) :
            koltuk = input("koltuğu giriniz")
            koltuklar.append(koltuk)
        print("Film : \n" , ad , "Koltuk sayısı : \n" , kS , "Koltuklar : \n" , koltuklar )
        yapilanFilm = {
                "Film Adı" : ad ,
                "Koltuk Sayısı" : kS ,
                "Koltuklar" : koltuklar.copy()
                
            }
        filmler.append(yapilanFilm)
        print(filmler)
        koltuklar.clear()

    
def filmIzlemek() :
    if not filmler :       #not yok demek oluyop burda
        print("Suanda kayıt olabileceğiniz film bulunmamaktadır")
    else :   # bu bahsettiğim seyin seçeneği diğil
        secilenFilm = 1
        for yapilanFilm in filmler :
            print( secilenFilm, "." , yapilanFilm['Film Adı'])
            secilenFilm += 1
        Film = int(input("Hnagi filmi izlemek istersiniz"))
        Film -= 1
        print(filmler[Film]['Koltuklar'])
        kisi = int(input("kaç kişi olucak"))
        for i in range(kisi) :
            secilenKoltuk = input("Koltuğunuzu seçin")
            secilenFilm = filmler[Film]
            if secilenFilm["Koltuklar"].count(secilenKoltuk) != 0 :
                secilenFilm["Koltuklar"].remove(secilenKoltuk)
            else :
                print("BU KOLTUK DOLU VEYA GEÇERSİZ")

def tahmin() :
    farkliHarfler = set("film düzenlemek") ^ set(ask)
    x = len(farkliHarfler)
    farkliHarflerSayisi.append(x)
    farkliHarfler = set("film izlemek") ^ set(ask)
    x = len(farkliHarfler)
    farkliHarflerSayisi.append(x)
    for i in range(options):
        print(farkliHarflerSayisi)
        x = farkliHarflerSayisi.pop()
        y = farkliHarflerSayisi.pop()
        if len(farkliHarflerSayisi) != 0 :
            if x > y :
                y = farkliHarflerSayisi.pop()
            elif x < y :
                x = farkliHarflerSayisi.pop()
        else :
            if x > y :
                filmDuzenlemek()
                break
            elif x < y :
                filmIzlemek()
                break
            else :
                import random as rasgele
                
                if rasgele.randint(1 , options) == 1 :
                    filmDuzenlemek()
                    break
                else :
                    filmIzlemek()
                    break


while True :
    ask = input("Ne yapmak istersiniz")
    if ask == "film düzenlemek" :  # bu bahsettiğim seyin seçeneği
        filmDuzenlemek()
    elif ask == "film izlemek" :
        filmIzlemek()
    else : #else olduğu için buda diğil ama olanlarla aynı sütünda 
        tahmin()