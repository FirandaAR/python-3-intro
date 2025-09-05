import csv

path_file = r"C:\Users\dell\Desktop\Tugas Tugas\tugas_csv\keuangan.csv"

total_per_kategori = {}
total_semua = 0
with open (path_file,"r") as keuangan_file:
    next (keuangan_file)
    total = 0
    isi = csv.reader (keuangan_file)
    list_read = list(isi)
    for list_keuangan in list_read:
        tanggal = list_keuangan[0]
        keterangan = list_keuangan [1]
        kategori = list_keuangan [2].strip() # hilangkan spasi
        jumlah = int(list_keuangan [3])
        print (f"| {tanggal} | {keterangan} | {kategori} | {jumlah} |")
        total += jumlah
        total_semua += jumlah  
        # Cari katerogi terbesar
        if kategori not in total_per_kategori:
          total_per_kategori[kategori] = 0
        total_per_kategori[kategori] += jumlah
    print("--------------------")
    print("Total per kategori:")
    for kategori, total in total_per_kategori.items():
        print(f"{kategori}: {total}")
 
kategori_terbesar = max(total_per_kategori, key=total_per_kategori.get)
print("--------------------")
print(f"Kategori dengan pengeluaran terbesar: {kategori_terbesar} = {total_per_kategori[kategori_terbesar]}")
print(f"Total semua pengeluaran: {total_semua}")
    


    
    


# with open (path_file,"r")


import os 
print("Daftar file di folder sekarang:", os.listdir())
