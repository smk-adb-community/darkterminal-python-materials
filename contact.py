import json

# Fungsi untuk membuat semua data kontak dari file JSON
def load_kontak():
    try:
        with open("kontak.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menampilkan kontak
def display_kontak(daftar_kontak):
    if not daftar_kontak:
        print("||===|| Menu ||===||")
        print("Daftar kontak kosong")
        print("||===|| Menu ||===||")
    else:
        for kontak in daftar_kontak:
            print("_[^-^]_[^-^]_[^-^]_[^-^]_")
            print("Nama:", kontak["nama"])
            print("Email:", kontak["email"])
            print("Telepon:", kontak["telepon"])
            print("_[^-^]_[^-^]_[^-^]_[^-^]_")

# Fungsi untuk membuat kontak baru
def new_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon: ")
    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }
    return kontak

# Fungsi untuk menyimpan kontak ke file JSON
def save_kontak(daftar_kontak):
    with open("kontak.json", "w") as file:
        json.dump(daftar_kontak, file)

# Fungsi untuk mencari kontak
def cari_kontak(daftar_kontak):
    nama = input("Masukkan nama kontak yang ingin dicari==> ")
    for kontak in daftar_kontak:
        if kontak["nama"] == nama:
            print("Kontak ditemukan:")
            print("Nama:", kontak["nama"])
            print("Email:", kontak["email"])
            print("Telepon:", kontak["telepon"])
            return
    print(f"Maaf, kontak {nama} tidak ditemukan:(.")

# Fungsi untuk mengahapus kontak
def hapus_kontak(daftar_kontak):
    nama = input("Masukkan nama kontak yang ingin dihapus==> ")
    for kontak in daftar_kontak:
        if kontak["nama"] == nama:
            daftar_kontak.remove(kontak)
            print(f"Anda telah menghapus kontak {nama}.")
            return
    print(f"Maaf, kontak {nama} tidak ditemukan:(.")
