import datetime

zaman = datetime.datetime.now()


durum = "evet"
durum2 = "hayir"
bakiye = 5000

def giris():
   
    global bakiye
    print("Bankamatiğe hoş geldiniz")
    
    
    secim = int(input("İşlem seçiniz \n 1-) Bakiye Öğrenme \n 2-) Para Yatırma \n 3-) Para Çekme \n 4-) Çıkış: "))

    if secim == 1:
        print("Güncel bakiyeniz:", bakiye)

    elif secim == 2:
        yatirilcakpara = int(input("Ne kadar para yatırılacak: "))
        print("Girilen para sayılıyor ...")
      
        if(yatirilcakpara>50000):
         print("Yatırılacak para limitini aştınız , tekrar deneyin.")
        if yatirilcakpara > 0 and yatirilcakpara<=50000:  
            print("Para:", yatirilcakpara)
            onay = input("Onaylıyorsanız 'evet', onaylamıyorsanız 'hayir' yazın: ").lower()

            if onay == durum:
                bakiye += yatirilcakpara
                print("Para yatırma işleminiz başarıyla gerçekleşti.\nGüncel Bakiyeniz =>", bakiye)
                print("İşlem Zamanı:", zaman)  
                print("****************************")
            else:
                print("Para yatırma işleminiz iptal edildi.")
                print("****************************")
        else:
            print("Lütfen pozitif bir sayı giriniz.")
            print("****************************")

    elif secim == 3:
        cekim = int(input("Ne kadar para çekeceksiniz: "))

        if cekim <= bakiye:
            bakiye -= cekim
            print("Paranız başarıyla çekildi.\nGüncel bakiyeniz =>", bakiye)
            print("İşlem Zamanı:", zaman)  
            print("****************************")
        else:
            print("Yetersiz bakiye.")
            print("****************************")

    elif secim == 4:
        print("Sistemden çıkışınız yapılıyor ...")
        exit()

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        print("********************************")

while True:
   giris()
