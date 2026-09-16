import sqlite3 as s
name = input("Enter Artist name: ")
db = s.connect('chinook.db')
query = "SELECT Title FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId WHERE artists.Name LIKE ?"

params = (f'%{name}%',)
print(query)
print("\nResults found: \n-------------------")
cursor = db.execute(query,params)
for row in cursor:
    print((f'{row[0]}'))

db.commit()
db.close()