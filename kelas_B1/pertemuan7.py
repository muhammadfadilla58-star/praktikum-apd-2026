'''def luas_persegi(sisi):
    luas = sisi*sisi
    return luas
print(f"Luas persegi adalah : {luas_persegi(5)}")

def pengumuman():
    print("Hari ini Pengujian Proyek Akhir")
pengumuman()

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}"

try:
   angka = int(input('Masukkan Angka : '))
except:
    print('input yang anda masukkan bukan Integer (angka)')'''
daftar_minuman = {
"minuman" : [
["sprite",  8000, 8],
["fanta",  7000, 10],
["coca cola", 9000, 9],
["ultra milk", 5000, 15],
["soya",  6000, 5]
]
}

def pilihan1():
    produk = input("Tambahkan Daftar Minuman: ").strip()
    harga = input("Tambahkan Harga: ").strip()
    stok = input("Tambahkan Stok: ").strip()
    if produk == "" or harga == "" or stok == "":
        print("Isi Tidak Boleh Kosong!")
    try:
        produk = int(produk)
        harga = int(harga)
        stok = int(stok)
        daftar_minuman["minuman"].append([produk, int(harga), int(stok)])
        print("Data Berhasil Ditambahkan!")
    except:
        print("Silahkan Input Sesuai yang Diminta!")
pilihan1()
