import sqlite3
import re
import xml.etree.ElementTree as ET

def lookup(line, key):
	aim = False
	for x in line:
		if aim:
			return x.text
		if x.tag == 'key' and x.text == key:
			aim = True
	return 'None'

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()
cur.executescript('''
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Track;
''')
cur.executescript('''
	CREATE TABLE Artist (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	);

	CREATE TABLE Genre (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE
	);

	CREATE TABLE Album (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id INTEGER,
		title TEXT UNIQUE
	);

	CREATE TABLE Track (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT UNIQUE,
		album_id INTEGER,
		genre_id INTEGER,
		len INTEGER, rating INTEGER, count INTEGER
	);
''')

fd = open('library.xml')
lines = ET.fromstring(fd.read()).findall('dict/dict/dict')
fd.close()

for line in lines:
	if ( lookup(line, 'Track ID') is None ) : continue
	name = lookup(line, 'Name')
	artist = lookup(line, 'Artist')
	genre = lookup(line, 'Genre')
	album = lookup(line, 'Album')
	count = lookup(line, 'Play Count')
	rating = lookup(line, 'Rating')
	length = lookup(line, 'Total Time')
	#if name is None or artist is None or album is None or genre is None: 
	#	continue
	print(name, artist, genre, album, count, rating, length)
	
	cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) 
	)
	cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) 
	)
	cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
	genre_id = cur.fetchone()[0]

	cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id) 
	)
	cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
	album_id = cur.fetchone()[0]

	cur.execute('''
		INSERT OR REPLACE INTO Track
		(title, album_id, genre_id, len, rating, count)
		VALUES ( ?, ?, ?, ?, ?, ? )''',
		( name, album_id, genre_id, length, rating, count )
	)

conn.commit()
cur.close()
