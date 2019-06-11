
global ad
ad= "list.txt"

print("Kütüphane Kataloğuna Hoşgeldiniz!")

def listele() :
    with open(ad ,"r") as dosya:
        veriler = dosya.readlines()
        i =1
        for veri in veriler:
            print(i,".",veri)
            i+= 1
def ekle():

        with open (ad,"a") as dosya:
         dosya.write(input("Yazarın ismini giriniz")+":")
         dosya.write(input("Eserin ismini giriniz")+",")
         dosya.write(input("Eserin tarihini giriniz"))

def arama():

    with open(ad,"r") as dosya:

        aranan = input("Aramak istediğiniz kelimeyi giriniz: ")

        aranan_varmi =dosya.read().find(aranan)

    if aranan_varmi != -1:
        print(aranan)

    else:

        print("Aradığınız kelime bulunmamaktadır.")
        print("Lütfen tekrar deneyiniz.!")



while 1:
    print("Eserleri listelemek için: [1]")
    print("Yeni eser girişi için: [2]")
    print("Eserin adını, yazarın adını ve ya eserin tarihe göre arama yapmak için: [3]")

    secenek =int(input("Lütfen yapmak istediğiniz işlemi seçiniz:"))

    if secenek ==1 :
        listele()
    if secenek ==2 :
        ekle()
    if secenek ==3 :
       arama()
