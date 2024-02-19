class Kutuphane:
    def __init__(self):
        self.dosya = open("kitaplar.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitap_satirlari = self.dosya.read().splitlines()

        if not kitap_satirlari:
            print("Kütüphanede kitap bulunmamaktadır.")
        else:
            for satir in kitap_satirlari:
                kitap_bilgisi = satir.split(',')
                kitap_adi, yazar, yayin_tarihi, sayfa_sayisi = kitap_bilgisi
                print(f"Kitap: {kitap_adi}, Yazar: {yazar}, Yayın Tarihi: {yayin_tarihi}, Sayfa Sayısı: {sayfa_sayisi}")

    def kitap_ekle(self):
        kitap_adi = input("Kitap adını girin: ")
        yazar = input("Yazarı girin: ")
        yayin_tarihi = input("Yayın tarihini girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")

        kitap_satiri = f"{kitap_adi},{yazar},{yayin_tarihi},{sayfa_sayisi}\n"
        self.dosya.write(kitap_satiri)
        print("Kitap başarıyla eklendi.")

    def kitap_sil(self):
        silinecek_kitap_adi = input("Silinecek kitabın adını girin: ")

        self.dosya.seek(0)
        kitap_satirlari = self.dosya.readlines()

        with open("kitaplar.txt", "w") as yeni_dosya:
            for satir in kitap_satirlari:
                if silinecek_kitap_adi not in satir:
                    yeni_dosya.write(satir)

        self.dosya.close()
        self.dosya = open("kitaplar.txt", "a+")
        print(f"Kitap '{silinecek_kitap_adi}' başarıyla silindi.")

    def kapat(self):
        print("Kütüphane yönetim sisteminden çıkılıyor. Hoşça kalın!")
        exit(0)

def ana_program():
    kutuphane = Kutuphane()

    while True:
        print("\nKütüphane Yönetim Sistemi\n"
              "1. Kitapları Listele\n"
              "2. Kitap Ekle\n"
              "3. Kitap Sil\n"
              "Q. Çıkış")

        secim = input("Seçiminizi girin: ")

        if secim == '1':
            kutuphane.kitaplari_listele()
        elif secim == '2':
            kutuphane.kitap_ekle()
        elif secim == '3':
            kutuphane.kitap_sil()
        elif secim.upper() == 'Q':
            kutuphane.kapat()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_program()