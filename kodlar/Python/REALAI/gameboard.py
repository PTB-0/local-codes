import random
board = []
def createBoard():
    for i in range(100):
        block = {
            "id": i,
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
def CanIWalk(ROTA = None):
       if ROTA == None or ROTA == 1 :
           for block in board :
               if block['status'] == 3 : 
                   pass
def CanISee() :
    pass

print(createBoard())