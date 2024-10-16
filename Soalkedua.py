#Tugas 2
# Meminta input dari pengguna untuk tiga angka dan mengonversinya ke tipe data integer
a = int(input("Masukan Angka Pertama: "))
b = int(input("Masukan Angka Kedua: "))
c = int(input("Masukan Angka Ketiga: "))

# Memeriksa apakah a adalah angka terbesar dengan membandingkan a dengan b dan c
if a >= b and a >= c:
    AngkaTerbesar = a  # Jika a lebih besar atau sama dengan b dan c, simpan a sebagai AngkaTerbesar
elif b >= a and b >= c:
    AngkaTerbesar = b  # Jika b lebih besar atau sama dengan a dan c, simpan b sebagai AngkaTerbesar
else:
    AngkaTerbesar = c  # Jika tidak ada yang lebih besar, maka c adalah yang terbesar

# Menampilkan angka terbesar yang telah ditemukan
print("Angka Terbesar:", AngkaTerbesar)