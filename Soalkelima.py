#soal ke lima 5
# Meminta input dari pengguna untuk nilai n yang menentukan jumlah baris yang akan dicetak
n = int(input("Masukkan nilai n: "))

# Loop pertama untuk iterasi dari 1 hingga n (inklusif), menentukan angka yang akan dicetak
for i in range(1, n + 1):
    # Loop kedua untuk mencetak angka i sebanyak i kali
    for j in range(i):
        print(i, end=" ")  # Mencetak angka i tanpa membuat baris baru (end=" " untuk spasi)
    print()  # Mencetak baris baru setelah mencetak angka i
