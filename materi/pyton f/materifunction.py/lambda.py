# Function dengan def

def hello(nama):
    # ("halo mr.",nama)
    # kasih "f" dia awal string untuk menyisipkan variable/parameter
    print(f"Halo tuan.{nama}")
    print("Bagaimana kabar anda tuan?")

print("------------------------------------------------------")

# Lambda untuk menulis fungsi yang ringkas dengan 1 bari saja
# Sering disebut fungsi anonim

hello2 = lambda nama: print(f"Hello Mr.{nama}")
# Panggil fungsi2 nya di bawah ini
hello("Azzam")
hello("Dika")
print("---------------------")
hello2("Firanda")
hello2("Harun")
print("---------------------")
# contoh penerapan lambda dengan higher order function
# map() --- sorted() --- filter()
jajanMingguan=[5000,10000,50000,25000,15000]
# sorted() ----> untuk mengurutkan data
urutanUang=sorted(jajanMingguan)
urutanUangterbalik=sorted(jajanMingguan,reverse=True)
print(f"Urutan uang dari kecil: {urutanUang}")
print(f"Urutan uang terbalik: {urutanUangterbalik}")
print("---------------------")
# map()--> mentranformasi data
kurangiUang=map(lambda uang: uang-500,jajanMingguan)
print("---------------------")
# List() mengubah data objek map menjadi bentuk list
listKurangiUang = list(kurangiUang)
print(f"Map uang berkurang: {listKurangiUang}")
print("---------------------")
# Filter() menyaring / memfilter data 
JajanBanyak=filter(lambda uang: uang>=30000, jajanMingguan)
listJajanBanyak= list(JajanBanyak)
print(f"Filter jajan diatas 30rb: {listJajanBanyak}")











