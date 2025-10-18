from collections import Counter
def kelimeSayici(cumle) :
    cumleUzunluk = len(cumle)
    print("cümleniz : \n" , cumle , "\n uzunluğu :" , cumleUzunluk , "karakter")
global kelimeler
global kelimelerRAM
kelimelerRAM = []
kelimeler = []
tur = 0

while True :
    cumle = input("cümlenizi giriniz")
    kelimeSayici(cumle)
    kelimeler = cumle.split()
    print(kelimeler)
    kelimelerRAM = kelimeler
    print(kelimeler)
    for i in range(len(cumle)) :
        lastOne = kelimeler.pop(0)
        while (tur == len(kelimelerRAM)) == False :
            if kelimelerRAM.count(lastOne) >= 1 :
                count = kelimelerRAM.count(lastOne)
                kelimelerRAM.pop(0)
                if kelimelerRAM.count(lastOne) == 0 :
                    print(lastOne , "kelimesi cÜmlede" , count   + 1 , "kere tekrar ediyor")
                    break
                else :
                    continue
            else : 
                print(lastOne , "cümlede 1 kez tekrar ediyor")
                break

    de = input("devam etmek istermisiniz :")
    cumle.count()
    if de == "evet" :
        continue
    else :
        break
