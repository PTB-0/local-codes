while True :
    ilk = 0
    ikinci = 1
    tekrar = int(input("kaç kere tekrar etsin")) #n yerine tekrar adlı bir değişkeni kullanmanın daha açıklşayıcı olduğunu düşünüyorum
    for i in range(tekrar) :
        print(ilk)
        print(ikinci)
        ilk = ilk + ikinci 
        ikinci = ilk + ikinci
    devam = input("devam etmek istermisiniz")
    if devam == "evet" or devam == "olur" or devam == "isterim" :
        continue
    else :
        print("çıkış yapılıyor")
        break
