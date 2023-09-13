import random
import sys

# Daftar penyedia dan produk
penyedia_produk = {
    '0852': '0852 Kartu AS (Telkomsel)',
    '0853': '0853 Kartu AS (Telkomsel)',
    '0811': 'Kartu Halo (Telkomsel)',
    '0812': '0812 Kartu Simpati atau Halo (Telkomsel)',
    '0813': '0813 Kartu Simpati (Telkomsel)',
    '0821': '0821 Kartu Simpati (Telkomsel)',
    '0822': 'Kartu Loop (Telkomsel)',
    '0851': 'Kartu AS atau By.u (Telkomsel)',
    '0814': 'Kartu Indosat M2 Broadband (Indosat)',
    '0815': '0815 Kartu Matrix dan Mentari (Indosat)',
    '0816': '0816 Kartu Matrix dan Mentari (Indosat)',
    '0855': 'Kartu Matrix (Indosat)',
    '0856': '0856 Kartu IM3 (Indosat)',
    '0857': '0857 Kartu IM3 (Indosat)',
    '0858': 'Kartu Mentari (Indosat)',
    '0896': '0896 (Three)',
    '0895': '0895 (Three)',
    '0897': '0897 (Three)',
    '0898': '0898 (Three)',
    '0899': '0899 (Three)',
    '0817': '0817 (XL)',
    '0818': '0818 (XL)',
    '0819': '0819 (XL)',
    '0859': '0859 (XL)',
    '0877': '0877 (XL)',
    '0878': '0878 (XL)',
    '0813': '0813 (Axis)',
    '0832': '0832 (Axis)',
    '0833': '0833 (Axis)',
    '0838': '0838 (Axis)',
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
