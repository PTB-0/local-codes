
while True :
    cumle = input("cümlenizi giriniz")
    kelimeler = cumle.split()
    selection = 1
    kelimeler.sort
    kelimelerBenzersiz = kelimeler
    
    print("bu cümlenin içerdiği kelime sayısı :" , len(kelimeler) , "\n bu cümlenin içerdiği karakter sayısı (boşluklar dahil)" , len(cumle))
    for i in range(len(kelimeler)-1):
        try :
            last = kelimeler.pop(selection)
        except IndexError :
            break
        kelimeler.insert(selection , last)
        print(last , kelimeler.count(last))
        if kelimeler.count(last) > 1 :
            for i in range(kelimeler.count(last)):
                kelimeler.remove(last)
        else :
            kelimeler.remove(last)
    ask = input("devam etmek istermisiniz")
    if  ask == "hayır" or ask == "istemem" :
        print("çıkılıyor")
        break
    