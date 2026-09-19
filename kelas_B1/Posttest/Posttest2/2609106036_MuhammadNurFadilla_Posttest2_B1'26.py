makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
nim = 36
harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5]
total_harga = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5
mata_uang_euro = total_harga / 20422
rata_rata = total_harga / len(harga_makanan)
bolean = nim != rata_rata
print(harga_makanan[-5:])
print(f"Total harga makanan: Rp.{total_harga}")
print(f"Mata uang euro:  {mata_uang_euro:.2f} EUR")
print(f"Rata-rata harga makanan: Rp. {int(rata_rata)}")   
print(bolean)

