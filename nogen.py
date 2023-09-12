import random
import sys

# Daftar penyedia dan produk
penyedia_produk = {
    '0811': 'KartuHALO (Telkomsel)',
    '0812': 'SimPATI, KartuHALO (Telkomsel)',
    '0813': 'SimPATI, KartuHALO (Telkomsel)',
    '0814': 'Indosat 3,5G Broadband (IndosatM2)',
    '0815': 'Mentari, Matrix (Indosat)',
    '0816': 'Mentari, Matrix (Indosat)',
    '0817': 'XL Prabayar/Pascabayar (Axiata)',
    '0818': 'XL Prabayar/Pascabayar (Axiata)',
    '0819': 'XL Prabayar/Pascabayar (Axiata)',
    '0821': 'SimPATI (Telkomsel)',
    '0828': 'Ceria (Sampoerna Telekom)',
    '0831': 'Axis (Natrindo Telepon Seluler)',
    '0838': 'Axis (Natrindo Telepon Seluler)',
    '0852': 'Kartu As (Telkomsel)',
    '0853': 'Kartu As Fress (Telkomsel)',
    '0855': 'Matrix Auto (Indosat)',
    '0856': 'IM3 (Indosat)',
    '0857': 'IM3 (Indosat)',
    '0858': 'Mentari (Indosat)',
    '0859': 'XL Prabayar/Pascabayar (Axiata)',
    '08681': 'ByRU (PSN - Pasifik Satelit Nusantara)',
    '0877': 'XL Prabayar (Axiata)',
    '0878': 'XL Prabayar (Axiata)',
    '0879': 'XL Prabayar (Axiata)',
    '0881': 'Smart (Smart Telecom)',
    '0882': 'Smart (Smart Telecom)',
    '0888': 'Fren, Mobi (Mobile-8)',
    '0889': 'Mobi (Mobile-8)',
    '0896': '3 (Three)',
    '0897': '3 (Three)',
    '0898': '3 (Three)',
    '0899': '3 (Three)'
}

def tampilkan_produk(penyedia_terpilih):
    # Menampilkan produk-produk yang tersedia untuk penyedia yang dipilih
    produk_produk = [produk.split('(')[0].strip() for nomor_awal, produk in penyedia_produk.items() if penyedia_terpilih in produk]
    if produk_produk:
        print(f"\nProduk yang Tersedia untuk {penyedia_terpilih} adalah:")
        for i, produk in enumerate(produk_produk, start=1):
            print(f"{i}. {produk}")
        return produk_produk
    else:
        print(f"Tidak ada produk yang tersedia untuk {penyedia_terpilih}.")
        return None

# Menampilkan menu pilihan penyedia
while True:
    print("\nPilih Penyedia (Operator):")
    daftar_penyedia = {}
    for nomor_awal, produk in penyedia_produk.items():
        penyedia = produk.split('(')[-1].strip(')')
        if penyedia not in daftar_penyedia:
            daftar_penyedia[penyedia] = nomor_awal
            print(f"{len(daftar_penyedia)}. {penyedia}")

    # Menambahkan pilihan Exit
    print("0. Exit")

    # Meminta input dari pengguna
    pilihan_penyedia = int(input("Masukkan nomor penyedia yang Anda pilih (misal: 1): "))

    if pilihan_penyedia == 0:
        print("Terima kasih telah menggunakan program. Sampai jumpa!")
        sys.exit()  # Keluar dari program

    # Mengambil nomor penyedia yang dipilih
    penyedia_terpilih = None
    if pilihan_penyedia > 0 and pilihan_penyedia <= len(daftar_penyedia):
        penyedia_terpilih = list(daftar_penyedia.keys())[pilihan_penyedia - 1]

    if penyedia_terpilih:
        produk_produk = tampilkan_produk(penyedia_terpilih)
        if produk_produk:
            # Meminta input dari pengguna untuk memilih produk
            pilihan_produk = int(input(f"Masukkan nomor produk yang Anda pilih (1-{len(produk_produk)}): "))
            if pilihan_produk > 0 and pilihan_produk <= len(produk_produk):
                produk_terpilih = produk_produk[pilihan_produk - 1]
                print(f"Anda memilih produk: {produk_terpilih}")

                # Memilih nomor acak berdasarkan penyedia dan produk yang dipilih
                nomor_terpilih = [nomor for nomor, produk in penyedia_produk.items() if penyedia_terpilih in produk and produk_terpilih in produk]
                if nomor_terpilih:
                    nomor_acak = random.choice(nomor_terpilih)

                    # Menambahkan nomor acak setelah nomor awal hingga mencapai 10 sampai 12 digit
                    while len(nomor_acak) < 12:
                        nomor_acak += str(random.randint(0, 9))

                    print(f"Nomor Telepon Acak ({penyedia_terpilih} - {produk_terpilih}): {nomor_acak}")
                else:
                    print(f"Tidak ada nomor yang cocok dengan penyedia dan produk yang dipilih.")
            else:
                print("Nomor produk yang Anda pilih tidak valid.")
        else:
            print("Kembali ke Menu Penyedia/Operator.")
    else:
        print("Nomor penyedia yang Anda pilih tidak valid.")
        
#pyinstaller --onefile nogen.py
