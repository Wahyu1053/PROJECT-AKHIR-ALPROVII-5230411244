import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
#Update asal dari hewan ‘Komodo’ menjadi ‘Nusa Tenggara Timur’
Id_hewan = 3
# Asal_baru = "Nusa Tenggara Timur"

kursor.execute(f'''
               UPDATE HEWAN SET Asal = "Nusa Tenggara Timur" WHERE Id_hewan = {Id_hewan}
''')

koneksi.commit()

if kursor.rowcount> 0:
    print(f"DATA  DENGAN ID {Id_hewan} BERHASIL DIUBAH")

else:
    print(f"TIDAK ADA DATA HEWAN DENGAN ID{Id_hewan}")

koneksi.close()