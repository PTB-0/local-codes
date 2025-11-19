import random
randomList = ["A", "B" , "C" , "D" , "E" , "F" , "G" ,"a","b","c","d","e","f"]
kullanicilar = []
kullanici = {}
global num
num = -1
def checker(kullanimTuru , selection = None , theObj = None) :
    listOfChoise = ["0. ID" , "1. KULLANICI ADI" , "2. GERÇEK AD"]
    listOfSee = ["ID" , "nameTag" , "realName"]
    copy = listOfSee.copy() 
    while True :
        if selection == None :
            print("sayı girin")
            ask = int(input(listOfChoise))
        else :
            ghostForlistOfChoise = listOfChoise.copy()
            for i in range(len(listOfChoise)-1):
                print(i)
                forSelection = ghostForlistOfChoise.pop(i)
                if selection == forSelection :
                    ask = i 
            if ask == i  :
                break
            else :
                selection = None
    pull = copy.pop(ask)
    if kullanimTuru == "ara" :
        for kullanici in kullanicilar :
            if kullanici[pull] == theObj :
                num = kullanici['sıra']
                return 1
        return 0
"""
    elif kullanimTuru == "ID" :
        for kullanici in kullanicilar :
"""    
     # bu doaha sonra bu kullanıcının gerçekten var olup olmadığını kontrol edicicek ve eğer varsa return 1 yaparak bunu belirticek
def kullaniciOlustur() :
    while True :
        kullaniciAdi = input("kullanıcı adınızı girin")
        gercekAd = input("gerçek adınızı giriniz")
        returns = checker("ara","nameTag" , kullaniciAdi)
        if returns != 0 :
            print("üzgünüm bu kullanıcı adı alınmış tekrar deneyin")
        passwd = input("şifrenizi giriniz")
        passwd2 = input("şifrenizi doğrulayın")
        if passwd != passwd2 :
            print("girdiğiniz şifreler birbirleriyle uyuşmuyor")
        for i in range(4):
            selectionList = str(random.randint(0,9))
            a = a +""+selectionList
        selectionList = random.randint(0,len(randomList))
        chrForID = randomList.pop(selectionList)
        a = a +""+ chrForID
        checker("ara" ,"ID",a )
        sira = len(kullanicilar) 
        kullanici = {
            "nameTag" : kullaniciAdi ,
            "realName" : gercekAd ,
            "ID" : a ,
            "passwd" : passwd,
            "sıra" : sira            
        }
        kullanicilar.append(kullanici)
def kullaniciGir(LogAd , Passwd) :
    check = checker("ara","nameTag",LogAd)
    if checker == 1 :
        for i in range(num):
            a = kullanici
        if a['passwd'] != Passwd :
            print("tekrar dene")
            Passwd = input("şifreyi giriniz")
            sinirDeneme += 1

kullaniciOlustur()
kullaniciOlustur()
kullaniciGir("Ege" , "1234")