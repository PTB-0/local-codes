from tkinter import *
import random
import time

pencere = Tk()
pencere.title("deneme")
pencere.geometry("5000x500+500+500")
pencere.resizable(False , False)
pencere.state("normal")
pencere.wm_attributes("-alpha" , 0.4)
control = int()
control = 0

theList = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10 , 11 , 12 , 13 , 14 , 15]
def chS():
    tet["text"] = theNumber


tet = Label(
    fg= "blue",
    
    text = "niga"
    )
tet.pack()
buton = Button(
    text= tet ,
    command= chS
    
)
buton.pack()
theNumber = random.choice(theList)

while control != 15  :
    
    pencere.mainloop(
        control == control+1
        print(control)
        
    )
    control = +1
    print("dsad")
    
#ne yazıkki çalışmıyor pencere.mainloop olayı yüzüden sorunu pencere.after(200) gibi bişi ile çözebilirim



