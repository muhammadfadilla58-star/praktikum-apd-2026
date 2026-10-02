nama = "fadil"
nim = "036"

while True:
    Nama = str(input("Masukkan nama anda : ")).lower()
    Nim = str(input("Masukkan nim anda : "))
    if Nama == nama and Nim == nim:
        print("Login Berhasil")
        break
    elif Nama != nama and Nim == nim:
        print("Nama anda salah")
    elif Nama == nama and Nim != nim:
        print("Nim anda salah")
    else:
        print("Nama dan Nim anda salah")

ulang = "y"
kalimantan_gambut = kalimantan_mineral = 0
sumatera_gambut = sumatera_mineral = 0
total_luas_lahan_gambut_kalimantan = total_luas_lahan_mineral_kalimantan = 0
total_luas_lahan_gambut_sumatera = total_luas_lahan_mineral_sumatera = 0
while ulang == "y":
    pulau = str(input("Masukkan nama pulau : ")).lower()
    if pulau == "kalimantan":
        jenis_lahan = str(input("Masukkan jenis lahan : ")).lower()
        if jenis_lahan == "gambut":
            jumlah_titik_api = int(input("Masukkan jumlah titik api : "))
            nilai_gambut_kalimantan = jumlah_titik_api
            ulang = str(input("Apakah anda ingin mengulang? (y/t) : ")).lower()
            kalimantan_gambut += nilai_gambut_kalimantan
            total_luas_lahan_gambut_kalimantan = kalimantan_gambut * 5
        elif jenis_lahan == "mineral":
            jumlah_titik_api = int(input("Masukkan jumlah titik api : "))
            nilai_mineral_kalimantan = jumlah_titik_api 
            ulang = str(input("Apakah anda ingin mengulang? (y/t) : ")).lower()
            kalimantan_mineral += nilai_mineral_kalimantan
            total_luas_lahan_mineral_kalimantan = kalimantan_mineral * 5
        else:
            print("Jenis lahan tidak valid")
            ulang = "y"

    elif pulau == "sumatera":
        jenis_lahan = str(input("Masukkan jenis lahan : ")).lower()
        if jenis_lahan == "gambut":
            jumlah_titik_api = int(input("Masukkan jumlah titik api : "))
            nilai_gambut_sumatera = jumlah_titik_api
            ulang = str(input("Apakah anda ingin mengulang? (y/t) : ")).lower()
            sumatera_gambut += nilai_gambut_sumatera
            total_luas_lahan_gambut_sumatera = sumatera_gambut * 5
        elif jenis_lahan == "mineral":
            jumlah_titik_api = int(input("Masukkan jumlah titik api : "))
            nilai_mineral_sumatera = jumlah_titik_api 
            ulang = str(input("Apakah anda ingin mengulang? (y/t) : ")).lower()
            sumatera_mineral += nilai_mineral_sumatera
            total_luas_lahan_mineral_sumatera = sumatera_mineral * 5
        else:
            print("Jenis lahan tidak valid")
            ulang = "y"
    else:
        print("Pulau tidak valid")
        ulang = "y"

print("="*50)
print(f"Total luas lahan gambut yang terbakar di Kalimantan adalah {total_luas_lahan_gambut_kalimantan} hektar")
print(f"Total luas lahan mineral yang terbakar di Kalimantan adalah {total_luas_lahan_mineral_kalimantan} hektar")
print("="*50)
print(f"Total luas lahan gambut yang terbakar di Sumatera adalah {total_luas_lahan_gambut_sumatera} hektar")
print(f"Total luas lahan mineral yang terbakar di Sumatera adalah {total_luas_lahan_mineral_sumatera} hektar")
print("="*50)