import sqlite3

connect = sqlite3.connect("database_hewan.db")

connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('1', 'Orangutan', 'Mamalia', 'Sumatera', 14000, 2021)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('2', 'Harimau Sumatera', 'Mamalia', 'Sumatera', 400, 2020)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('3', 'Komodo', 'Reptil', 'Nusa Tenggara', 3000, 2019)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('4', 'Anoa', 'Mamalia', 'Sulawesi', 5000, 2022)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('5', 'Badak Jawa', 'Mamalia', 'Jawa', 72, 2021)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('6', 'Kuskus', 'Mamalia', 'Papua', 50, 2020)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('7', 'Trenggiling', 'Mamalia', 'Sumatera', 90, 2022)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('8', 'Burung Cendrawasih', 'Burung', 'Papua', 45, 2021)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('9', 'Penyu Hijau', 'Reptil', 'NTT', 20, 2022)"
)
connect.execute(
    "INSERT INTO HEWAN (id_hewan, nama_hewan, jenis, asal, jml_skrng, thn_ditemukan) VALUES ('10', 'Gajah Sumatera', 'Mamalia', 'Sumatera', 2500, 2023)"
)
connect.commit()

connect.close()