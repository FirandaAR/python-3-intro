
nama = input("Masukkan Nama Lengkap Mu Dong:")
umur = int (input("Berapa Sih Umurmu :"))
kelas = input("Lo Kelas Berapa :")
citaCita = input("Cita-cita Lo Apa Nih:")
hobi = input("Hobi lo apa:")
waktuBelajar = input("Lebih Suka Belajar Pagi apa malam? ")
sekarang = int (2025)
tahunLahir = sekarang - umur
print("")
print("")
print("1.Wibu (bau bawang)")
print("2.gamer (Rank jalan teruss)")
print("3.K popers (Pencinta plastik wkwwk)")
print("4.Anak konten(Apapun untuk konten)")
print("5.Anak nongki(Yang penting ngumpul)")
print("")
tipe = int(input("Tipe digital lo apa nih ketik angka aja"))

if tipe == 1:
    waifu = input("Siapa Waifu/husbu mu?  ")
elif tipe == 2:
    game = input("Game favorit lo apa?  ")
elif tipe == 3:
    bias = input("Siapa bias kamu:?  ")
elif tipe == 4:
    plat = input("Konten lo biasa nya pake platform mana?  ")
else:
    tempat = input("Biasa nya nongkrong dimana?  ")

if tipe == 1:
    tipe = ("Wibu (bau bawang)")
elif tipe == 2:
    tipe = ("Gamer")
elif tipe == 3:
    tipe = ("K popers(Bauuu)")
elif tipe == 4:
    tipe = ("Anak Konten")
else:
    tipe = ("Anak nongki")
             
    

print("===========================================")
for i  in range (3):
    print ("")
print("Nama Saya:" ,nama)
print("Umur Saya:" ,umur)
print("Saya Sekarang Kelas:" ,kelas)
print("Hobi saya :" , hobi)
print("Bagi gw belajar enakan:" ,waktuBelajar)
print("Saya lahir pada tahun:",tahunLahir)
for i in range (3):
    print("")


print ("======Tipe Digital======")
print("")
print("")
print ("Tipe digital:" ,tipe,)
if tipe == 1:
    print("waifu/husbu gw: ",waifu)
elif tipe == 2:
    print("Game favorit:",game)
elif tipe == 3:
    print("bias gw:",bias)
elif tipe == 4:
    print("Gw biasa nya ngonten di" ,plat)
elif tipe == 5:
    print("Gw biasa nya nongki di", tempat)
print("")
print("")


bau = input (f"Teman disebelah mu bau gak ? 1/2   \n "
            f" 1.iya\n"
            f" 2.gak:  ")

if bau == "1":
    print("Wah kasih parfum biar wangi")
else: 
    print("Wah pasti orang nya rajin mandi")
print("")
print("")
print("")
print("")
print("Terims",nama,"yang gantenggggg/cantikkk abieez")    



