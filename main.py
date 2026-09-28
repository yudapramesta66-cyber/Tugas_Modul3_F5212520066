import time
import os

# Membersihkan layar terminal agar antarmuka terlihat bersih
os.system('cls' if os.name == 'nt' else 'clear')

lebar = 55
print("=" * lebar)
print("SISTEM INFORMASI KEBENCANAAN TERPADU & NOMAD FINDER".center(lebar))
print("=" * lebar)

# Efek animasi loading sederhana
print("\nMenginisialisasi sistem", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" [OK]")

print("Memuat profil pengguna", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" [OK]\n")

# Menampilkan biodata dengan format kotak (box) yang rapi
print("-" * lebar)
print(f"| {'Nama   : Yuda Pramesta'.ljust(lebar - 4)} |")
print(f"| {'NIM    : F5212520066'.ljust(lebar - 4)} |")
print(f"| {'Kelas  : Sistem Informasi (SI-B)'.ljust(lebar - 4)} |")
print(f"| {'Status : UI/UX & System Analyst (Active)'.ljust(lebar - 4)} |")
print("-" * lebar)

print("\n[SYSTEM] Setup Environment & Git berhasil diinisialisasi!")
print("[SYSTEM] Sistem siap menerima perintah...\n")