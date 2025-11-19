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
        if tekrarlar.count(a) >= 1 :
            rep = {
                "sayı" : a ,
                "tekrar" : tekrarlar.count(a),
                "skor" : score
                }
            tekrarlar.append(rep)
        else :
            tekrarlar.append(a)
    print(tekrarlar)
def kacTekrar() :
    for rep in tekrarlar:
        print(rep)
    print(score)
def calis():
    while True :
        if score == 0 :
            ask = int(input("Kaç kere sayı oluşturulsun (0 uygulamadan çıkartır)"))
        else :
            ask = int(input("-1 girerseniz kaç tane tekrar olduğunu görürsünüz 0 girerseniz uygulamadan çıkarsınız bir sayı girersen ve o sayı \n bu sayılardan farklı olursa o kadar sayı eklenir"))
            
        if ask == -1 :
            kacTekrar()
        elif ask == 0 :
            quit()
        else :
            Rasgele(ask)
        
calis()