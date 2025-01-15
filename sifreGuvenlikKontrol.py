"""Kosullar
Uzunluk: Parola en az 8 karakter olmali.
Buyuk Harf: En az bir buyuk harf icermeli.
Kucuk Harf: En az bir kucuk harf icermeli.
Rakam: En az bir rakam icermeli.
Ozel Karakter: En az bir ozel karakter (!, @, # vb.) icermeli.
"""


import re

guvenlikPuani = 0 
parola = input("Şifrenizi Giriniz : ")

if len(parola) >= 8:
    print("1-)Parola uzunluğu yeterli")
    guvenlikPuani+=1

    
    if re.search(r'[A-Z]', parola):
        print("2-)Büyük harf içeriyor.")
        guvenlikPuani+=1
    else:
        print("2-)Parolanızın büyük harf içermesi gerekiyor !")

    if re.search(r'[a-z]', parola):

        print("3-)Küçük harf iceriyor.")
        guvenlikPuani+=1
    else:
        print("3-)Parolanızın küçük harf içermesi gerekiyor ! ")

    if re.search(r'[\d]',parola):
        print("4-)Parolanız Sayı içeriyor.")
        guvenlikPuani+=1

    else:
        print("4-)Parolanızın sayı içermesi gerekiyor !")      

    if re.search(r'[!@#$%^&*(),.?":{}|<>]' , parola):
        print("5-)Parolanız Özel semboller içeriyor .")
        guvenlikPuani+=1

    else:
        print("5-)Parolanızın özel semboller içermesi gerekiyor ! ")      

    if guvenlikPuani == 5:
        print("**************************")
        print("Parolanız OLDUKÇA güvenli.")
    elif 3 <= guvenlikPuani < 5:
        print("**************************")
        print("Parolanız güvenli.")
    else:
        print("**************************")
        print("Parolanız güvenli değil!!")

          

else:
    print("Parolanız en az 8 karakterden oluşmalı !")

    
