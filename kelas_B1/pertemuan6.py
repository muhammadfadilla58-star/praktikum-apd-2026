#set
'''kartu = {"kartu merah", "kartu merah", "kartu biru", "kartu hijau"}
for i in kartu:
    print(i)'''
    
'''angka_ganjil = {1, 3, 5, 7, 9, 11}
for i in angka_ganjil:
    print(i)'''
    
'''kelas = {"a", "b", "c"}
kelas.add("d")
print(kelas)'''

'''

aslab1 = {"fina", "shasha", "risma"}
aslab2 = {"larry", "attar", "haekal"}
gabung = aslab1.union(aslab2)
print(gabung)kelas_B1 = {"juna", "mia", "ilyas", "gabriel", "falih"}
print(kelas_B1)
kelas_B1.remove("falih")
print(kelas_B1)'''

'''angka1 = {1, 2, 3, 4, 5}
angka2 = {2, 4, 6, 8, 10}
angka1.update(angka2)
print(angka1)'''

'''praktikum = {
    "apd" : "belajar dictionary",
    "orsikom" : "belajar logism"
}
print(praktikum["apd"])'''

biodata = {
    "nama" : "ilyas",
    "nim" : "049",
    "pacar" : ["laptop", "anime"],
    "sosmed" : "@mhdilyass"
}
'''print(f"pacar no 1 adalah {biodata["pacar"][0]}")'''
'''print(biodata.get("nama", "tidak ditemukan"))
print(biodata.get("alamat", "tidak ditemukan"))'''

'''for i in biodata:
    print(i)
for i in biodata.keys():
    print(i)
for i in biodata.values():
    print(i)
for i, j in biodata.items():
    print(f"ini adalah keys {i} dan ini adalah value {j}")'''
'''biodata["matkul"] = "kalkulus"
biodata.update({"warna" : "hitam legam"})
print(biodata)'''

'''game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

key = "A", "B", "C"
value = "anak infor"
akt26 = dict.fromkeys(key, value)
print(akt26)
game_copy = game.copy()
game_copy["mobile legend"] = "hmz"
print(game)
print(game_copy)

cache= game.pop("valorant")
print(cache)

tambah = game.setdefault("resident evil", "horror")
print(game)
print("Tipe game", game.setdefault("grow a garden", "gardening"))

game["valorant"] = "horor"
game.update({"minecraft" : "gore"})
print(game)'''
'''list_game = dict(gensin="odette", ml="saber", hayday="ayam")
print(list_game)'''

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu :")
    for kategori in j:
        print(kategori)
    print("")