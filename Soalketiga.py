#soal 3
# Meminta input dari pengguna untuk nilai n yang menentukan banyaknya elemen deret Fibonacci
n = int(input("Masukkan nilai n: "))

# Menginisialisasi dua variabel untuk menyimpan angka Fibonacci, a untuk 0 dan b untuk 1
a, b = 0, 1
# Membuat list kosong untuk menyimpan hasil deret Fibonacci
hasil = []

# Menggunakan loop untuk menghasilkan n angka dalam deret Fibonacci
for i in range(n):
    hasil.append(a)  # Menambahkan nilai a ke dalam list hasil
    a, b = b, a + b  # Memperbarui a dan b untuk iterasi berikutnya (a menjadi b, b menjadi a + b)

# Menampilkan deret Fibonacci yang dihasilkan hingga n
print("Deret Fibonacci hingga", n, ":", hasil)
