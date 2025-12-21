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
        block = {
            "status" : theStatus ,
            "cords" : i 
        }
def spawnArea() :
    EasyB = board.copy()
    chrIsSpawnble = False
    while chrIsSpawnble == False :
        thenum = random.randint(0,99)
        chrSpawnArea = EasyB.pop(thenum)
        if chrSpawnArea == 0 : 
            chrIsSpawnble = True
def AttackerSpawn() :