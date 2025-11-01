"""
kelimeleri otomatik hafızadaki kelimelerden hangisine benziyorsa ona çevirmesini sağlayacağım
"""
global dopamin
dopamin = 0
kelimeler = []
oncekihatalar = []
def DisHafizayaEris():
    pass

def kelimeAlici(eklenenKelime = None) :
    if eklenenKelime == None :
        eklenenKelime = input("hafızaya eklemek istediğiniz kelimeyi yazınız").lower()
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy()
        }
        kelimeler.append(kelime)
    else : 
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy()
        }
        kelimeler.append(kelime)
    print(kelime)

def kelimeChecker(yazilanKelime) :
    lastBiggestNum = 0
    while True :
        if yazilanKelime == "" :
            yazilanKelime = input("kelimenizi girin").lower()
        else : 
            break
    for kelime in kelimeler :
        print(kelime['TrueK'])
        farkliHarfler = set(kelime['TrueK']) ^ set(yazilanKelime)
        farkNum = len(farkliHarfler)
        if lastBiggestNum > farkNum or kelime < 0 :
            lastKelime = kelime['TrueK']
            lastBiggestNum = len(lastKelime)
            lastBiggestIndex = int(kelime)
        elif lastBiggestNum == farkNum :
            pass
    oncekihatalar = kelime['oncekiHatalar']
    oncekihatalar.append(lastKelime)
    kelimeler.remove(lastBiggestIndex)
    kelime = {
        "TrueK" : lastKelime ,
        "oncekiHatalar" : oncekihatalar.coppy
    }
    oncekihatalar.clear()
    return lastKelime

def controller() : #kontrol amaçlı zorunlu diğil
    checkTrue = input("doğru düzelti yapıldımı ?").lower()
    if checkTrue in ["evet" , "doğru düzelti yapıldı" , "yapıldı"] :
        print("Bu harika")
        dopamin += 10
    else :
        print(kelimeler)
        inThere = input("kelimeniz burda varmı eğer yoksa kelimenizi yazınız").lower()
        for kelime in kelimeler :
            if inThere == kelime['TrueK'] :
                print("Kelimeniz :" , kelime['TrueK'] , "\n" , "Eğer yapılmısa bunlarda Önceki Hatalarınız : \n" , kelime['oncekiHatalar'])
                return
        kelimeAlici(inThere)
        
kelimeAlici()
kelimeAlici()
a = input("s").lower()
b = kelimeChecker(a)
print(kelimeler)
print(b)