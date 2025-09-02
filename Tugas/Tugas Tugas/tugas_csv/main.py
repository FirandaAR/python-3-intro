import csv

path_file = r"C:\Users\dell\Desktop\Tugas Tugas\tugas_csv\keuangan.csv"
total = 0
with open (path_file,"r") as keuangan_file:
    next (keuangan_file)
    isi = csv.reader (keuangan_file)
    list_read = list(isi)
    for list_keuangan in list_read:
        tanggal = list_keuangan[0]
        keterangan = list_keuangan [1]
        kategori = list_keuangan [2]
        jumlah = int(list_keuangan [3])
        print (f"| {tanggal} | {keterangan} | {kategori} | {jumlah} |")
        total += jumlah
print("")
# Hitung 
kategori_total = {}
for baris in list_read:
    kategorinya = baris[2]
    jumlahnya = int(baris[3])
    if kategori not in kategori_total:
        kategori_total[kategorinya] = 0
    kategori_total[kategorinya] += jumlahnya 

pr   

print(f"Total pengeluaran: {total}")

# Cari katerogi terbesar



# with open (path_file,"r")


import os 
print("Daftar file di folder sekarang:", os.listdir())
