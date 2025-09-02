import json
# import json
print("----------OPEN JSON FILE---------")

file_path_json=r"C:\Users\dell\Desktop\pyton f\materi-handling-data\materi.json"
with open(file_path_json,"r") as file_materi:
    # json load ()--> membaca isi file json
    data_materi=json.load(file_materi)

    # akses data json dengan  'key' nya
    print(f"judul berkas: {data_materi["title"]}")
    print(f"Total kelas A: {data_materi["total"]}")
    print(f"Status santri: {data_materi["status_santri"]}")
    print(f"Status Lulus: {data_materi["status_lulus"]}")
    print(f"Pelajaran: {data_materi["pelajaran"]}")

    # exstrak dengan looping data list nya
    for pelajaran in data_materi["pelajaran"]:
        print(f"---> {pelajaran}")
        
    # extrak semua data array of object surrah
    # key surah : no,nama,ayat,turun
    print("-" * 50) # gandakan simbol dengan perkalian
    print("| No | Nama surah | Ayat | Tempat turun|")
    print("-" * 50) 
    for surah in data_materi['surah']:
        print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} |")
