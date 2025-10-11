import time
import psutil
global a

while True :
    print(" 1 - disk kullanımı \n 2 - Swap usage \n 3 - Cpu usage \n 4 - cores \n 5 - cpu count \n 6-  boot time \n 7 - disk partları")
    a = input("Ne görmek istersiniz \n :")
    if a == "disk kullanımı" or a == "1" :
        yol = input("hangi diskin kullanımı görmek istersiniz ? \n örneğin c diski için C: yazın\n").upper
        print(psutil.disk_usage(yol))
    elif a == "2" or a == "Swap" or a == "Swap usage" :
        print(psutil.swap_memory())
    elif a == "3" or a == "cpu" or a == "cpu usage"  :
        print(psutil.cpu_stats)
    elif a == "4" or a == "cores" :
        print(psutil.cpu_times())
    elif a == "5" or a == "cpu count" :
        print(psutil.cpu_count(False))
    elif a == "6" or a == "boot" or a == "boot time":
        print(psutil.boot_time)
    elif a == "7" :
        print(psutil.disk_partitions)

    cikis = input("çıkış yapmak istermisiniz ? \n :")
    if cikis == "isterim" or cikis == "evet" or cikis == "çıkış" :
        break
    