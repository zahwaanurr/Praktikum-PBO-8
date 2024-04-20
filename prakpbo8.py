class MasyarakatKampus:
    def __init__(self, golongan="LAINNYA", gaji=150000):
        self.golongan = golongan
        self.gaji = gaji
    
    def display_info(self):
        print(f"Golongan {self.golongan} mendapatkan gaji: {self.gaji}")

class Dosen(MasyarakatKampus):
    def __init__(self):
        super().__init__(golongan="DOSEN", gaji=450000)

class Staff(MasyarakatKampus):
    def __init__(self):
        super().__init__(golongan="STAFF", gaji=300000)

class Lainnya(MasyarakatKampus):
    def __init__(self):
        super().__init__()

print("=============================")
nama = "Zahwa Nur Azkia Putri   |"
nim = "064002300038             |"
print("Nama:", nama)
print("NIM:", nim)
print("=============================")

def main():
    dosen = Dosen()
    staff = Staff()
    lainnya = Lainnya()
    
    dosen.display_info()
    staff.display_info()
    lainnya.display_info()

if __name__ == "__main__":
    main()
