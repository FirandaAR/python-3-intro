import csv
print("MATERI 11 File handling part 2")
print("--------------Update csv--------------")
# Baca semua file -> Extrak data -> Buat data baru
# Tulis ulang semua baris nya dengan kode 'w'

file_path_csv= r"\Users\dell\Desktop\pyton f\materi-handling-data\gamefav.csv"
# siap kan data kosong
# untuk menampung data dari csv list
data_game=[]
with open(file_path_csv,"r") as file_path:
    # csv reader()----> membaca isi file csv
    isi_tabel_game=csv.reader(file_path)
    # esktrak semua data dengan for loop
    for tabel_game in isi_tabel_game:
        print(tabel_game)
        # tambahkan item ke list game
        data_game.append(tabel_game)

# 2. mengubah atau membuat data baru
for item in data_game:
    print(f"Proses item no ==>{item[0]}")
    print(item)
# Jika kolom nama (index 1 adalah "nama")
    if item[1]=='Firanda':
    # Ganti kolom game (index 2) dengan nilai baru
        game_baru=("FF")
        item[2]=game_baru
        print(f"Data ditemukan,ganti game: {game_baru}")

# hapus data di list index 2
del data_game[2]
print(f"data jajan terkini: {data_game}")

print("===============")
# tulis ulang data dengan mode 'w' -> write
with open(file_path_csv,"w") as file_path:
    writer=csv.writer(file_path)
    #writerows() --> tulis banyak sekali
    writer.writerows(data_game)


