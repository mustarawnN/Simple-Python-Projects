import tkinter as tk
import datetime
import random

zaman = datetime.datetime.now()

window = tk.Tk()
window.title("Kullanıcı Giriş Ekranı")
window.geometry("430x320")

kullanici_bilgileri = {}

kullaniciAdi = tk.Label(window, text="Kullanıcı Adı :", fg='black', bg='orange', font='Times 15 italic')
kullaniciAdi.place(x=10, y=30)

sifre = tk.Label(window, text="Şifre:", fg="black", bg="gray", font="Times 15 italic")
sifre.place(x=10, y=70)

kaGiris = tk.Entry()
kaGiris.place(x=150, y=35)

sifreGiris = tk.Entry(show="*")
sifreGiris.place(x=150, y=75)

sonucEtiketi = tk.Label(window, text="", fg="blue", font="Times 15 italic")
sonucEtiketi.place(x=10, y=150)

def kayitOl():
    kullanici_ad = kaGiris.get() 
    sifre = sifreGiris.get()      
    if kullanici_ad and sifre:  
        if kullanici_ad in kullanici_bilgileri:
            sonucEtiketi.config(text="Bu kullanıcı adı zaten kayıtlı!", fg="red")
        else:
            kullanici_bilgileri[kullanici_ad] = sifre 
            sifre_yildizli = "*" * len(sifre)
            mesaj = "Kayıt Başarılı!\nKullanıcı Adı: " + kullanici_ad + "\nŞifre: " + sifre_yildizli
            sonucEtiketi.config(text=mesaj, fg="blue")
    else:
        sonucEtiketi.config(text="Lütfen tüm alanları doldurun!", fg="red")

def giris():
    kullanici_add = kaGiris.get()
    sifree = sifreGiris.get()
    if kullanici_add in kullanici_bilgileri and kullanici_bilgileri[kullanici_add] == sifree:
        sonucEtiketi.config(text="Giriş başarılı!", fg="blue")

        yeniPencereAc()
        window.withdraw()  

    else:
        sonucEtiketi.config(text="Kullanıcı adı ya da şifre hatalı!", fg="red")


def ulkeleri_yukle():

    ulke_baskent = {}
    try:
       
        dosya_yolu = "C:/Users/HP/Desktop/countries.txt" 
        
        with open(dosya_yolu, 'r', encoding='utf-8') as file:
            for line in file:
                ulke, baskent = line.strip().split('|')
                ulke_baskent[ulke] = baskent
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen 'countries.txt' dosyasını doğru bir şekilde yerleştirin.")
    return ulke_baskent


def oyun(pencere):
    ulke_baskent = ulkeleri_yukle()  
    if not ulke_baskent:
        return

    def yeni_soru():
        
        ulke, baskent = random.choice(list(ulke_baskent.items()))

      
        tahmin_label.config(text=ulke + " ülkesinin başkenti nedir?")
        tahmin_entry.delete(0, tk.END)  

       
        def kontrol_et():
            tahmin = tahmin_entry.get()
            if tahmin.lower() == baskent.lower():
                sonuc_label.config(text="Doğru Cevap! 🎉", fg="green")
                
                del ulke_baskent[ulke]
               
                yeni_soru()
            else:
                sonuc_label.config(text="Yanlış! Doğru cevap: " + baskent, fg="red")

        cevapla_butonu = tk.Button(pencere, text="Cevapla", command=kontrol_et, bg="blue", fg="white")
        cevapla_butonu.pack(pady=10)

    
    tahmin_label = tk.Label(pencere, font="Times 15 italic")
    tahmin_label.pack(pady=20)

    tahmin_entry = tk.Entry(pencere)
    tahmin_entry.pack(pady=5)

    sonuc_label = tk.Label(pencere, text="", font="Times 15 italic")
    sonuc_label.pack(pady=5)

    yeni_soru()  

def yeniPencereAc():
    yeni_pencere = tk.Toplevel(window) 
    yeni_pencere.title("Başkent Bilme Oyunu")
    yeni_pencere.geometry("500x450")

    mesaj = tk.Label(yeni_pencere, text="Giriş başarılı! Yeni pencereye hoş geldiniz.", fg="black", bg="pink", font="Times 15 italic")
    mesaj.pack(pady=20)

    bildiri = tk.Label(yeni_pencere, text="Tarih: ", fg="black", bg="green", font="Times 15 italic")
    bildiri.place(x=70, y=70)

    tarih = tk.Label(yeni_pencere, text=zaman.strftime("%Y-%m-%d %H:%M:%S"), fg="black", bg="orange", font="Times 15 italic")
    tarih.place(x=160, y=70)

    oyun_butonu = tk.Button(yeni_pencere, text="Ülke ve Başkent Oyunu Oyna", command=lambda: oyun(yeni_pencere), bg="red", fg="white")
    oyun_butonu.pack(pady=45)

kayitButonu = tk.Button(window, text="Kayıt Ol", fg="black", bg="green", font="Times 15 italic", command=kayitOl)
kayitButonu.place(x=60, y=120)

girisButonu = tk.Button(window, text="Giriş", fg="black", bg="red", font="Times 15 italic", command=giris)
girisButonu.place(x=175, y=120)

window.mainloop()

