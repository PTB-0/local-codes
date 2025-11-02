"""
kelimeleri otomatik hafızadaki kelimelerden hangisine benziyorsa ona çevirmesini sağlayacağım
"""
global dopamin
dopamin = 0
global dopaminRam
dopaminRam = 0
kelimeler = []
oncekihatalar = []
def DisHafizayaEris():
    pass

def kelimeAlici(eklenenKelime = None) :
    if eklenenKelime == None  or eklenenKelime == "" :
        eklenenKelime = input("hafızaya eklemek istediğiniz kelimeyi yazınız").lower()
        for kelime in kelimeler :
            if eklenenKelime == kelime['TrueK'] :
                print("Bu kelime zaten ekli")
                return
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy()
        }
        kelimeler.append(kelime)
    else : 
        for kelime in kelimeler :
            if kelime['TrueK']  == eklenenKelime :
                print("üzgünüm ama bu kelime : \n" , eklenenKelime , "\n zaten ekli")
                return
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy()
        }
        kelimeler.append(kelime)
    print(kelime)

def kelimeChecker(yazilanKelime = None) :
    lastBiggestNum = 0
    while True :
        if yazilanKelime == ""  or yazilanKelime == None :
            yazilanKelime = input("kelimenizi girin").lower()
        else : 
            break
    for kelime in kelimeler :
        i = 0
        farkliHarfler = set(kelime['TrueK']) ^ set(yazilanKelime)
        farkNum = len(farkliHarfler)
        if lastBiggestNum > farkNum or i <= 0 :
            lastKelime = kelime['TrueK']
            lastBiggestNum = len(lastKelime)
            lastBiggestIndex = kelimeler.index(kelime)
            print(lastBiggestIndex)
        elif lastBiggestNum == farkNum :
            pass
        i += 1 
    oncekihatalar = kelime['oncekiHatalar']
    oncekihatalar.append(lastKelime)
    del kelimeler[lastBiggestIndex]
    kelime = {
        "TrueK" : lastKelime ,
        "oncekiHatalar" : oncekihatalar.copy()
    }
    oncekihatalar.clear()
    return lastKelime

def controller() : #kontrol amaçlı zorunlu diğil ama dopamin kullanılmak istiyorsanız zorunlu
    checkTrue = input("doğru düzelti yapıldımı ?").lower()
    if checkTrue in ["evet" , "doğru düzelti yapıldı" , "yapıldı"] :
        print("Bu harika")
        dopaminRam += 10
    else :
        print(kelimeler)
        inThere = input("kelimeniz burda varmı eğer yoksa kelimenizi yazınız").lower()
        for kelime in kelimeler :
            if inThere == kelime['TrueK'] :
                print("Kelimeniz :" , kelime['TrueK'] , "\n" , "Eğer yapılmısa bunlarda Önceki Hatalarınız : \n" , kelime['oncekiHatalar'])
                return
        kelimeAlici(inThere)

def asker() :
    print("0. çıkış \n 1. kelime eklemek \n 2. kelime doğrulama \n 3. DB ye ulaşma")
    ask = input("Ne yapmak istersiniz ? \n")
    if ask ["0" , "0."] :
        quit()
    elif ask in ["1" , "1."]:
        kelimeAlici()
    elif ask in ["2" , "2."] :
        girdi = input("kelimenizi giriniz")
        cikti = kelimeChecker(girdi)
        print(cikti)
        controller()
    elif ask in ["3" , "3."] :
        DisHafizayaEris()
    

while True :
    asker()