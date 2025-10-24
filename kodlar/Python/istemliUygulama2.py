import os
while True :
    yol = input("uygulamanın yolunu yazınız")
    if os.path.exists(yol):
        os.system(yol)
    else :
        print("bu yol :" , yol , "geçerli diğil")
    devam = input("devam etmek istermisiniz")
    if devam == "hayır":
        break