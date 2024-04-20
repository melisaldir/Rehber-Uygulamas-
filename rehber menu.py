import ast
def kisiekle():
    ad = input("Kişinin adını giriniz:")
    no = input("Kişinin numarasını giriniz:")
    kisi={
    "Adi" : ad ,
    "Numarasi" : no
    }
    dosya = open("rehber.xx","a")
    dosya.write(str(kisi))
    dosya.close()

def listele():
    xx = open("rehber.xx",)
    aa = xx.read()
    print(aa)

import ast
def ara():
    with open("rehber.xx","r") as dosya:
        okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim:")
    for a in cevirilen:
        if a["Adi"] == aranan:
            print(a)

import ast
def duzelt():
    with open("rehber.xx","r") as dosya:
        okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Düzeltilecek isim:")
    dosya.close()
    with open("rehber.xx","r") as dosya:
        for a in cevirilen:
            if a["Adi"] == aranan:
                print(a)
            yeniAd = input("Yeni ad:")
            yeniNo = input("Yeni numara:")
            a["Adi"]=yeniAd
            a["Numarasi"]=yeniNo
        dosya.write(f"{str(a)},")

import ast
def sil():
    with open("rehber.xx","r") as dosya:
        okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim:")
    dosya.close()
    with open("rehber.xx","w") as dosya:
        for a in cevirilen:
            if a["Adi"] != aranan:
                dosya.write(f"{str(a)},")


def menu():
    print("╔═══════════════════╗")
    print("║ REHBER UYGULAMASI ║")
    print("║1-Kişi Ekle        ║")
    print("║2-Listele          ║")
    print("║3-Ara              ║")
    print("║4-Düzelt           ║")
    print("║5-Sil              ║")
    print("║  Seçiminiz nedir? ║")
    print("╚═══════════════════╝")
    secim= input("Buraya yazınız:")
    if secim == "1" :
        kisiekle()
        menu()
    if secim == "2" :
        listele()
        menu()
    if secim == "3":
        ara()
        menu()
    if secim =="4":
       duzelt()
       menu()
    if secim =="5":
        sil()
        menu()
menu()