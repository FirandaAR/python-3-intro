import csv
print("MATERI 10 FILE HANDLING")
print("--------------------------------")

# Buka pesan 
file_pesan=open(r"C:\Users\dell\Desktop\pyton f\materi-handling-data\pesan.txt","r")
# Buka Isi Pesan
isi_pesan=file_pesan.read()
# Output isi pesan di terminal
print(f"ISI PESAN---->{isi_pesan}")
# tutup file
file_pesan.close()

("=========================")

print("")
print("Open CSV FILE")
print("=============================")
# r raw string olah data string asli
# mode 'r' = read only 
("============READ CSV FILE=============")
file_game=open(r"C:\Users\dell\Desktop\pyton f\materi-handling-data\gamefav.csv")
isi_tabel=file_game.read()
# Output isi pesan di terminal
print(f"ISI TABEL---->{isi_tabel}")
# tutup file
file_game.close()

file_path = r"C:\Users\dell\Desktop\pyton f\materi-handling-data\gamefav.csv"

print("")
print("==========APPEND CSV FILE+===========")
game_baru=[4,'Luqman',"FIFA"]
# with.........as= buka tutup otomatis file
# open()= membuka file dari file path
# mode 'a' = append (tambah file)
# newline tambah baris baru dengan text kosong
with open(file_path, "a", newline="") as isi_tabel:
    # aktifkan mode writter csv dari file target
    writer = csv.writer(isi_tabel)
    # tambahkan baris dari variabel jajan baru
    writer.writerow(game_baru)



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

    
        

    











