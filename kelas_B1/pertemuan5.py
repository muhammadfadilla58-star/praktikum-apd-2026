'''formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
print(formula1)

print(formula1[3])
print(formula1[4][0])


sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
print(sirkuit)

#menambah 1 elemen
sirkuit.append("Spa-Francorchamps")
print(sirkuit)
#menambah banyak elemen
sirkuit.extend(["Spa-Francorchamps", "Interlagos"])
print(sirkuit)
#menyisipkan elemen
sirkuit.insert(2, "Interlagos")
print(sirkuit)
#mengubah element
sirkuit[1] = "Monza Italia"
print(sirkuit)
#metode slicing
sirkuit[0:2] = ["Sepang", "Mugello"]
print(sirkuit)
#menghapus list
del sirkuit[2]
print(sirkuit)
#menghapus nilai
sirkuit.remove("sepang")
print(sirkuit)

ambil_sirkuit = sirkuit.pop(2)
print(ambil_sirkuit)

driver = ["Hamilton", "Verstappen", "Leclerc", "Sainz", "Russell",
"Antoneli", "Norris"]
print(driver[0:6:2])

team1 = ["Mercedes", "Ferrari", "MacLaren"]
team2 = ["Red Bull", "Alpine", "Aston Martin"]
gabung_team = team1 + team2
print(gabung_team)

juara_WDC = ["MacLaren", "Red Bull"]
juara = juara_WDC * 3
print(juara)

line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]
for i in line_up:
    for j in i:
        print(j, end=" ")
print(line_up[1:4:1])


chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
print(chara)
print(chara[2])
print(chara[-1])
print(chara[4][0])'''

'''chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)
print(listchara)

listchara.append("Yui ")
chara = tuple(listchara)
print(chara)'''



