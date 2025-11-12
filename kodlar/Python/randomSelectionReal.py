list = []
tekrarlar=[]
global score
score = 0
rep = {}
import random as salla
def Rasgele(tekrar = None) :
    score = 0
    while True:
        if tekrar == None :
            tekrar = int(input("kaç tekrar olsun önerilen: 5"))
        else :
            break
    for i in range(tekrar) :
        a = salla.randint(1,100)
        if list.count(a) > 1 :
            rep = {
                "sayı" : a ,
                "tekrar" : list.count(a),
                "skor" : score
                }
            tekrarlar.append(rep)
        else :
            list.append(a)
    print(list)
def kacTekrar() :
    for rep in tekrarlar:
        print(rep)
    print(score)
def calis():
    while True :
        if score == 0:
            ask = int(input("kaç tekrar olsun (çıkmak için 0 yazınız)"))
        else :
            ask = int(input("tekrar sayısı girmek için o sayıyı girin eğer çıkmak istiyorsanız 0 girin eğer tekrarı görmek istiyorsan -1 gir"))
            if ask == -1 :
                kacTekrar()
        if ask != 0 :
            Rasgele(ask)
        else :
            break
calis()