"""
kelimeleri otomatik hafızadaki kelimelerden hangisine benziyorsa ona çevirmesini sağlayacağım
"""
import os
import time 
global dopamin
global ram
dopamin = 0
kelimeler = []
oncekihatalar = []
folderPath = r"C:\\Users\\USER\Desktop\\local-codes"
def kelimeAlici(eklenenKelime = None) :
    if eklenenKelime == None  or eklenenKelime == "" :
        eklenenKelime = input("hafızaya eklemek istediğiniz kelimeyi yazınız").lower()
        for kelime in kelimeler :
            if eklenenKelime == kelime['TrueK'] :
                print("Bu kelime zaten ekli")
                return
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy() ,
            "Dopamin" : dopamin
        }
        kelimeler.append(kelime)
    else : 
        for kelime in kelimeler :
            if kelime['TrueK']  == eklenenKelime :
                print("üzgünüm ama bu kelime : \n" , eklenenKelime , "\n zaten ekli")
                return
        kelime = {
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy() ,
            "Dopamin" : dopamin
        }
        kelimeler.append(kelime)
    print(kelime)
def kelimeChecker(yazilanKelime = None) :
    lastBiggestNum = 0
    while True :
        if yazilanKelime == ""  or yazilanKelime == None :
            yazilanKelime = input("kelimenizi girin").lower()
        else : 
            ram = yazilanKelime
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
        "oncekiHatalar" : oncekihatalar.copy() ,
        "Dopamin" : dopamin
    }
    oncekihatalar.clear()
    return lastKelime 
def kaliciHafizaEkle(willAdd = None) :
    if willAdd == "" or willAdd == None :
        willAdd = input("Eklenecek kelimeyi giriniz (eğer birden fazla kelime giriyorsanız virgül ile ayırabilirsiniz lütfen boşluk koymayın)").lower().split(',')
        print("eklemek istediğiniz kelimeler bunlarmı : \n" , willAdd)
        onay = input("Evet/hayır").lower()
        if onay == "hayır" :
            while True :
                willAdd = input("kelimeleri veya kelimeyi giriniz (virgüllerle ayırın boşluk kullanmayın)").lower().split(',')
                onay = input("hepsi doğrumu \n Evet/hayır").lower()
                if onay in ["" , "e" , "evet"] :
                    break
    for i in range(len(willAdd)) :
        fileName = willAdd[i] + ".txt"  
        if  os.path.exists(fileName) == False :    
            f = open(fileName , "w")  
            f.write(willAdd[i])   
            kelimeAlici(willAdd[i])    
        else :
           print("bu kelime zaten hafızada varolduğundan eklenemiyor : \n" , willAdd[i])    
def DisHafizayaEris():
    for filename in os.listdir(folderPath):
        if filename.endswith(".txt"): 
            filePath = os.path.join(folderPath, filename)
            with open(filePath, "r", encoding="cp1254") as f:
                data = f.read()
                kelimeAlici(data)
def controller() : #kontrol amaçlı zorunlu diğil ama dopamin kullanılmak istiyorsanız zorunlu
    checkTrue = input("doğru düzelti yapıldımı ?").lower()
    if checkTrue in ["evet" , "doğru düzelti yapıldı" , "yapıldı"] :
        print("Bu harika")
        dopamin += 10
    else :
        print(kelimeler)
        inThere = input("kelimeniz burda varmı").lower()
        for kelime in kelimeler :
            if inThere == kelime['TrueK'] :
                print("Kelimeniz :" , kelime['TrueK'] , "\n" , "Eğer yapılmısa bunlarda Önceki Hatalarınız : \n" , kelime['oncekiHatalar'])
                return
        kelimeAlici(ram)
def hepsiniDBekle() :
    for kelime in kelimeler :
        kaliciHafizaEkle(kelime['TrueK'])
def asker() :
    print("0. çıkış \n 1. kelime eklemek \n 2. kelime doğrulama \n 3. DB ye ulaşma \n 4. Hafızaya Kalıcı olarak ekle \n 5. tüm kelimeleri DB ye ekle")
    ask = input("Ne yapmak istersiniz ? \n")
    if ask in ["0" , "0."] :
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
    elif ask in ["4" , "4."] :
        kaliciHafizaEkle()
    elif ask in ["5" , "5."] :
        hepsiniDBekle()
        print("başarı ile eklendi")
    elif ask in ["-1"] :
        print("dev op center")
        print(kelimeler)
        time.sleep(2)
        for kelime in kelimeler :
            print(kelime['TrueK'])
        print(dopamin)
        print(folderPath)
    else :
        print("dev modunda olduğu için çıkılıyor")
        quit() #bunu koydum çünkü burda kodu başlata bastığımda eğer burdaysa kod başlamıyor onun yerine asker() başlıyor eski versiyonu ile
while True :
    asker()