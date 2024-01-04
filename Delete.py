import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Menjalankan query DELETE
jenis = 'Mamalia'  # ID pegawai yang akan dihapus
cursor.execute(f"DELETE FROM hewan WHERE jenis = '{jenis}'")
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data HEWAN dengan Jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data HEWAN dengan Jenis {jenis}.")

# Menutup koneksi
conn.close()
