import sqlite3

con = sqlite3.connect('database_backup/test.db')
f = open('database_backup/backupdatabase_dump.sql','r')
str = f.read()
cur = con.cursor()
cur.executescript(str)
