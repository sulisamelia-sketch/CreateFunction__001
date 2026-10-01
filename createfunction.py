#1. Fungsi konversi suhu celcius <-> fahrenheit
def konversi_suhu(suhu, satuan):
    if satuan == 'C':
        # Celsius ke Fahrenheit
        hasil = (suhu * 9/5) + 32
        return hasil
    elif satuan == 'F':
        # Fahrenheit ke Celsius
        hasil = (suhu - 32) * 5/9
        return hasil
    else:
        return "Satuan tidak valid!"

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ").upper()
hasil = konversi_suhu(suhu, satuan)

print("Hasil konversi:", hasil)

#2. Lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: 3.14 * r * r

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

hasil_luas = luas_lingkaran(jari_jari)

print("Luas lingkaran:", hasil_luas)
