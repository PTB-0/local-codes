import time
import psutil
global a
print(" 1 - disk kullanımı \n 2 - Swap usage \n 3 - Cpu usage \n 4 - cores ")
a = input("Ne görmek istersiniz \n :")
if a == "disk kullanımı" or a == "1" :
    yol = input("hangi diskin kullanımı görmek istersiniz ? \n örneğin c diski için C: yazın\n").upper
    b = psutil.disk_usage(yol)
    print(b)
elif a == "2" or a == "Swap" or a == "Swap usage" :
    b = psutil.swap_memory()
    print(b)