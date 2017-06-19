import sqlite3
 
conn = sqlite3.connect("music.db")
cursor = conn.cursor()
 
sql = """
UPDATE albums 
SET artis = 'John Doe' 
WHERE artis = 'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()