while True :
    sayi1 = int(input("bir sayı giriniz"))
    sayi2 = int(input("bir sayı daha giriniz"))
    islem = input("işlem ne")
    if islem == "/" : 
        print(sayi1 / sayi2)
    elif islem == "*" :
        print(sayi1 * sayi2)
    elif islem == "+" :
        print(sayi1 + sayi2)
    elif islem == "-" :
        print(sayi1 - sayi2)
    elif islem == "%" :
        print(sayi1 % sayi2)
    elif islem == "//" :
        print(sayi1 // sayi2)
    devam = input("devam etmek istermisiniz")
    if devam == "hayır" :
        break