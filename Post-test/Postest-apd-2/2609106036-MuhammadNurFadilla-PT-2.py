makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000
biaya_aplikasi = 5000
nim = 36
harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]
total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_aplikasi
mata_uang_euro = total_bayar / 20527
rata_rata = total_bayar / len(harga_makanan)
bolean = nim != rata_rata
print(harga_makanan[-6:])
print(f"Total bayar: Rp.{total_bayar}")
print(f"Mata uang euro:  {mata_uang_euro:.2f} EUR")
print(f"Rata-rata harga makanan: Rp. {rata_rata:.2f}")   
print(bolean)