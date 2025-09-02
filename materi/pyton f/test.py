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
    
rukunIslam=('Syahadat','shalat','zakat','puasa','haji')

print("RUKUN ISLAM")
for i in range(len(rukunIslam)):
    print(f"{i + 1}. {rukunIslam[i]}")