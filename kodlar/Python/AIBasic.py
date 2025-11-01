"""
kelimeleri otomatik hafızadaki kelimelerden hangisine benziyorsa ona çevirmesini sağlayacağım
"""
kelimeler = []
def DisHafizayaEris():
    pass

def kelimeAlici() :
    eklenenKelime = input("hafızaya eklemek istediğiniz kelimeyi yazınız")
    kelime = {
        "TrueK" : eklenenKelime
    }
    kelimeler.append(kelime)

def kelimeChecker(yazilanKelime) :
    while True :
        if yazilanKelime == "" :
            yazilanKelime = input("kelimenizi girin")
        else : 
            break
    for kelime in kelimeler :
        
        
kelimeAlici()
a = input("s")
kelimeChecker(a)