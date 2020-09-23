import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cursor = connection.cursor()

#Deleting db
cursor.execute('DROP TABLE IF EXISTS Counts')
#creating new db
cursor.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
