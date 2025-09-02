print("MATERI 7 -  PYTHON DATA STRUCTURE")
print("-------------------------------------")
# Set -> {} -> tidak berurutan,berubah,tidak duplikat
gameAzka = {"valorant","delta","roblox"}
gameZaky = {"ff","roblox"}
gameAzka.add("minecraft")
gameZaky.add("valorant")

print("Game azka: ", gameAzka)
print("Game zaky: ", gameZaky)
gameGabungan = gameAzka | gameZaky
print("Daftar game: ", gameGabungan)
# for (loop) untuk mengeluarkan isi item dari set
for game in gameGabungan:
    print(game)
    print("--> transfer data",game,"ke PS5")


# Dictionary (dict) ->{key-value} / {kunci:isi}
# -> berurutan,berubah,tidak duplikat
jenisbola ={
    "bola besar":"basket",
    "bola kecil":"kasti",
    "bola lainnya":{
        "umum":"Bola dunia",
        "beda":"Bola lonjong (kwkwkwkw)"
    }
}
print("Jenis bola: ",jenisbola)
print("Bola yang berat dan besar: ",jenisbola["bola besar"])
print("Bola bola lain nya: ",jenisbola["bola lainnya"]["umum"])

# menambah item baru ke dictionary
jenisbola["bola kotak"]="gak adaa"
print("jenis bola saat ini: ",jenisbola["bola kotak"])

# mengubah item dari dictionary
jenisbola["bola besar"]="Football"

#mengghapus item dari dictionary

del(jenisbola["bola kecil"])
print("jenis bola terbaru: ",jenisbola)

# cara ngecek key nya apa aja

print(jenisbola.keys())

# cara ngecek isi nya apa aja

print(jenisbola.values())

# looping 
for bola in jenisbola:
    print(bola)

for isiBola in jenisbola.values():
    print(isiBola)
    
for key, value in jenisbola.items():
    print(f"{key} -> {value}")
print("")
# nested dictionary

kelas = {
    "siswa1": {
        "nama": "harun",
        "umur": 15,
        "asal": "bogor",
        "hobi" : {
            "hobi1":"makan",
            "hobi2":"Bola"
                    
        }       

    }

    
}