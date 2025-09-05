# 1

piketMasak = ["Banyu","Azka","Bilal","Hakim"]
print("Piket Masak Hari ini adalah:")
for jadwal in piketMasak:
    print('-',jadwal)
# 2
print("")
rukunIman = ("Iman kepada Allah","Iman kepada malaikat","Iman kepada kitab","Iman kepada nabi dan rasul","Iman kepada hari akhir","Iman kepada Qadha dan Qadar")
rukunIslam=("Syahadat","Sholat","Zakat","Puasa","Haji")
print("Rukun iman ada 6: ")
for rukun in rukunIman:
    print("-",rukun)
print("")
print("Rukun Islam ada 5: ")
for rukun2 in rukunIslam:
    print("-",rukun2)
print("")

#3
print("Kitab yang akan dipelajari hari ini: ")
kitab = {'Kitab fiqih','kitab Tauhid','Kitab injil',}
for kutub in kitab:
    print('-',kutub)
print("----------------------------")

#4
bioData1 = {
    "nama":"Fatimah",
    "Asal":'jawa barat',
    'umur':'15',
    'kelas':'1 SMA',
    'hobi':'Murojaah',
    'sifat': {
        'sifat1':'pemalu',
        'sifat2':'rajin',
        'sifat3':'shalihah',
        'sifat4':'patuh'
    }
}
print("Biodata My istri gwe dimasa depan (Aamiin): ")
print("")
for keys,values in bioData1.items():
    print(f"{keys}: {values}")
print("--------------------------------------------------")
print("Atau dengan kode yang lebih ribet tapi hasil nya ")
print("")
print("Nama: ",bioData1 ["nama"])
print("Kelas: ",bioData1["kelas"])
print("Asal: ",bioData1["Asal"])
print("Umur: ",bioData1["umur"])
print("Hobi: ",bioData1["hobi"])
print("Sifat sifat beliau ><: ",bioData1["sifat"]["sifat1"],",",bioData1['sifat']['sifat2'],",",bioData1['sifat']['sifat3'],",",bioData1['sifat']['sifat4'])

