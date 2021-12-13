from tkinter import *
from module1 import *

dictionary=main("info.txt")

window=Tk()
window.title("Тайна Вашего имени скрыта здесь!")
window.geometry("1500x900")
window.iconbitmap("numerology.ico")

lbl=Label(window, text="Введите ваше имя:", fg="#810600", font=("Arial", 18, "bold"))
lbl.pack()
#name=StringVar()
ent=Entry(window, fg="#041C52", width=20, font="Arial, 15")#,textvariable=name)
ent.bind("<Return>")
ent.pack()
lbl1=Label(window, text="Ваш результат:", fg="#810600", font=("Arial", 13, "bold"))

btn=Button(window, text="Узнать!", font=("Arial", 15, "bold"), fg="#810600", bg="#B7B6B6", command=lambda:first_step(ent.get().lower(),lbl1))
#btn.bind("<Button-1>", first_step)
btn.pack()
lbl1.pack() 




window.mainloop()
