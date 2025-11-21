import webbrowser
print("Purpur için otomatik jar indirmeye hosgeldiniz lutfen versiyonu girin\n")
ver = input("Versiyon")
linkPurpur = "https://api.purpurmc.org/v2/purpur/"
linkPurpurC = "/latest/download"   #bu purpurun indirme apisi
webbrowser.open(linkPurpur+ver+linkPurpurC)