import shutil
import os
yol = "C:\Users\Administrator\Desktop\Servers"
def DosyaOlustur() :
    dosyAdi =  "mc"
    kac = "0"
    while True :
        if os.path.exists(yol + "\\" + dosyAdi + kac ) :
            kac += 1 
        else :
            os.mkdir(yol + "\\" + dosyAdi + kac)
            break
    os.path(yol + "\\" + dosyAdi + kac)
    import otomatikServerJarPurpur
    otomatikServerJarPurpur.jarTaker()
    src = 'C:\Users\Administrator\Downloads'
    where = yol + '\\' + dosyAdi + kac + ""
    shutil.copy(src , )
    