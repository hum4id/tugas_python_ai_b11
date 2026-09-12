print("=== 1. DEKLARASI VARIABEL DAN TIPE DATA ===")

var_string = "Belajar Python di Infinite Learning"
var_integer = 25
var_float = 3.14
var_boolean = True
var_list = ["Python", "JavaScript", "HTML", "CSS"]

print(f"Variabel String   : {var_string} | Tipe: {type(var_string)}")
print(f"Variabel Integer  : {var_integer} | Tipe: {type(var_integer)}")
print(f"Variabel Float    : {var_float} | Tipe: {type(var_float)}")
print(f"Variabel Boolean  : {var_boolean} | Tipe: {type(var_boolean)}")
print(f"Variabel List     : {var_list} | Tipe: {type(var_list)}")
print()

print("=== 2. MANIPULASI STRING ===")

kata_depan = "Halo"
kata_belakang = "Dunia"

gabungan_kata = kata_depan + " " + kata_belakang
print("Teks gabungan               :", gabungan_kata)

panjang_karakter = len(gabungan_kata)
print(f"Panjang teks '{gabungan_kata}' : {panjang_karakter} karakter")

print("Huruf besar (.upper())      :", gabungan_kata.upper())
print("Huruf kecil (.lower())      :", gabungan_kata.lower())
print()

print("=== 3. OPERASI MATEMATIKA SEDERHANA ===")

angka_a = 15
angka_b = 4

print(f"Nilai a = {angka_a}, Nilai b = {angka_b}")
print(f"Penjumlahan (+)        : {angka_a} + {angka_b} = {angka_a + angka_b}")
print(f"Pengurangan (-)        : {angka_a} - {angka_b} = {angka_a - angka_b}")
print(f"Perkalian (*)          : {angka_a} * {angka_b} = {angka_a * angka_b}")
print(f"Pembagian (/)          : {angka_a} / {angka_b} = {angka_a / angka_b}")
print(f"Pembagian Bulat (//)   : {angka_a} // {angka_b} = {angka_a // angka_b}")
print(f"Modulus/Sisa Bagi (%)  : {angka_a} % {angka_b} = {angka_a % angka_b}")
print()

print("=== 4. LIST DAN AKSES ELEMEN ===")

daftar_buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Semangka"]
print("List awal (5 item) :", daftar_buah)

print("Elemen pertama (indeks 0)  :", daftar_buah[0])
print("Elemen ketiga (indeks 2)   :", daftar_buah[2])
print("Elemen terakhir (indeks -1):", daftar_buah[-1])

daftar_buah.append("Melon")
print("Setelah append('Melon')    :", daftar_buah)

daftar_buah.remove("Jeruk")
print("Setelah remove('Jeruk')    :", daftar_buah)

item_dihapus = daftar_buah.pop()
print(f"Setelah pop() (menghapus '{item_dihapus}'):", daftar_buah)
print()

print("=== 5. PENGGUNAAN INPUT DARI USER ===")

nama_user = input("Masukkan nama Anda : ")
umur_user = input("Masukkan umur Anda : ")

print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
