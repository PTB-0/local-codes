@echo off
title theHub_v0.0.1
cd C:\Users\USER\Desktop\kodlar
start hey.py
start heyo.py
cd Python
start hesapMakinesi.py
start siteAcma.py
cd ..
cd theHub
echo İŞTEEE BUUUUU
echo _____________________
echo end
REM 1 saniye bekleme
timeout /t 1 /nobreak > nul

REM Python dizinine git
cd /d C:\Users\USER\Desktop\kodlar\Python\

REM starter dosyasını başlat
start starter.py

REM theHub dizinine geri dön
cd /d C:\Users\USER\Desktop\kodlar\theHub

exit