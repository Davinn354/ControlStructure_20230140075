#Soal 1`
# Meminta input dari pengguna berupa nilai mahasiswa dan mengonversinya ke tipe data integer
Nilai = int(input("Masukan Nilai Mahasiswa"))

# Memeriksa apakah nilai mahasiswa 90 atau lebih besar, jika ya, tampilkan pesan "Excellent performance"
if Nilai >=90:
    print(" Excellent performance")

# Jika nilai antara 80 hingga 89, tampilkan pesan "Very Good performance"
elif Nilai >=80:
    print(" Very Good performance")

# Jika nilai antara 70 hingga 79, tampilkan pesan "Good performance"
elif Nilai >=70:
    print(" Good performance")

# Jika nilai antara 60 hingga 69, tampilkan pesan "Average performance"
elif Nilai >=60:
    print(" average performance")
