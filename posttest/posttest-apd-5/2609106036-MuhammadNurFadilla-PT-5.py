import os
akun = []
daftar_minuman = [
["sprite",  8000, 8],
["fanta",  7000, 10],
["coca cola", 9000, 9],
["ultra milk", 5000, 15],
["soya",  6000, 5]
]
while True:
    os.system("cls")
    print("=====MANAJEMEN STOK MINUMAN=====")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    pilihan = input("Masukkan Pilihan Anda: ")
    if pilihan == "1":
        akun_valid = False
        username = str(input("Masukkan Username Anda: "))
        password = str(input("Masukkan Password Anda: "))
        for i in akun:
            if  i[0] == username and i[1] == password:
                akun_valid = True
                role = i[2] 
        if akun_valid == False:
            print("Username atau Password Anda Salah!")
            input("Tekan Enter Untuk Kembali...")
        elif role == "admin":
            print("======LOGIN BERHASIL!=====")
            print("Selamat Datang, Admin")
            input("Tekan Enter Untuk Melanjutkan...")
            while True:
                os.system("cls")
                print("\n=======DAFTAR MINUMAN=======")
                for i in daftar_minuman:
                    print(f"Nama: {i[0]}")
                    print(f"Harga: Rp {i[1]}")
                    print(f"Jumlah Stok: {i[2]}")
                    print("="*20)

                print("\n=============MENU=============")
                print("1. Tambah Daftar Minuman Baru")
                print("2. Tampilkan Daftar Minuman")
                print("3. Update Barang")
                print("4. Hapus Daftar Minuman")
                print("5. Exit")
                pilih = input("Masukkan Pilihan Anda: ")
                if pilih == "1":
                    produk = input("Tambahkan Daftar Minuman: ")
                    harga = input("Tambahkan Harga: ")
                    stok = input("Tambahkan Stok: ")
                    a = produk.isascii()
                    b = harga.isdigit()
                    c = stok.isdigit()
                    if produk == "" and harga == "" and stok == "":
                        print("Isi Tidak Boleh Kosong!")
                    elif a == True and b == True and c == True:
                        daftar_minuman.append([produk, harga, stok])
                        print("Data Berhasil Ditambahkan!")
                    else:
                        print("Silahkan Input Sesuai yang Diminta!")
                    input("Tekan Enter Untuk Kembali...")
                elif pilih == "2":
                    print("\n=======DAFTAR MINUMAN=======")
                    for i in daftar_minuman:
                        print(f"Nama: {i[0]}")
                        print(f"Harga: {i[1]}")
                        print(f"Jumlah Stok: {i[2]}")
                        print("="*20)
                    input("Tekan Enter Untuk Kembali...")
                elif pilih == "3":
                    print("Apa yang Igin Anda Update?")
                    print("1. Harga Barang")
                    print("2. Stok Barang")
                    pilihan = input("Masukkan Pilihan Anda: ")
                    if pilihan == "1":
                        indeks = input("Masukkan Indeks Minuman yang Ingin di Ganti: ")
                        if indeks.isdigit():
                            indeks = int(indeks)
                            if indeks < len(daftar_minuman):
                                harga_baru = input("Masukkan Harga Baru: ")
                                if harga_baru.isdigit():
                                    daftar_minuman[int(indeks)][1] = int(harga_baru)
                                    input("Tekan Enter Untuk Kembali...")
                                else:
                                    print("Hanya Menerima Input Angka!")
                                    input("Tekan Enter Untuk Kembali...")        
                            else:
                                print("Jangkauan Tidak Tersedia!")
                                input("Tekan Enter Untuk Kembali...")
                        else:
                            print("Hanya Menerima Input Angka!")
                            input("Tekan Enter Untuk Kembali...")
                    elif pilihan == "2":
                        indeks = input("Masukkan Indeks yang Ingin di Ganti: ")
                        if indeks.isdigit():
                            indeks = int(indeks)
                            if indeks < len(daftar_minuman):
                                stok_baru = input("Masukkan Stok Baru: ")
                                if stok_baru.isdigit():
                                    daftar_minuman[int(indeks)][2] = int(stok_baru)
                                    input("Tekan Enter Untuk Kembali...")
                                else:
                                    print("Hanya Menerima Input Angka!")
                                    input("Tekan Enter Untuk Kembali...")    
                            else:
                                print("Jangkauan Tidak Tersedia!")
                                input("Tekan Enter Untuk Kembali...")   
                        else:
                            print("Hanya Menerima Input Angka!")
                            input("Tekan Enter Untuk Kembali...")    
                    else:
                        print("pilihan Tidak Valid!")
                        input("Tekan Enter Untuk Kembali...")
                elif pilih == "4":
                    hapus = input("Data Mana yang Ingin Anda Hapus: ")
                    if hapus.isdigit():
                        hapus = int(hapus)
                        if hapus < len(daftar_minuman):
                            del daftar_minuman[int(hapus)]
                            print("Data Berhasil Dihapus!")
                            input("Tekan Enter Untuk Kembali...")
                        else:
                            print("Jangkauan Tidak Tersedia!")
                            input("Tekan Enter Untuk Kembali...")                              
                    else:
                        print("Hanya Menerima Input Angka!")
                        input("Tekan Enter Untuk Kembali...")
                elif pilih == "5":
                    print("Terima kasih!")
                    input("Tekan Enter Untuk Kembali...")
                    break
                else:
                    print("Pilihan Tidak Valid!")
                    input("Tekan Enter Untuk Kembali...")
        elif role == "pengguna":
            while True:
                os.system("cls")
                print("\n=============MENU=============")
                print("1. Tampilkan Daftar Minuman")
                print("2. Exit")
                pilih = input("Masukkan Pilihan Anda: ")
                if pilih == "1":
                    print("\n=======DAFTAR MINUMAN=======")
                    for i in daftar_minuman:
                        print(f"Nama: {i[0]}")
                        print(f"Harga: {i[1]}")
                        print(f"Jumlah Stok: {i[2]}")
                        print("="*20)
                    input("Tekan Enter Untuk Kembali...")
                elif pilih == "2":
                    print("Terima kasih!")
                    break
                else:
                    print("Pilihan Tidak Valid!")
                    input("Tekan Enter Untuk Kembali...")
        else:
            print("Role Tidak Tersedia!")
            input("Tekan Enter Untuk Kembali...")
    elif pilihan == "2":
        x = True
        username = str(input("Masukkan Username Anda: "))
        password = str(input("MasukkanPassword Anda: "))
        role = str(input("Masukkan Role Anda: ")).lower()
        for i in akun:
            if i[0] == username or i[1] == password:
                print("Username atau Password Tersebut Telah Digunakan!")
                x = False
                input("Tekan Enter Untuk Kembali...")
                break
        if username == "" or password == "":
            print("Username atau Password Tidak Boleh Kosong!")
            input("Tekan Enter Untuk Kembali...")
        elif x == True:
            akun.append([username, password, role])
            print("Registrasi Berhasil!")
            input("Tekan Enter Untuk Kembali...")
    elif pilihan == "3":
        print("Terima Kasih Telah Menggunakan Aplikasi Manajemen Stok Minuman!")
        break
    else:
        print("Pilihan Tidak Tersedia!")
        input("Tekan Enter untuk Kembali...")