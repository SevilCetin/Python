import random
secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldinizn Oyunu bitirmek için q tuşuna basın")
while True:
    secim = input("Taş mı kağıt mı makas mı? ")
    bil_secim = random.choice(secenek)
    if secim==taş:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş\n Sonuç: Berabere")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt\n Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: makas\n Sonuç:Kazandınız")
    if secim==kağıt:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş\n Sonuç: Kazandınız")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt\n Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: makas\n Sonuç:Kaybettiniz")
    if secim==makas:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş\n Sonuç: Kaybettiniz")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt\n Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: makas\n Sonuç:Berabere")
        if secim=='q':
            print("Çıkılıyor...")
            break