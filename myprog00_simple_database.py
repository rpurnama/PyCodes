import sqlite3

koneksi = sqlite3.connect('test00.db')

kursor = koneksi.cursor()

#Create Table
kursor.execute('''CREATE TABLE credentials 
				(Username	TEXT	NOT NULL, 
				Password	CHAR(8)	NOT NULL)''')

#Inser Data
kursor.execute("INSERT INTO credentials \
				VALUES('user00','pass00!')")

koneksi.commit()

koneksi.close()