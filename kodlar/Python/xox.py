import time
a = 0
kazanc = 0

def cikis() :
    global a , kazanc
    wannaCon = input("devammı (E)vet/(H)ayır")
    if wannaCon == "H" :
        print("çıkılıyor")
        a = 1
        pass
    elif wannaCon == "E" :
        a = 0
        kazanc = 0
    else :
        print("sanırım yanlış yazıldı sistem kapatılıyor")
        pass

while  a == 0 :
    

    print("xox oyununa hoş geldiniz ne yapmak istersiniz\n")
    modstr = input("1 kurrallar 2 oyna")
    try :
        mod = int(modstr)
    except ValueError :
        if modstr == "HEY1234" :
            print("yes")
            print("\nwrite \n 123,Ab \n for 100 percent sucsesfful ending the code\n")
            killer = input("s")
            killerN = int(killer)
        else :
            
            print("sayı girmeniz lazım 1 veya 2 ")
        continue
        
    if mod == 1 :
        print("harita şu şekildedir:\n")
        print("  |   |   \n")
        print("__________ \n")
        print("  |   |   \n")
        print(" ________ \n")
        print("  |    |   \n")
        print("ilk X başlar ve yukardaki 9 şecenekten birine koyar\n")
        print("Sonra O oyuncusu ikinci işlemi yapıp O harfini kalan 8 şeçenekten birine koyar\n")
        print("oyunun sonu tüm kareler dolarsa veya bir oyuncu kendi harfinden 3 tanesini çapraz yanyana üstüste yaparsa kazanmış olur\n")
        pass
    elif mod == 2 :
        kazanc = 0
        ##kodlar buraya
        ##kodlar buraya
        if kazanc == 0 :
            a = 1
            print("Beraberlik !!!!\n")         #beraberlik olunca 
            cikis()
            pass
        elif kazanc ==  1 :
            a = 1
            print("Kazandın tebrikler \n")
            cikis()
            pass
        elif kazanc == -1 :
            a = 1
            print("!!!!!KAYBETTİN EZİK !!!!")
            time.sleep(5)
            print("pardon dans ediyoduöda evet nerde kalmıştık")
            cikis()
            pass
        else :
            a = 1
            print("kodda bir hata olmuyş ve puanlama sisteminde bir sroun var bu yüzden kazandınmı kaybettinmi bilmiyoruz\n")
            cikis()
            pass
        pass
    pass

time.sleep(2)
