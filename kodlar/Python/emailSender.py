import smtplib
import email
import ssl
Esifre =  ""
Nsifre = ""
while True :
    mesaj = input("mesajınız nedir")
    mailAdress = input("e mail adreslerinden birini seçiniz")
    if  mailAdress != "ege.yildiz123456789" or mailAdress != "noloopreal@gmail.com" :
        print("üzgünüm ama bu e maie izin verilmiyor")
    