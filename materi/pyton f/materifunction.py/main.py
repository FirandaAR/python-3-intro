import ranking

nilai = [75,35,100,87,93,85]
nilai_urut = ranking.urutkan_nilai(nilai)
print(f"Nilai santri: {nilai_urut}")

nilai_tertinggi = ranking.nilai_tertinggi(nilai)
print(f'Nilai tertinggi santri: {nilai_tertinggi}')

nilai_terkecil=ranking.nilai_terkecil(nilai)
print(f"Nilai terendah santri: {nilai_terkecil}")
print("===============================")
# VERSI SIMPLE NYAAAA
print(f"Nilai santri: {ranking.urutkan_nilai(nilai)}")
print(f"Nilai tertinggi: {ranking.nilai_tertinggi(nilai)}")
print(f"Nilai terkecil: {ranking.nilai_terkecil(nilai)}")

print("EMOJII")
print("++++++++++++")
import emoji
mood=["Senang","Biasa","Sedih","Marah","Muak"]
print(emoji.emoji(mood))

for moody in mood:
    print(emoji.emoji(mood))
