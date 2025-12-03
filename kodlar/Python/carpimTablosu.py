def mod1():
    while True :
        try  : 
            istekSayi = int(input("bir sayı giriniz"))
        except ValueError :
            print("düzgüce bir sayı girmeniz lazım")
            continue
        if istekSayi <= 10 and istekSayi >= 0 :
            for i in range(11) :
                print(istekSayi * i)
                i += 1
def mod2():
    while True :
        num = int(input(""))

def mod3() :
    for i in range (101):
        j = i * i
        print( i , j) 
        ram = i
        print(i , ram , j)
        ram = i
def mod4() :
    for i in range(101):
        print(i , i + 1 ,"")
def secenek():
    ask = input("mod 1 mod 2 mod 3(write as mod1 mod2 mod3)")
    if ask == "mod1" :
        mod1()
    elif ask == "mod2" :
        mod2()
    elif ask == "mod3" :
        mod3()
    elif ask == "mod4":
        mod4()
secenek()