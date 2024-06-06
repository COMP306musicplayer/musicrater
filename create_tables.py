import mysql.connector
import pandas as pd
import csv

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234", 
  auth_plugin='mysql_native_password'
)

db_cursor = db_connection.cursor(buffered=True)

##db_cursor.execute("CREATE DATABASE ratingApp")

db_cursor.execute("USE ratingApp")
# create Artists table
db_cursor.execute("""CREATE TABLE ARTISTS (artist_id VARCHAR(50) PRIMARY KEY NOT NULL,  
                                          artist_fname VARCHAR(50), 
                                          artist_mname VARCHAR(50), 
                                          artist_lname VARCHAR(50),
                                          artist_genre VARCHAR(50))""")

insert_artists = (
    "INSERT INTO ARTISTS(artist_id, artist_fname, artist_mname, artist_lname, artist_genre) "
    "VALUES (%s, %s, %s, %s, %s)"
)


# create Albums table
db_cursor.execute("""CREATE TABLE ALBUMS (album_id VARCHAR(50) PRIMARY KEY NOT NULL,  
                                          album_title VARCHAR(50), 
                                          album_releaseDate DATETIME,
                                          maker_id VARCHAR(50),
                                          album_genre VARCHAR(50),
                                          FOREIGN KEY(maker_id) REFERENCES ARTISTS(artist_id) 
                                          ON DELETE CASCADE
                                          ON UPDATE NO ACTION)""")

insert_albums = (
    "INSERT INTO ALBUM(album_id, album_title, album_releaseDate, album_genre) "
    "VALUES (%s, %s, %s, %s)"
)


# create Songs table
db_cursor.execute("""CREATE TABLE SONGS (song_id VARCHAR(50) PRIMARY KEY NOT NULL,  
                                          song_title VARCHAR(50), 
                                          song_duration VARCHAR(50),
                                          song_rating INTEGER,
                                          singer_id VARCHAR(50),
                                          inalbum_id VARCHAR(50),
                                          song_genre VARCHAR(50),
                                          FOREIGN KEY(singer_id) REFERENCES ARTISTS(artist_id) ON DELETE CASCADE
                                          ON UPDATE NO ACTION,
                                          FOREIGN KEY(inalbum_id) REFERENCES ALBUMS(album_id) ON DELETE CASCADE
                                          ON UPDATE NO ACTION)""")

insert_songs = (
    "INSERT INTO SONGS(song_id, song_title, song_duration, song_rating, singer_id, inalbum_id, song_genre) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)


# create Users table
db_cursor.execute("""CREATE TABLE USERS (user_id VARCHAR(50) PRIMARY KEY NOT NULL,  
                                          user_userName VARCHAR(50), 
                                          user_password VARCHAR(50) 
                                          )""")

insert_user = (
    "INSERT INTO USERS(user_id, user_userName, user_password) "
    "VALUES (%s, %s, %s)"
)

# create LikedSongs table
db_cursor.execute("""CREATE TABLE LikedSongs (song_id VARCHAR(50),  
                 user_id VARCHAR(50),
                 FOREIGN KEY(song_id) REFERENCES SONGS(song_id) ON DELETE CASCADE
                 ON UPDATE NO ACTION,
                 FOREIGN KEY(user_id) REFERENCES USERS(user_id) ON DELETE CASCADE
                 ON UPDATE NO ACTION)""")

insert_likedsong = (
    "INSERT INTO LikedSongs(song_id, user_id) "
    "VALUES (%s, %s)"
)


db_cursor.execute("""alter table LikedSongs add primary key (song_id, user_id)""")

# create LikedAlbums table
db_cursor.execute("""CREATE TABLE LikedAlbums (album_id VARCHAR(50),  
                 user_id VARCHAR(50),
                 FOREIGN KEY(album_id) REFERENCES ALBUMS(album_id) ON DELETE CASCADE
                 ON UPDATE NO ACTION,
                 FOREIGN KEY(user_id) REFERENCES USERS(user_id) ON DELETE CASCADE
                 ON UPDATE NO ACTION)""")

insert_likedalbum = (
    "INSERT INTO LikedAlbums(album_id, user_id) "
    "VALUES (%s, %s)"
)

db_cursor.execute("""alter table LikedAlbums add primary key (album_id, user_id)""")
