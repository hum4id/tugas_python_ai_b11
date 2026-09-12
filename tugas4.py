print("=" * 60)
print("1. LIST - AKSES & MANIPULASI")
print("=" * 60)

data_campuran = ["Python", 100, "Infinite", 3.14, "Learning", 2024, "Batch 11"]
print(f"List awal ({len(data_campuran)} elemen): {data_campuran}")

print(f"Elemen pertama        : {data_campuran[0]}")
print(f"Elemen terakhir       : {data_campuran[-1]}")

print(f"Slicing [1:6:2]       : {data_campuran[1:6:2]}")
print(f"Slicing reverse [::-1]: {data_campuran[::-1]}")

print("\n--- Manipulasi List (Sebelum & Sesudah) ---")
print(f"Sebelum append() : {data_campuran}")
data_campuran.append("Data Baru")
print(f"Sesudah append() : {data_campuran}\n")

print(f"Sebelum insert() : {data_campuran}")
data_campuran.insert(2, "Disisipkan")
print(f"Sesudah insert() : {data_campuran}\n")

print(f"Sebelum extend() : {data_campuran}")
data_campuran.extend([999, "Akhir"])
print(f"Sesudah extend() : {data_campuran}\n")

print(f"Sebelum pop()    : {data_campuran}")
item_pop = data_campuran.pop()
print(f"Sesudah pop()    : {data_campuran} (Item terhapus: '{item_pop}')\n")

print(f"Sebelum remove() : {data_campuran}")
data_campuran.remove("Disisipkan")
print(f"Sesudah remove() : {data_campuran}\n")

print("=" * 60)
print("2. TUPLE - IMMUTABILITY & UNPACKING")
print("=" * 60)

data_tuple = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
print(f"Tuple               : {data_tuple}")

print(f"Panjang tuple       : {len(data_tuple)}")
print(f"Elemen indeks 0     : {data_tuple[0]}")
print(f"Elemen indeks 4     : {data_tuple[4]}")

pertama, kedua, ketiga, *hari_lainnya = data_tuple
print("\nHasil Unpacking:")
print(f"Variabel pertama    : {pertama}")
print(f"Variabel kedua      : {kedua}")
print(f"Variabel ketiga     : {ketiga}")
print(f"Variabel *hari_lain : {hari_lainnya}\n")

print("=" * 60)
print("3. SET - KEUNIKAN & OPERASI HIMPUNAN")
print("=" * 60)

list_dengan_duplikat = [1, 2, 2, 3, 4, 4, 4, 5]
set_unik = set(list_dengan_duplikat)
print(f"List awal ada duplikat: {list_dengan_duplikat}")
print(f"Setelah diubah ke set : {set_unik} (duplikat otomatis dihapus)\n")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A : {set_a}")
print(f"Set B : {set_b}")

print(f"Union (|)               : {set_a | set_b}")
print(f"Intersection (&)        : {set_a & set_b}")
print(f"Difference (A - B)      : {set_a - set_b}")
print(f"Difference (B - A)      : {set_b - set_a}")
print(f"Symmetric Diff (^)      : {set_a ^ set_b}\n")

print("=" * 60)
print("4. DICTIONARY - KEY/VALUE DASAR")
print("=" * 60)

mahasiswa = {
    "nama": "Budi Santoso",
    "nim": "12345678",
    "angkatan": 2022,
    "kota": "Bandung"
}
print(f"Dict awal: {mahasiswa}\n")

mahasiswa["jurusan"] = "Teknik Informatika"
print(f"Setelah tambah key 'jurusan'  : {mahasiswa}")

mahasiswa["kota"] = "Jakarta"
print(f"Setelah ubah nilai 'kota'     : {mahasiswa}")

del mahasiswa["angkatan"]
print(f"Setelah hapus key 'angkatan'  : {mahasiswa}\n")

print(f"Keys()   : {list(mahasiswa.keys())}")
print(f"Values() : {list(mahasiswa.values())}")
print(f"Items()  : {list(mahasiswa.items())}\n")

print("Iterasi key & value:")
for key, value in mahasiswa.items():
    print(f"- {key}: {value}")
print()

print("=" * 60)
print("5. NESTED STRUCTURES")
print("=" * 60)

daftar_buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Filosofi Teras", "penulis": "Henry Manampiring", "tahun": 2018},
    {"judul": "Laut Bercerita", "penulis": "Leila S. Chudori", "tahun": 2017},
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018}
]

print("Daftar Judul Buku:")
for i, buku in enumerate(daftar_buku, start=1):
    print(f" {i}. {buku['judul']} ({buku['penulis']})")

tahun_batas = 2015
buku_modern = [buku["judul"] for buku in daftar_buku if buku["tahun"] >= tahun_batas]
print(f"\nBuku terbit >= {tahun_batas} (List Comprehension):")
print(buku_modern)
print()

print("=" * 60)
print("6. COMPREHENSION & UTILITAS")
print("=" * 60)

angka_1_20 = list(range(1, 21))
list_genap = [x for x in angka_1_20 if x % 2 == 0]
list_kuadrat = [x**2 for x in angka_1_20]

print(f"List Genap (1-20)   : {list_genap}")
print(f"List Kuadrat (1-20) : {list_kuadrat}\n")

dict_ganjil_genap = {n: ("genap" if n % 2 == 0 else "ganjil") for n in range(1, 11)}
print("Dict Comprehension 1-10 (genap/ganjil):")
print(dict_ganjil_genap)
print()

kalimat = "Belajar Pemrograman Python Mandiri Infinite Learning"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}
print(f"Kalimat              : '{kalimat}'")
print(f"Set Huruf Unik (a-z) : {sorted(huruf_unik)}")
print()

print("=" * 60)
print("7. KEANGGOTAAN & PENCARIAN SEDERHANA")
print("=" * 60)

daftar_buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Melon"]
kumpulan_hobi = {"Membaca", "Coding", "Bermain Game", "Olahraga"}

cari_buah = "Pisang"
if cari_buah in daftar_buah:
    posisi = daftar_buah.index(cari_buah)
    print(f"'{cari_buah}' DITEMUKAN di dalam list pada indeks ke-{posisi}.")
else:
    print(f"'{cari_buah}' TIDAK DITEMUKAN di dalam list.")

cari_buah_lain = "Durian"
ada = cari_buah_lain in daftar_buah
print(f"Apakah '{cari_buah_lain}' ada di list? {ada}")

cari_hobi = "Coding"
print(f"Apakah '{cari_hobi}' ada di set hobi? {cari_hobi in kumpulan_hobi}")
print("=" * 60)
