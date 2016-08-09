#!/usr/bin/python
import MySQLdb

#Asks information about movie and inserts it into a database.
name = raw_input("Movie Title in Finnish: ")
orig_title = raw_input("Original Movie title: ")

def versio():
	version = raw_input("1 for DVD or 2 for Bluray: ")
        if version == "1":
                version = "DVD"
                return version
        elif version == "2":
                version = "Bluray"
                return version
        else:
                print "Invalid choice. Try again."
                dvdbluray = versio()
		return dvdbluray

dvdbluray = versio()

def movie():
        series = raw_input("1 for TV-show or 2 for Movie: ")
        if series == "1":
                series = "TV-Sarja"
                return series
        elif series == "2":
                series = "Elokuva"
                return series
        else:
                print "Invalid choice. Try again."
                showormovie = movie()
                return showormovie

showormovie = movie()
year = raw_input("Year: ")
genre = raw_input("Genre: ")

db = MySQLdb.connect(host="",    # your database host
                     user="",         # your username
                     passwd="",  # your password
                     db="")        # name of the database

cursor = db.cursor()

# execute SQL insert statement
cursor.execute("INSERT INTO movies_movdb_movies (title, org_title, version, series, year, short_title) VALUES (%s, %s, %s, %s, %s, %s)", (name, orig_title, dvdbluray, showormovie, year, genre))

# commit your changes
db.commit()

print "Movie has been inserted into database"
