def jarTaker() :
    import webbrowser
    print("Purpur için otomatik jar indirmeye hosgeldiniz lutfen versiyonu girin\n")
    while True :
        ver = input("Versiyon")
        linkPurpur = "https://api.purpurmc.org/v2/purpur/"
        linkPurpurC = "/latest/download"   #bu purpurun indirme apisi
        webbrowser.open(linkPurpur+ver+linkPurpurC)
        ask = input("durdurmak istermisin")
        if ask == "evet" or ask == "stop" :
            break
    return ver