import time
import os
control = input("hesap makinesi 1 site açma 2 hey 3 heyo 4 bat 5 xox 6")

if control == "1" :
    os.system (" C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\hesapMakinesi.py")
elif control == "2" :
    os.system(" C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\siteAcma.py")
elif control == "3" :
    os.system(" C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\hey.py")
elif control == "4" :
    os.system(" C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\heyo.py")
elif control == "5" :
    os.system("C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\bat.bat")
elif control == "6" :
    os.system("C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\xox.py")
else :
    if control != "0":
        os.system("C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\starter.py")
    else:
        print("sanırım yanlış girdin ")
        time.sleep(3)
        os.system(" C:\\Users\\USER\\Desktop\\local-codes\\kodlar\\Python\\starter.py")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        pass
    pass
