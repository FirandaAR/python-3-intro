# Membuat bank se derhana 
# percobaan #1

saldo = 0
sandi = "1234"
kode = input("Masukkan Sandi Anda:")
pilihan = int


if sandi != kode:
    print("sandi yang anda masukkan salah")
else:
    pilihan= int(input("1.Tarik Saldo 2.Isi Saldo 3."))

if pilihan == 1 :
    tarikSaldo=input("Masukkan Nominal yang ingin anda tarik:")
elif pilihan == 2:
    isisaldo=input("Masukkan nominal yang ingin anda isi :")

