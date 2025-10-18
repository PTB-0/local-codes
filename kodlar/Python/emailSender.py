import smtplib
import email
import ssl
Esifre =  ""
Nsifre = ""
while True :
    mesaj = input("mesajınız nedir")
    mailAdress = input("e mail adreslerinden birini seçiniz")
    if  mailAdress != "balh" or mailAdress != "bleh" :
        print("üzgünüm ama bu e maie izin verilmiyor")
    