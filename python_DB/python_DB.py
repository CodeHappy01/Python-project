
import sqlite3

conn = sqlite3.connect('files.db')

with conn: #creates table and columns
    cur = conn.cursor() #enables cursor to type sql command
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt TEXT \
        )")
    conn.commit() #commits sql command
conn.close() #closes connection to files.db

#tuple of files
fileList = ('information.docx','Hello.txt','myImage.png',\
    'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('files.db')

for x in fileList:
    if x.endswith('txt'):
        with conn: # adds to table columns
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefore (x,)
        # will denote a one element tuple for each name ending with txt
            cur.execute("INSERT INTO tbl_files(col_txt) VALUES (?)", (x,))
            print(x)

conn.close()
