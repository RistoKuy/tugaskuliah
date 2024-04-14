# Aristo Baadi - 41823010006
# Universitas Mercu Buana 
# Tugas 1 - Pemrograman Lanjut

# Intro & Variabel
print("Selamat datang di Aplikasi Perhitungan Nilai Mahasiswa")
nilai_tugas = float(input("Silahkan Masukkan Nilai Tugas Anda: "))
nilai_uts = float(input("Silahkan Masukkan Nilai UTS Anda: "))
nilai_uas = float(input("Silahkan Masukkan Nilai UAS Anda: "))

# Perhitungan Nilai Akhir
nilai_akhir = (nilai_tugas*0.25) + (nilai_uts*0.35) + (nilai_uas*0.40)

# Penentuan Nilai dalam Huruf (Grade)
if nilai_akhir >= 85 and nilai_akhir <= 100 :
    grade = "A"
elif nilai_akhir >= 80 and nilai_akhir < 85:
    grade = "A-"
elif nilai_akhir >= 75 and nilai_akhir < 80:
    grade = "B+"
elif nilai_akhir >= 70 and nilai_akhir < 75:
    grade = "B"
elif nilai_akhir >= 65 and nilai_akhir < 70:
    grade = "B-"
elif nilai_akhir >= 60 and nilai_akhir < 65:
    grade = "C+"
elif nilai_akhir >= 55 and nilai_akhir < 60:
    grade = "C"
elif nilai_akhir >= 50 and nilai_akhir < 55:
    grade = "C-"
elif nilai_akhir >= 30 and nilai_akhir < 50:
    grade = "D"
elif nilai_akhir < 30 :
    grade = "E"
else :
    grade = "Undefined"

# Menampilkan nilai akhir dan grade
print("Nilai Akhir Anda :", nilai_akhir)
print("Dalam Huruf :", grade)