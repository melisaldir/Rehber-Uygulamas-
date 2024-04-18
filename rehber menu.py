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
        ad = input("Kişinin adını giriniz:")
        no = input("Kişinin numarasını giriniz:")
        kisi={
        "Adi" : ad ,
        "Numarasi" : no
        }
        dosya = open("rehber.xx","a")
        dosya.write(str(kisi))
        dosya.close()

        menu()
    if secim == "2" :
        xx = open("rehber.xx",)
        aa = xx.read()
        print(aa)
        menu()
    if secim == "3":
        print("a")
        menu()
    if secim =="4":
       print("b")
       menu()
    if secim =="5":
        import os
        os.remove("rehber.xx")
        print("Rehber başarıyla silinmiştir!")
        menu()
menu()