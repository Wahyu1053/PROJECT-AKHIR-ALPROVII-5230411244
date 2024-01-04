import sqlite3

koneksi = sqlite3.connect("database_hewan.db")
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN WHERE jenis = 'Mamalia' AND asal = 'Sumatera'")
baris_table = kursor.fetchall()

print("Data Hewan:")
print("-" * 80)
print(
    "{:<5} {:<20} {:<20} {:<20} {:<10} {:<20}".format(
        "id_hewan", "nama_hewan", "jenis", "asal", "jml_skrng", "thn_ditemukan"
    )
)
print("_" * 80)
for baris in baris_table:
    print(
        "{:<5} {:<20} {:<20} {:<20} {:<10} {:<20}".format(
            baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]
        )
    )

koneksi.close()