import shutil
import os
import time
global existCont
yol = "C:\\Users\\Administrator\\Desktop\\Servers"
def DosyaOlustur() :
    dosyAdi =  "mc"
    kac = 0
    temp = str(kac)
    
    while True :
        temp = str(kac)
        existCont = yol + "\\" + dosyAdi + temp 
        if os.path.exists(existCont) :
            kac += 1
        else :
            os.mkdir(existCont)
            break
    temp  = str(kac)
    existCont = yol + "\\" + dosyAdi + temp 
    #os.path(existCont)
    import otomatikServerJarPurpur
    ver = otomatikServerJarPurpur.jarTaker()
    src = 'C:\\Users\\Administrator\\Downloads'
    where = yol + '\\' + dosyAdi + temp + ""
    shutil.copy(src ,ver )
DosyaOlustur()