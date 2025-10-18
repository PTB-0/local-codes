import webbrowser
while True :
    mod = input(" ney apmak istersiniz")
    if mod == "rasgele şarkı" :
        webbrowser.open("https://music.youtube.com/watch?v=E1JdlaWyBHI&list=PLuQcklYBdp-fnYMuIQmU5xldniSUhQFUe")
    else :
        site = input("siteyi giriniz")
        webbrowser.open_new_tab(site)