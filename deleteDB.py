import sqlite3
 
conn = sqlite3.connect("music.db")
cursor = conn.cursor()
 
sql = """
DELETE FROM albums
WHERE artis = 'John Doe'
"""
cursor.execute(sql)
conn.commit()