import sqlite3

connect = sqlite3.connect("database_hewan.db")

connect.execute(
    """
                CREATE TABLE HEWAN(
                id_hewan INT AUTO_INCREMENT PRIMARY KEY,
                nama_hewan VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INTEGER(10),
                thn_ditemukan INTEGER(10)
                )
                """
)

connect.close()