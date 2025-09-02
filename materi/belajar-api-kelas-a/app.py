import requests
url = f"https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Ngawi&country=Indonesia&method=5"
response = requests.get(url) # Http Get (ambil data)
data_json = response.json()
print("JADWAL SHOLAT")
print("-" * 40)
print(data_json)

print("-"*40)
print(f"--Maghrib -->{data_json["data"]["timings"]["Maghrib"]}")

jadwal_sholat = data_json["data"]["timings"]
print(f"Jadwal sholat: {jadwal_sholat["Fajr"]}")