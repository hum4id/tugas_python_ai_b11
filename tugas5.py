def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return float(a + b)


def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None) -> None:
        self.nama: str = nama
        self.nim: str = nim
        self.nilai: list[float] = list(nilai) if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"tambah(5, 7)  = {tambah(5, 7)}")
    print(f"tambah(10)    = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([])            = {rata_rata([])}")
    print()

    print("=== CLASS STUDENT ===")
    mhs1 = Student(nama="Budi Santoso", nim="A123")
    mhs1.tambah_nilai(80.0)
    mhs1.tambah_nilai(85.0)
    mhs1.tambah_nilai(82.5)

    mhs2 = Student(nama="Siti Aminah", nim="B456")
    mhs2.tambah_nilai(65.0)
    mhs2.tambah_nilai(70.0)
    mhs2.tambah_nilai(60.0)

    print("Informasi Mahasiswa 1:")
    print(mhs1)
    print(f"-> Rata-rata: {mhs1.rata_nilai()} | Status: {mhs1.status()}")
    print()

    print("Informasi Mahasiswa 2:")
    print(mhs2)
    print(f"-> Rata-rata: {mhs2.rata_nilai()} | Status: {mhs2.status()}")
