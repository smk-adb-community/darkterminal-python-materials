import contact

# Memuat semua kontak yang ada di file JSON
daftar_kontak = contact.load_kontak()

while True:
    print("###### Menu ######")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("5. Cari Kontak")
    print("0. Keluar Program")
    print("###### Menu ######")

    menu = input("Pilih menu : ")

    if menu == "0":
        contact.save_kontak(daftar_kontak)
        break
    elif menu == "1":
        contact.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = contact.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        daftar_kontak_baru = contact.ubah_kontak(daftar_kontak)
        contact.save_kontak(daftar_kontak)
    elif menu == "4":
        contact.hapus_kontak(daftar_kontak)
    elif menu == "5":
        contact.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai berjalan, sampai jumpa")