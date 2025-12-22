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
"""
#######################
import random
board = []
def createBoard():
    for i in range(100):
        block = {
            "ID": i,
            "status": 0,
            "x": i % 10,
            "y": i // 10
        }
        board.append(block)
    return board
def spawnArea() :
    EasyB = board.copy()
    chrIsSpawnble = False
    while chrIsSpawnble == False :
        thenum = random.randint(0,99)
        chrSpawnArea = EasyB.pop(thenum)
        if chrSpawnArea == 0 : 
            chrIsSpawnble = True
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
def AttackerSpawn() :
    for i in range(5) :
        for block in board :
            if block['status'] == 0 :
                block['status'] = 2
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
def CanISee() :           # bunu şöyle yapabiliriz BAKINIZ SATIR 1
    pass
def bugCheck(ONE =None , Two = None):
    print(createBoard())


def Worker():   # ilerde Starterdan emri aldıktan sonra dosyaları toplayıp gereken yere vericek
    pass
def Starter():  # İlerde motoru çalıştıran olucak yönetici olucak
    pass