kitaplar = []
kac = int(input("kaç tekrar istersiniz"))
for i in range(kac):
    kitap1 = input("bir kitap giriniz")
    kitaplar.insert(0 , kitap1)
    print(kitap1)
    kontrol = input("son yazdığınız kitap doğrumu").strip().lower()
    while (kontrol in ("değil" , "hayır" , "yanlış" , "doğru değil") ) == True :
        kitaplar[0] =  input("Yazmak istediğniz kitabı giriniz")
        kontrol = input("bu doğrumuydu").lower()
try :
    b = input("1. kitabı yaz")
    kitaplar.append(0 , b)
except TypeError :
    print("üzgünüm bir hata yaptınız bu bir isim olamaz")
print(len(kitaplar))
for i in range(kac):
    a = kitaplar.pop(i)
    print(a)