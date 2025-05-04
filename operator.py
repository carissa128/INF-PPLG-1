print("operator aritmatika penjumlahan")
buahpisang = 100
buahsemangka = 50 
jumlah = buahpisang + buahsemangka
print("jumlah buah pada toko ini adalah", jumlah)
print("\n")

print("operator aritmatika pengurangan")
jumlahuang = 100
jumlahpembelian = 50 
kembalian = jumlahuang - jumlahpembelian
print("kembaliannya adalah", kembalian)
print("\n")

print("operator aritmatika pembagian")
buah = 100
jumlahanak = 50 
perorang = buah / jumlahanak
print("perorang mendapatkan", perorang, "buah")
print("\n")

print("operator aritmatika perkalian")
harga = 5
jumlah = 50
total = harga * jumlah
print("total pembelanjaan anda adalah", total)
print("\n")

print("operator perbandingan (sama dengan)")
a = 5
b = 5 
print("Apakah nilai a sama dengan dari nilai b", a == b)
print("\n")

print("operator perbandingan (tidak sama dengan)")
print("Apakah nilai a tidak sama dengan dari nilai b", a != b)
print("\n")

print("operator perbandingan (lebih besar dari)")
print("Apakah nilai a lebih besar dari dari nilai b", a > b)
print("\n")

print("operator perbandingan (lebih kecil dari)")
print("Apakah nilai a lebih kecil dari dari nilai b", a < b)
print("\n")

print("operator perbandingan (lebih besar sama dengan dari)")
print("Apakah nilai 5 lebih besar sama dengan dari dari nilai 5", 5 >= 5)
print("Apakah nilai 5 lebih besar sama dengan dari dari nilai 8", 5 >= 8)
print("Apakah nilai 5 lebih besar sama dengan dari dari nilai 3", 5 >= 3)
print("\n")

print("operator perbandingan (lebih kecil sama dengan dari)")
print("Apakah nilai 5 lebih kecil sama dengan dari dari nilai 5", 5 <= 5)
print("Apakah nilai 5 lebih kecil sama dengan dari dari nilai 8", 5 <= 8)
print("Apakah nilai 5 lebih kecil sama dengan dari dari nilai 3", 5 <= 3)
print("\n")

print("Operator Penugasan")
print("Operator sama dengan")
a = 5
print("angka awal =", a)
a = 10 
print("angka baru =", a)
print("\n")

print("Operator tambah sama dengan")
angka_awal = 20 
print("angka awal=", angka_awal)
angka_awal += 5
print("angka awal setelah di tambah sama dengan 5=", angka_awal)
print("\n")

print("Operator kurang sama dengan")
angka_awal -= 5
print("angka awal setelah di kurang sama dengan 5=", angka_awal)
print("\n")

print("Operator kali sama dengan")
angka_awal *= 5
print("angka awal setelah di kali sama dengan 5=", angka_awal)
print("\n")

print("Operator bagi sama dengan")
angka_awal /= 5
print("angka awal setelah di bagi sama dengan 5=", angka_awal)
print("\n")

print("Operator sisa bagi sama dengan")
a = 20
print(a)
a %= 6
print("20 setelah di sisa bagi sama dengan 6", a)
print("\n")

print("Operator pangkat sama dengan")
a = 20
print(a)
a **= 6
print("20 setelah di pangkat sama dengan 6", a)
print("\n")

print("Operator pembagian bulat sama dengan")
a = 20
print(a)
a //= 6
print("20 setelah di pembagian bulat sama dengan 6", a)
print("\n")

print("operator logika")
a = 10
b = 7
c = 6
print("a =", a, ", b =", b, ", c = 6")
print("a > b dan a > c =", a > b or a > c)
print("b > a dan b > c =", b > a or b > c)
print("c > b dan c > a =", c > b or c > a)
print("\n")

print("Operator Bitwise")
a = 1150
b = 2790
c = a & b 
print(c)
print("\n")

a = 1150
b = 2790
c = a | b 
print(c)
print("\n")

print ("Operator Keanggotaan")
list_angka = [1, 2, 3, 4, 5]
print(list_angka)
print ("apakah ada angka 3 di list angkanya?", 3 in list_angka )  
print ("apakah ada angka 8 di list angkanya?",  8 in list_angka) 
print ("apakah tidak ada angka 3 di list angkanya?",  3 not in list_angka) 
print ("apakah tidak ada angka 8 di list angkanya?",  8 not in list_angka) 
print("\n")

x = 10
y = 10
z = 5
print("nilai X =", x, "\n","nilai Y =", y, "\n","nilai Z =", z)
print("apakah nilai X sama dengan nilai Y? ",x is y)
print("apakah nilai X sama dengan nilai Z? ",x is z)
print("apakah nilai X tidak sama dengan nilai Y? ",x is not y)
print("apakah nilai X tidak sama dengan nilai Z? ",x is not z)