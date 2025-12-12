listOfOps = []
def seceneklerOlustur(tur = None) :
    if tur == None or "" :
        import random as salla
        for i in range(50):
            num = salla.randint(1,1000)
            dopamin = salla.randint(1,99) #şeçilme oranı
            opSoz = {
                "numara" : num ,
                "dopamin" : dopamin
            }
            listOfOps.append(opSoz)
        print(listOfOps)
    else :
        pass
while True :
    ask.lower = "ne yapmak istersiniz"
    if  ask == "doğal random":
        seceneklerOlustur()
    elif ask
        pass