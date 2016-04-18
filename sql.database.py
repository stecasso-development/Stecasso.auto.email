from os import getenv
import pymssql

conn = pymssql.connect('192.168.0.48','Stephan','Cocolo3co','Stecasso')
cursor = conn.cursor()
cursor.execute("""
INSERT INTO Users (primaryKey, username) VALUES (2, 'cas')
""")
conn.commit()

cursor.execute('SELECT (primaryKey) FROM Users')
row = cursor.fetchone()
while row:
    print("ID=%d" % (row[0]))
    row = cursor.fetchone()

conn.close()

