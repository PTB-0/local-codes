"""
kelimeleri otomatik hafızadaki kelimelerden hangisine benziyorsa ona çevirmesini sağlayacağım
"""
import os
import time 
global dopamin
global ram
dopamin = 0 # Gelecekteki arada kalıkndığında hangisinin seçilmseini sağlayacak olan değişken
kelimeler = []
oncekihatalar = [] 
folderPath = r"C:\\Users\\USER\Desktop\\local-codes\\kodlar\\Python\\kelimeler"  # DB txt veya json dosyalarının olduğu konum
def kelimeAlici(eklenenKelime = None) :    # Kelimwyi Ram e ekliyor 
    if eklenenKelime == None  or eklenenKelime == "" :  #kelime çağrılırken girilmişmi girilmemişmi eğer girilmiş ise direk eklemeye başla girilmemiş ise kelimeyi gir
        eklenenKelime = input("hafızaya eklemek istediğiniz kelimeyi yazınız").lower()
        for kelime in kelimeler :    # eklenecek kelime zaten eklimi
            if eklenenKelime == kelime['TrueK'] :
                print("Bu kelime zaten ekli")
                return
        kelime = {  # değilse ekle
            "TrueK" : eklenenKelime,
            "oncekiHatalar" : oncekihatalar.copy() ,   #böylece eğer önceki hatalarda varsa tamamen baştan her kelime ile karşılaştırmak gerekmicek
            "Dopamin" : dopamin
        }
        kelimeler.append(kelime)   #kelimeler listine ekle
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
def controller() : #kontrol amaçlı zorunlu diğil ama dopamin kullanılmak istiyorsanız zorunlu
    checkTrue = input("doğru düzelti yapıldımı ?").lower()
    if checkTrue in ["evet" , "doğru düzelti yapıldı" , "yapıldı"] :
        print("Bu harika")
        dopamin += 10   #doğru yaptığı için ödüllendirildi
        return 1
    else :
        print(kelimeler)
        inThere = input("kelimeniz burda varmı").lower()   #kelimenin cidden verilerde olup olmadığına bakıyor
        for kelime in kelimeler :
            if inThere == kelime['TrueK'] :   #varsa
                print("Kelimeniz :" , kelime['TrueK'] , "\n" , "Eğer yapılmısa bunlarda Önceki Hatalarınız : \n" , kelime['oncekiHatalar'])  #yazdır
                return 0
        kelimeAlici(ram) # eğer bulamaz ise kelimeyi ekliyor
def kelimeChecker(yazilanKelime = None) :   #kelimenin doğru yazılımının bulunmasını sağlar
    lastBiggestNum = 0   
    while True :  
        if yazilanKelime == ""  or yazilanKelime == None :  # yine eğer kelime boş veya girilmemiş ise bir kelime girmeye zorluyor
            yazilanKelime = input("kelimenizi girin").lower()
        else : 
            ram = yazilanKelime
            break
    for kelime in kelimeler :    #kelimelerin içinde dolaşıyoruz
        i = 0
        farkliHarfler = set(kelime['TrueK']) ^ set(yazilanKelime)  #farklı olan harfleri liste yapıp koyuyoruz
        farkNum = len(farkliHarfler)   #önemli olan farklı karekterlerin sayısı olduğu için sayısını alıyoruz
        if lastBiggestNum > farkNum or i <= 0 :  # daha önceki fark daha fazla ise veya ilk defa yapıyorsam 
            lastKelime = kelime['TrueK'] # suanki kelimeyi son kelimenin yerine koyuyor
            lastBiggestNum = len(lastKelime)  #bunun uzunluğunu alıyor
            lastBiggestIndex = kelimeler.index(kelime)
            print(lastBiggestIndex)
        elif lastBiggestNum == farkNum :
            if lastKelime['Dopamin'] < kelime['Dopamin'] :
                lastKelime = kelime['TrueK'] # suanki kelimeyi son kelimenin yerine koyuyor
                lastBiggestNum = len(lastKelime)  #bunun uzunluğunu alıyor
                lastBiggestIndex = kelimeler.index(kelime)
                print(lastBiggestIndex)
        i += 1 
    check = controller()
    if check == 1 :
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
            with open(filePath, "r", encoding="cp1254") as f:       #nOT ÖNCE AD SONRA DOPAMİN GELECEK ŞEKİLDE GELİŞTİMEM LAZIM
                data = f.read()
                kelimeAlici(data)
def hepsiniDBekle() :
    ramList = []
    for kelime in kelimeler :
        ramList.append(kelime['TrueK'])
    kaliciHafizaEkle(ramList)
def yazdir() :
    print("tüm kelimeler yazdırılıyor")
    for kelime in kelimeler :
        print("\n" , kelime)
    print("hepsi yazıldı")
def dopaminTouch(SELECTION = None) :
    if SELECTION == None or SELECTION == "":
        print("bir kelime veya hepsini seçiniz")
        i = 0
        for kelime in kelimeler : 
            print("[",i,"]", kelime['TrueK' , 'Dopamin'])
            i += 1
        SELECTION = input("hangisini seçmek istersiniz")
    for i in range(SELECTION) :
        a = kelime
        if i == SELECTION :
            print(a)
            change = int(input("dopamini ne yapıcaksınız"))     
            a['Dopamin'] = change
            print(a)       
def asker() :
    print("0. çıkış \n 1. kelime eklemek \n 2. kelime doğrulama \n 3. DB ye ulaşma \n 4. Hafızaya Kalıcı olarak ekle \n 5. tüm kelimeleri DB ye ekle \n 6. tüm kelimeleri yazdır \n 7. dopamini değitir \n")
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
    elif ask in ["6" , "6."] :
        yazdir()
        time.sleep(3)
        print(len(kelimeler) , "tane kelime var")
    elif ask in ["7" , "7."] :
        dopaminTouch()
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
    dopamin == 0
while True :
    asker()