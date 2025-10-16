from collections import Counter
def kelimeSayici(cumle) :
    cumleUzunluk = len(cumle)
    print("cümleniz : \n" , cumle , "\n uzunluğu :" , cumleUzunluk , "karakter")
global kelimeler
global kelimelerRAM
kelimelerRAM = []
kelimeler = []
    
while True :
    cumle = input("cümlenizi giriniz")
    kelimeSayici(cumle)
    kelimeler = cumle.split()
    print(kelimeler)
    kelimelerRAM = kelimeler
    for i in range(len(cumle)) :
        lastOne = kelimeler.pop(0)
        if kelimelerRAM.count(lastOne) > 1 :
            print(lastOne , "kelimesi cÜmlede" , kelimelerRAM.count(lastOne) , "kere tekrar ediyor")
        else :
            continue
    
    de = input("devam etmek istermisiniz :")
    cumle.count()
    if de == "evet" :
        continue
    else :
        break
