import random
randomList = ["A", "B" , "C" , "D" , "E" , "F" , "G" ,"a","b","c","d","e","f"]
kullanicilar = []
kullanici = {}
def checker(kullanimTuru , kullaniciAdi = None , ID = None ) :
    if kullanimTuru == "nameTag" :
        for kullanici in kullanicilar :
            if kullanici['nameTag'] == kullaniciAdi :
                return 1
"""
    elif kullanimTuru == "ID" :
        for kullanici in kullanicilar :
"""    
     # bu doaha sonra bu kullanıcının gerçekten var olup olmadığını kontrol edicicek ve eğer varsa return 1 yaparak bunu belirticek
def kullaniciOlustur() :
    while True :
        kullaniciAdi = input("kullanıcı adınızı girin")
        gercekAd = input("gerçek adınızı giriniz")
        returns = checker("nameTag" , kullaniciAdi)
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
        kullanici = {
            "nameTag" : kullaniciAdi ,
            "realName" : gercekAd ,
            "ID" : a ,
            "passwd" : passwd            
        }
        kullanicilar.append(kullanici)
        