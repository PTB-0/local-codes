while   1 :
    age = int(input("yaş\n"))
    print("sen bir" , "yetişkinsin" if age >= 18 else "çocuksun")
    control = input("çıkmak istermisiniz\n")
    print(type(control))
    if control in "yes" or "evet" or "isterim" :
        quit()