import random
board = []
def crateBoard() :
    for i in range(101):
        board.append(0)
    for i in range (30) :    
        blockNum = random.randint(0 , 99)
        board.pop(blockNum)
        board.insert(blockNum , 1)
    for i in board :
        theStatus = board.pop(i)
        Yapsis = 1 ;
        if i >= 10 and i < 20 :
            Yapsis = 2 
        elif i >= 20  and i < 30 :
            Yapsis = 3
        elif i >= 30 and i < 40 :
            Yapsis = 4
        elif i >= 40 and i < 50 :
            Yapsis = 5
        elif i >= 50 and i < 60 :
            Yapsis = 6 
        elif i >= 60 and i < 70 :
            Yapsis = 7
        elif i >= 70 and i < 80 :
            Yapsis = 8 
        elif i >= 80 and i < 90 :
            Yapsis = 9
        elif i >= 90 and i < 100 :
            Yapsis = 10 
        else :
            Yapsis = 1
        block = {
            "status" : theStatus ,
            "cordsX" : i / 10 ,
            "cordsY" : Yapsis ,
            "blockID" : i 
        }
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
        if blockID == block['blockID'] :
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
    
                