
while True :
    try :
        istekSayi = int(input("bir sayı giriniz"))
    except ValueError :
        print("düzgüce bir sayı girmeniz lazım")
        continue
    if istekSayi <= 10 and istekSayi >= 0 :
        for i in range(11) :
            print(istekSayi * i)
            i += 1