print("kondisi if")
jumlah_buah = 250
print("jumlah persediaan buah saat ini: ", jumlah_buah)
if(jumlah_buah <= 240): 
    print("jumlah buah kurang dari persediaan")
if(jumlah_buah >= 240):
    print("jumlah buah lebih dari persediaan")
print("\n")

print("kondisi if else")
if(jumlah_buah <= 240): 
        print("jumlah buah kurang dari persediaan")
else:
        print("jumlah buah lebih dari persediaan")
print("\n")

print("Kondisi Elif")
jumlah_buah = 210
print("jumlah persediaan buah saat ini: ", jumlah_buah)
if(jumlah_buah <= 150): 
      print("jumlah buah sangat kurang dari persediaan")
elif(jumlah_buah <= 200): 
      print("jumlah buah sedikit kurang dari persediaan")
elif(jumlah_buah >= 200): 
      print("jumlah buah kurang dari persediaan")
elif(jumlah_buah == 250): 
      print("jumlah buah sesuai dengan dari persediaan")
elif(jumlah_buah >= 250): 
      print("jumlah buah melebihi dari persediaan")
else:
      print("jumlah buah tidak di prediksi")
print("\n")

print("Kondisi Elif")
jenis_buah = "MH"
if(jenis_buah == "Sk"):
    print("jenis buah Semangka")
elif(jenis_buah == "AL"): 
    print("jenis buah Alpukat")
elif(jenis_buah == "MH"): 
    print("jenis buah Mangga")
else:
    print("jenis buah tidak ada")
print("\n")

print("Perulangan While")
angka = 8
count = 0
while (angka <= 9 and angka >= 20):
    print("Angkanya adalah", angka)
    count += 1
    angka += 1 
print("\n")

print("Good bye!")

print("Loop Bersarang")
for nomorbuahmangga in range(1, 3):
    for nomorbuahmarkisa in range(5, 8):   
        print("Nomor buah mangga adalah", nomorbuahmangga)
        print("Nomor buah markisa adalah", nomorbuahmarkisa)
        print()  
    print("==== Baris berikutnya ====")  
print("\n")

print("Fungsi pada Number Python")
carissa = 80
zee = 81
elvira = 79
print('Nilai Tertinggi dari ketiga siswa diatas adalah =',max(carissa, zee, elvira))
print('Nilai Tekecil dari ketiga siswa diatas adalah =',min(carissa, zee, elvira))
print("\n")

nama_panggilan = "nafis"
print("nama panggilannya: ", nama_panggilan)
nama_panggilan = nama_panggilan + " lukman"
print("nama awal dan akhirnya: ", nama_panggilan)
nama_panggilan = nama_panggilan[:5] + ' autada ' + nama_panggilan[6:]
print("nama lengkapnya adalah: ", nama_panggilan)