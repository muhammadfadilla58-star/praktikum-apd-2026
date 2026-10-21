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
print(f"Hasil dari 4! {hasil_faktorial}")'''

try:
   angka = int(input('Masukkan Angka : '))
except:
    print('input yang anda masukkan bukan Integer (angka)')