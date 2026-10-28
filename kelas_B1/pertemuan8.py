'''#math
import math # Mengimpor semua fungsi yang ada di dalam library math
print(math.sqrt(100))
print(math.factorial(5))
#datetime
from datetime import datetime
print(datetime.now())
#calender
import calendar as kalender
print(kalender.calendar(2026))'''
#random
'''import random'''
# Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif)
'''print(random.randint(1, 5))
buah = ["pisang", "rambutan", "manggis"]
huruf = "abcd"
print(random.choice(buah)) 
print(random.choice(huruf))
kumpulan_angka = "0123456789"
pin_acak = ""
for i in range(4):
    pin_acak += random.choice(kumpulan_angka)
print(pin_acak)
kartu = ["As Wajik", "3 Hati", "7 Sekop"]
random.shuffle(kartu)
print(kartu)'''

'''from prettytable import PrettyTable
# Membuat objek tabel dan menentukan nama-nama kolom
tabel = PrettyTable()
tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]
# Menambahkan satu baris data ke dalam tabel
tabel.add_row(["2609106001", "Andi Alarice", "Informatika"])
# Menambahkan beberapa baris data sekaligus menggunakan list di dalam list
tabel.add_rows([
["2609106002", "Hammam Nopal", "Informatika"],
["2609106003", "Abimar LLM", "Sistem Informasi"]
])
# Mengatur perataan teks pada kolom tertentu ('l' = kiri, 'c' = tengah, 'r'= kanan)
tabel.align["Nama Mahasiswa"] = "l"
print(tabel)'''

import inquirer
# Menyusun daftar pertanyaan menu
pertanyaan = [
inquirer.List(
"menu",
message="Pilih menu aplikasi",
choices=["Tambah Data", "Lihat Data", "Keluar"],
),
]
# Menampilkan prompt di terminal dan menyimpan hasil pilihan
jawaban = inquirer.prompt(pertanyaan)
print(jawaban) # Output berupa Dictionary, misal: {'menu': 'TambahData'}
print(jawaban["menu"]) # Mengambil nilai berdasarkan key 'menu': Tambah Data'''
'''import inquirer
from prettytable import PrettyTable
# Deklarasi struktur dictionary untuk menampung data mahasiswa
data_mahasiswa = {
"nim": [],
"nama": [],
"kelas": []
}
def tambah_data():
    pertanyaan= [
        inquirer.Text("nim", message="Input NIM kamu"),
        inquirer.Text("nama", message="Input nama lengkapmu"),
        inquirer.List("kelas", message="Pilih kelas", choices=["A", "B", "C"]),
]
# Hasil input disimpan ke variabel jawaban dalam bentuk dictionary:
# {'nim': '...', 'nama': '...', 'kelas': '...'}
jawaban = inquirer.prompt(pertanyaan)
# Menambahkan masing-masing nilai ke dalam list pada dictionarydata_mahasiswa
data_mahasiswa["nim"].append(jawaban["nim"])
data_mahasiswa["nama"].append(jawaban["nama"])
data_mahasiswa["kelas"].append(jawaban["kelas"])
def tampil_data():
    tabel = PrettyTable()
    tabel.field_names = ["No", "NIM", "Nama", "Kelas"]
for i in range(len(data_mahasiswa["nim"])):
    tabel.add_row([
    i + 1,
    data_mahasiswa["nim"][i],
    data_mahasiswa["nama"][i],
    data_mahasiswa["kelas"][i]
    ])
print(tabel)
# Memanggil fungsi
tambah_data()'''

'''import datetime
from datetime import datetime

tgl = datetime(2026, 11, 28)
print(tgl.strftime("%d-%m-%Y")) 
a = round(19.4)
print(a)'''