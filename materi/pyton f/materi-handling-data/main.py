import csv

file_path =r"C:\Users\dell\Desktop\pyton f\materi-handling-data\keuangan.csv"


with open (file_path,"r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)
    print("SEMUA DATA")
    print(list_read)
    print("-"*20)
    print(f"jumlah item ke 3 : {list_read[2][3]}")
    index = 0
    for baris in list_read:
        print(f"Baris index ke-{index}")
        tanggal = baris[0]
        Keterangan = baris[1]
        Kategori = baris[2]
        jumlah = baris[3]
        print(f"{tanggal} | {Keterangan} | {Kategori} | {jumlah}")
        index+=1

# nambah file
with open (file_path,"a", newline="") as file_baru:
    tambah_data = csv.writer(file_baru)
    tambah_data.writerow(["TGL","KTRGN","KTRGI","JML"])
