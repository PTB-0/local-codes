global ilk
global ikinci
global i
global n
i = 0
n = 0
def nBasamak() :
    ilk = 0
    ikinci = 1
    for i in range(n) :
        ilk = ilk + ikinci
        ikinci = ilk + ikinci
    print(ilk)
while True :
    ilk = 0
    ikinci = 1
    mod = input("mod nasıl olsun ? yani ninci tekrardaki sayıyımı söylesin(1) yoksa n e gelesiye kadarmı (2)")
    if mod == "2" or mod == "(2)" :
        tekrar = int(input("kaç kere tekrar etsin")) #n yerine tekrar adlı bir değişkeni kullanmanın daha açıklşayıcı ve daha düzgün olduğunu düşünüyorum
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
    elif mod == "1" or mod == "(1)" :
        while True :
            n = int(input("kaçıncı sayıyı görmek istersiniz"))
            if n > 100 :
                print("Dikkat edin! Bu sayı çok uzun olacağı için bilgisiyar yavaşlaya bilir hatta çökebilir önerim başka bir sayı seçmek")
                kabul = input("sayıyı değiştirecekmisiniz edicekmisiniz? : \n")
                if kabul == "evet" :
                    print("tekrarlanıyor ...")
                else :
                    nBasamak()
            elif n < 0 :
                print("sayı negatif olamaz")
            else :
                nBasamak()
            