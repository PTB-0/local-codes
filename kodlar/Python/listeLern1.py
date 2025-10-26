kitaplar = []
while True :
    kac = int(input("kaç tekrar istersiniz"))
    for i in range(kac):
        kitap1 = input("bir kitap giriniz")
        kitaplar.insert(0 , kitap1)
        print(kitap1)
    print(kitaplar)
    ask = int(input("değiştirmek istediğiniz kitabın numarasını yazınız (EĞER YOKSA 0 YAZ) \n"))
    if ask == 0 :
        print("kitaplar yazılıyor")    
        for kitap in kitaplar :
            a = kitaplar.pop(i)
            print(a)
    else :
        eskiKitap  = kitaplar.pop(ask - 1)
        kitap = str(input("ne yazmak istersiniz"))
        kitaplar.insert(ask - 1 , kitap)
        print("şu \n", eskiKitap  , " bunla değiştirildi\n" , kitap)
    kontol = input("kitap oluşturucudan çıkmak istermisiniz")
    if kontol.lower in ["evet" , "olur" , "isterim" , "çıkmak isterim" , "1" ]:
        break
    
    
    
    

""""

try :
    b = input("1. kitabı yaz")
    kitaplar.append(0 , b)
except TypeError :
    print("üzgünüm bir hata yaptınız bu bir isim olamaz")
print(len(kitaplar))

"""