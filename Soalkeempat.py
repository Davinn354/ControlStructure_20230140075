#soal 4
# Meminta input dari pengguna untuk nilai n yang menentukan batas hingga angka ganjil yang akan ditampilkan
n = int(input("Masukkan nilai n: "))

# Menampilkan pesan untuk memberitahu pengguna bahwa angka ganjil hingga n akan ditampilkan
print("Angka ganjil hingga", n, ":")

# Menggunakan loop untuk iterasi dari 1 hingga n (inklusif)
for i in range(1, n + 1):
    # Memeriksa apakah angka i adalah angka ganjil dengan menggunakan operator modulus
    if i % 2 != 0:
        print(i)  # Jika i adalah angka ganjil, tampilkan angka tersebut
