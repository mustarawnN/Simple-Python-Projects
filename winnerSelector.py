import tkinter as tk
import random

katilimciListesi = []

def yeniCerceve():

    yeni_cerceve = tk.Toplevel(cerceve)
    yeni_cerceve.title("ÇEKİLİŞ")
    yeni_cerceve.geometry("500x350")

    tk.Label(yeni_cerceve, text="Katılımcıyı girin:", fg='black', bg='yellow', font='Times 15 italic').place(x=10, y=30)
    bosluk = tk.Entry(yeni_cerceve)
    bosluk.place(x=210, y=35)

    def ekle():
        katilimci = bosluk.get()
        if katilimci:
            katilimciListesi.insert(len(katilimciListesi), katilimci)
            bosluk.delete(0, len(katilimci))
            tk.Label(yeni_cerceve, text="Eklendi: " + katilimci, fg='green', font='Times 12').place(x=10, y=80)

    def listeyiGoster():
        y = 120
        for kisi in katilimciListesi:
            tk.Label(yeni_cerceve, text=kisi, fg='black', font='Times 12').place(x=10, y=y)
            y += 20

    def kazananSec():
        if len(katilimciListesi) > 0:
            kazanan = random.choice(katilimciListesi)
            tk.Label(yeni_cerceve, text="Kazanan: " + kazanan, fg='blue', font='Times 15 bold').place(x=10, y=300)
        else:
            tk.Label(yeni_cerceve, text="Yeterli katılımcı yok!", fg='red', font='Times 15 bold').place(x=10, y=300)

    tk.Button(yeni_cerceve, text='Katılımcıyı Ekle', fg='black', bg='lightgreen', font='Times 15 italic', command=ekle).place(x=10, y=60)
    tk.Button(yeni_cerceve, text='Listeyi Göster', fg='black', bg='lightblue', font='Times 15 italic', command=listeyiGoster).place(x=180, y=60)
    tk.Button(yeni_cerceve, text='Kazananı Seç', fg='black', bg='orange', font='Times 15 italic', command=kazananSec).place(x=330, y=60)

cerceve = tk.Tk()
cerceve.title("ÇEKİLİŞ")
cerceve.geometry('500x350')

tk.Label(cerceve, text="Çekiliş Menüsüne Hoş Geldiniz...", fg='black', bg='lightblue', font='Times 15 bold').place(x=10, y=30)
tk.Button(cerceve, text='Çekiliş Başlatmak için TIKLA', fg='black', bg='green', font='Times 15 italic', command=yeniCerceve).place(x=10, y=90)

cerceve.mainloop()
