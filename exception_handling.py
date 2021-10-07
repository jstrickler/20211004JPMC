import sqlite3

file_path = "DATA/wombats.txt"
with open(file_path) as file_in:
    pass

values = [5, 42, -12, 16, 8]
print(values[99])

x = 23
special_values = 8.3, 2.9, 0, 55.6, 42
for sv in special_values:
    result = x / sv
    print(result)

with sqlite3.connect('animals/cryptids.db') as conn:
    cursor = conn.cursor()
    cursor.execute('select name, species from cryptids')
    for row in cursor.fetchall():
        print(row)
