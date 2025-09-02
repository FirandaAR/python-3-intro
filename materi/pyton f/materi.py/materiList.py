# materi python data stucture

# list [](berurutan bisa diubah boleh duplikat)
daftarBelanja = ["teh desa", # index 0
"naspadn kawan lamo", # index 2
"pisang kembung"] # index 3

#mengakses list lewat lewat index
print ("isi tas belanja" , daftarBelanja)
print("itrm kr 1: ",daftarBelanja[0])
print ("item ke 2: ",daftarBelanja[1])

# append () menambah item baru ke list terakhir
daftarBelanja.append("olive chiken")
daftarBelanja.append("gabin")
print("Isi belanjaan sekarang",daftarBelanja)
# menambah list ke index terserah
daftarBelanja.insert(0,'kopi aku lan kowe')
print(daftarBelanja)

#remove () menghapus item dari list

daftarBelanja.remove("gabin")
print("Isi belanjaan sekarang",daftarBelanja)

print("")
print("")
# Menghapus list dengan index
daftarBelanja.pop(0)
print(daftarBelanja)
# Mengecek panjang list
print(len(daftarBelanja))
print("")
print("")
print("")
print("------- TUPLE -------")
# tuple (berurutan tidak bisa diubah bisa di duplikat)
# penulisan nya menggunakan ()
tempatTglLahir = ("Jakarta",12,"April",2010)
print("Tempat Tanggal Lahir gw  ", tempatTglLahir)

# no_index akses data tuple
print("Tempat Lahir: ",tempatTglLahir[0])
print("Tanggal lahir: ",tempatTglLahir[1])
print("Bulan: ", tempatTglLahir[2])
print("Tahun: ",tempatTglLahir[3])

print(tempatTglLahir[0:4])

# unpacking tuple ke variable baru
# mengikuti urutan item nya
tempatLahir,tglLahir,bulanLahir,tahunLahir, = tempatTglLahir
print(tempatLahir)


# Manipulasi List Lanjutan
# Megabungkan List dengan +
barangAsep = ["baju","Cd"]
barangUjang = ["Lemari,","buku"]
barangBersama = barangAsep + barangUjang
print (barangBersama)
# List multi dimensi

listMinuman = [
    ["kopi","susu"], # baris 0
    ["jus apel","jus jeruk"], # baris 1
    ["es teler","es dawet"], # baris 2
]

print(listMinuman)
# Tiap baris punya index (index di dalam index)(0,1,2)
print(listMinuman[2][0])
# menguabah isi list
listMinuman [1][0] = "Jus Mangga"
print(listMinuman) 
print("")
print("")
# Mencetak seluruh isi list menggunakan looping

for item in barangBersama:
    print(item)

print("")
print("")
print("")

print("==========Tugas==========")
print("")
print("")
print("")
listBuah = []
print("Coba Pilih 5 nama dari nama buah buah an")
buah1=input("buah pertama: ")
print("")
listBuah.append(buah1)
buah2=input("buah kedua: ")
print("")
listBuah.append(buah2)
buah3=input("buah ketiga: ")
print("")
listBuah.append(buah3)
buah4=input("buah ke empat: ")
print("")
listBuah.append(buah4)
buah5=input("buah ke lima: ")
print("")
listBuah.append(buah5)
print("")
print("")
print("")
print("Buah buah mu yang kamu pilih adalah:  ")
for buah2an in listBuah:
    print(buah2an)

