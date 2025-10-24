adlar = []
kitaplar = []
def kitapEkle(kitaplar,kitapVerisi):
    kitapAdi = input("kitabın sistemdeki adını girermisiniz")
    if kitaplar.
        kitapSozluk = {}
        kitapBilgileri = kitapVerisi.split(",")  # "suç ve ceza,1816"  -> ["bu","bir","metindir"]
        kitapSozluk["yazar"] = kitapBilgileri[0].strip()
        kitapSozluk["başlık"] = kitapBilgileri[1].strip()
        kitapSozluk["yayın yılı"] = kitapBilgileri[2].strip()
        kitapSozluk["kod"] = kitapBilgileri[3].strip()
        kitapSozluk["kategori"] = kitapBilgileri[4].strip()
        kitapSozluk["stok durumu"] = kitapBilgileri[5].strip()
        kitaplar.append(kitapSozluk)