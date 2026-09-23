angka = 6
if angka < 10: # Kondisi percabangan IF
    print("Angka kurang dari 10")

'''umur = int(input("Masukkan umur: ")) # Input umur
# Misalkan, umur = 17
if umur >= 17:
    print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena

else:
    print("Kamu belum bisa membuat KTP")''' # Blok else tidak dijalankan


'''kendaraan = input("Masukkan jenis kendaraan anda: ")
if kendaraan == "mobil":    
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
print("Tarif parkir yang harus dibayar:", tarif_parkir)'''

#program harus input nilai
#jika nilai > 90 A
#jika nilai > B 80
#jika nilai > C 70
#nilai > 50 dan < 69 D

'''nilai = int(input("Masukkan nilai: "))
if nilai > 90:
    print("Nilai anda A")
elif nilai > 80:
    print("Nilai anda B")
elif nilai >= 70:
    print("Nilai anda C")
elif nilai >= 50 and nilai <= 69:
    print("Nilai anda D")
else:
    print("Nilai anda E")'''

umur = 20
status = "Dewasa" if umur >= 18  else "Belum Dewasa"
print(status)

usia = int(input("Masukkan usia Anda: "))
if usia >= 16:
    print("Silahkan Masuk")
else:
    print("Dilarang masuk")

usia = "Silahkan masuk" if usia >= 16 else "Dilarang masuk"

total_pembelian = int(input("Masukkan total pembelian: "))
if total_pembelian > 200000:
    diskon = total_pembelian * 0.3
    total_bayar = total_pembelian - diskon
    print("Total yang harus dibayar:", total_bayar)
elif total_pembelian > 100000:  
    diskon = total_pembelian * 0.1
    total_bayar = total_pembelian - diskon
    print("Total yang harus dibayar:", total_bayar)
elif total_pembelian == 100000 or total_pembelian < 100000:
    diskon = total_pembelian * 0
    total_bayar = total_pembelian - diskon
    print("Total yang harus dibayar:", total_bayar)

