import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

cursor.execute("SELECT SUM(jml_skrng) FROM hewan")
total_populasi = cursor.fetchone()[0]

print(f"Total Populsi Sejarang: {total_populasi}")

conn.close()