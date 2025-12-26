"""
CanISee için :
        # # #
        # 1 #
        3 # #
        3 : AI
        1 : Engel
        AI ın blockundan başlayarak sırayla x + 1 x + 2  diye bakıyor sınırda geldiğide artık aı dan y yi artırıyor yani ilk başta şu oluyor :
                                                                            K  ?  ?
                                                                            K  ?  ?
                                                                            3  K  K
                                                                            SUAN ? işaretleri bilinmez 
                                                                            sonra AI ın x ini ve y sini bir artırıyor engel var o zaman o nun kalanını yapamaz durdur o tarafı gibi

isVisible Kodları ve anlamları :
0 : hayır görünmüyor
1 : evet görünüyor
9 : bilinmiyor 
2 3 4 5 6 7 8 : şuanki versionda bunların bir anlamı yok ama ilerde sisli bulanık gibi olabilmesi için buraları boş bıraktım
                                                                            PLAN
                oyuncu AI ile Düşman AI in aynı yerden gelmesi sorun oluştururmu
                mapın hepsini araması çok yanlış onun yerine o yerin arkasını aramasın
                ERROR NUMARALARI 
                        Z   Y   X
                        SECTOR Z 
                        SEÇİM Y
                        KAÇINCI X
                                        110   GEREĞİNDEN FAZLA VEYA AZ VAR
                                        111 YANLIŞ DEĞER
                                        KALANLARI BURAYA YAZ :         
"""
import random
global whereWeIn
debuggerMode = 0
whereWeIn = 0
board = []   #Oyun Alanı
IcanBeThis = [0 , 1 , 2 , 3]
chrsAtTheGame = ["player" , "AtackerNormal"]  # suanlık idare
chrsAtTheGameButWhitDATA = [] # we will use later ve chrsAtTheGame e gerek kalmıcak   UNUTMA CLASSTAKİ TİP AYARINI DEĞİŞTİRMEN LAZIM BUNU KULLANCAKSAN !!!!
chrListf = ["1"]
def createBoard():
    global whereWeIn
    isVisible = 9 ;     # burda bilmiyorum diyorum görünürlüğe neden 9 lütfen satır 15 e bakınız
    for i in range(100):
        block = {
            "ID": i,
            "status": 0 ,
            "x": i % 10,
            "y": i // 10 ,
            "vs" : isVisible 
        }
        board.append(block)
    whereWeIn = 1
    return board
def setItsMe(MyBlock , tip) :   #blockunu atıyorsun ve ne olduğunu (duvar AI boşluk veya düşman)
    if tip in IcanBeThis :
        MyBlock['status'] = tip
        return 1 
def spawnArea() :   #soft lock only ONE AI can spawn
        if whereWeIn == 2  :
            for block in board :
                if block['status'] == 3 :
                    block['status'] = 0 
                elif block['status'] == 0 : 
                    what = setItsMe(block , 3)
                    break
            if what != 1 : return 0     # YAPAMAM diyor
def WhatIsThisStatus(blockID , returnWanted = None) :
    for block in board :
        if blockID == block['ID'] :
            print("bu blockun statüsü :" , block['status'])
            if block['status'] == 0 :
                print("block boş")
            elif block['status'] == 1 :
                print("block dolu (engel)")
            elif block['status']  == 2:
                print("block dolu (düşman)")
            elif block['status'] == 3 :
                print("burada AI var")
            if returnWanted == None or returnWanted == 1 : 
                return block['status']
def AttackerSpawn(wantedBlocks = 5) :
    global whereWeIn
    whereWeIn = 2    #kaçıncı basamaktayız ona bakıyor
    AttackerCounter = 0
    BlockCounter = 0     
    for block in board :
        if BlockCounter >= wantedBlocks and AttackerCounter >= 2 :  #en az 2 düşman olmalı bu zorunluluk
            break
        BlockCounter += 1
        if AttackerCounter >= 5 :
            break
        elif block['status'] == 0 :
            luckyGuy = random.randint(0 , 100)
            if (5 > luckyGuy or 90 < luckyGuy) : 
                block['status'] = 2
                AttackerCounter += 1
def CanIWalk(ROTA = None):
       if ROTA == None or ROTA == 1 :
            for block in board :
               if block['status'] == 3 : 
                   AIinIt = block
            for block in board :
                if block['x'] == AIinIt['x'] and block['y'] - 1 == AIinIt['y'] and block['status'] == 0 :
                    return 1 ;          #onay verildi true
                elif block['x'] == AIinIt['x'] and block['y'] - 1 == AIinIt['y'] and not block['status'] == 0 : 
                    return 0 ;          # onay verilmedi false 
def CanISee(vers , x = None , y = None) :     # bunu şöyle yapabiliriz BAKINIZ SATIR 1
    if vers == 1 :
        checker = True   #Kodun en hızlı olması gereken yerlerinden biri bu def yani CanISee func Çok önemli
        while checker :
            for block in board :
                if block['status'] == 3 :
                    AIinIt = block
                    i = 1
                    while 100 :   #şimdilik sadece kodun mantığı otursun diye burda
                        for block in board :    # bu kısım  sağ x e bakıyor 
                            if (not AIinIt['x']  >= 9 )and block['x'] - i == AIinIt['x'] :
                                block['vs'] = 1 
                            i += 1 
                        i = 1
                        for block in board :     # bu kısım sol x e bakıyor
                            if block['x'] + i == AIinIt['x']  and not AIinIt <= 1 :
                                block['vs'] = 1 
                        i = 1
                        for block in board :
                            if block['y'] + i == AIinIt['y'] and not AIinIt <= 1 :
                                block['vs'] = 1
                        for block in board :
                            if block['y'] - i == AIinIt['y'] and not AIinIt >= 9 :
                                block['vs'] = 1
    elif vers == 2 :
        for block in board :
            if block['x'] == x and block['y'] == y :
                hereAmI = block
        xApsis = True 
        yApsis = False 
        while xApsis :
            #TAMAMLA
def bugCheck(ONE =None , Two = None):  # ilerde sorunların nerde olduğunu nalamak için blackBox u tamamen kapatan ve her bir detayı veren defleri tek tek çalıştıran komutu veren def
    global debuggerMode
    debuggerMode = 1 
    print(createBoard())
    print()
def Worker():   # ilerde Starterdan emri aldıktan sonra dosyaları toplayıp gereken yere vericek
    pass
def Starter():  # İlerde motoru çalıştıran olucak yönetici olucak
    pass
class Fighter :
    def __init__(self , hp , vs , x,y ):
        self.hp = hp 
        self.vs = vs
        self.x = x
        self.y = y
    def move(self , dx , dy) :
        self.x += dx 
        self.y += dy
    def takeDmg(self , dmg , warType , combos) :
        if warType == "classic" :
            self.dmg = dmg
            if self.shield > 0  :
                dmg = self.shield - ( (dmg ** 2) - 10)/ 10  
            self.hp -= dmg 
        else :
            self.dmg = dmg 
            dmg = 5.1 * combos + dmg 
            self.hp -= dmg 
        return self.didIdied()    # öldüren adama skor eklemek için
    def didIdied(self) :
        if self.hp <= 0  : 
            return 1    #ölmüş.
        else :
            return 0  # ölmemiş
    def HurtAndHit() :    #yakın dövüş daha sonra
        pass 
    def hit(self) :
        return self.MyGunDmg 
    def makeABase():
        pass
    def vs(self):
        x = self.x
        y = self.y
        CanISee()
def makeMyChr(whatsType):
    if whatsType in chrsAtTheGame :
        a = 0      # bu ıd için lazım
        for chrCRATE in chrListf :
            a += 1
        charWhichIsBlessed = Fighter(whatsType)    # have nothing speacil bu sadece bizim tarafımızdan doğrudan oluşturulduğu için bleesed
        chrCREATE = {
            "ID" : a + 1 ,
            "MyChr" : charWhichIsBlessed,              # şimdi görüyorum ki büyük ihtimal oluşturma sistemi bu olucak 
            "ChrType" : whatsType
            }
def shoot(mychrID) :
    for chrCRATE in chrListf :
        if mychrID == chrCRATE['ID'] :
            myChr = chrCRATE
    Atack = Fighter(myChr).hit()
    return Atack
def doingSomething(mychrID):
    control = 0
    for chrCREATE in chrListf :
        if mychrID == chrCREATE['ID'] :
            mychr = chrCREATE
            control += 1    #bu kaç tane bu ID den olduguna bakarak sorunları engelliyor
        if control >= 2 :
            return {"err" : 110 , "where" :"doingSomething" , "info" : "duplicate" }       # Error numaraları için lütfen satır 23 e bakın
#LATEST