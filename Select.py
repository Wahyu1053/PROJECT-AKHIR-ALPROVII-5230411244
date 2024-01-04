import sqlite3

connect = sqlite3.connect("database_hewan.db")
cursor = connect.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data HEWAN")
print("=" * 80)
print(
    "{:<5} {:<20} {:<20} {:<20} {:<10} {:<20} ".format(
        "id_hewan", "nama_hewan", "jenis", "asal", "jml_skrng", "thn_ditemukan"
    )
)
print("-" * 80)
for row in rows:
    print(
        "{:<5} {:<20} {:<20} {:<20} {:<10} {:<20} ".format(
            row[0], row[1], row[2], row[3], row[4], row[5]
        )
    )

connect.close()