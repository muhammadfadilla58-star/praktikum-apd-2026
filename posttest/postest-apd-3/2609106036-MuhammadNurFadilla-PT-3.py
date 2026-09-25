#validasi login 
nama = "fadil"
nim = 36
biaya_langganan = 1500000
username = str(input("Masukkan username anda: "))
password = int(input("Masukkan password anda: "))
if username == nama and password == nim:
    print("")
    print("Selamat Datang di Aplikasi ANGKASA!")
  
    print('''
==============================================
|              APLIKASI ANGKASA              |
==============================================
|               PAKET LANGGANAN              |
----------------------------------------------
|    NAMA PAKET     |   BIAYA ADMINISTRASI   |                          
----------------------------------------------
|   Paket Orbit     |             1%         |
|   Paket Nebula    |             3%         | 
|   Paket Galaxy    |             5%         |
|   Paket Supernova |             7%         |
==============================================
''')

    print('''
    Silahkan pilih opsi pembayaran biaya langganan aplikasi streaming musik angkasa:
    1. paket orbit
    2. paket nebula
    3. paket galaxy
    4. paket supernova
    ''')
    opsi = str(input("Opsi pembayaran : "))
    print()
    if opsi == "paket orbit":
              biaya_admin = 0.01
              total_bayar = biaya_langganan + (biaya_langganan*biaya_admin)
              print(f"1. Paket yang anda pilih   : {opsi}")
              print("2. Benefit                 : memiliki akses dasar ke lagu-lagu populer")
              print(f"3. Total yang anda bayar   : {total_bayar:.2f}")
    elif opsi == "paket nebula":
              biaya_admin = 0.03
              total_bayar = biaya_langganan + (biaya_langganan*biaya_admin)
              print(f"1. Paket yang anda pilih   : {opsi}")
              print("2. Benefit                 : akses lagu premium dan playlist kustom")
              print(f"3. Total yang anda bayar   : {total_bayar:.2f}")
    elif opsi == "paket galaxy":
              biaya_admin = 0.05
              total_bayar = biaya_langganan + (biaya_langganan*biaya_admin)
              print(f"1. Paket yang anda pilih   : {opsi}")
              print("2. Benefit                 : akses lagu premium, playlist kustom, dan mode offline")
              print(f"3. Total yang anda bayar   : {total_bayar:.2f}")
    elif opsi == "paket supernova":
              biaya_admin = 0.07
              total_bayar = biaya_langganan + (biaya_langganan*biaya_admin)
              print(f"1. Paket yang anda pilih   : {opsi}")
              print("2. Benefit                 : akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
              print(f"3. Total yang anda bayar   : {total_bayar:.2f}")
    else:
              print("Paket tidak tersedia!")

else:
  print("ERROR!")