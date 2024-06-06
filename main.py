from customtkinter import *
from frames.loginFrame import LoginFrame
from frames.infoFrame import InfoFrame
from frames.profileFrame import ProfileFrame

import random
import uuid

import mysql.connector
import pandas as pd
import csv

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234", 
  auth_plugin='mysql_native_password'
)
print(db_connection)


# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)

##db_cursor.execute("CREATE DATABASE ratingApp")

db_cursor.execute("USE ratingApp")

# executing cursor with execute method and pass SQL query


# get list of all databases
db_cursor.execute("SHOW DATABASES")

# print all databases
for db in db_cursor:
    print(db)




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
                                          song_duration VARCHAR(50), 
                                          song_title VARCHAR(50),
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


def populate_table(db_connection, db_cursor, insert_query, file_path):
    
    with open(file_path, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        csv_data_list = list(reader)
        for row in csv_data_list[1:]:
            row = tuple(map(lambda x: None if x == "" else x, row[0].split(',')))
            db_cursor.execute(insert_query, row)
        
    db_connection.commit()

    

def findFromSong(songtitle): 
    frommsong_query = """SELECT s.song_id, s.song_title, 'song' as type 
                      FROM SONGS s
                      WHERE s.song_title like '%""" + songtitle + """%' """
    db_cursor.execute(frommsong_query)
    records = db_cursor.fetchall()
    
    return records


def findFromAlbum(albumtitle): 
    fromalbum_query = """SELECT a.album_id, a.album_title, 'album' as type 
                      FROM ALBUMS a
                      WHERE a.album_title like '%""" + albumtitle + """%' """
    db_cursor.execute(fromalbum_query)
    records = db_cursor.fetchall()
    
    return records

def findFromArtist(name): 
    fromartist_query = """SELECT a.artist_id, a.artist_fname, 'artist' as type 
                      FROM ARTISTS a
                      WHERE a.artist_fname like '%""" + name + """%' 
                      OR a.artist_mname like '%""" + name + """%'
                      OR a.artist_lname like '%""" + name + """%' """
    db_cursor.execute(fromartist_query)
    records = db_cursor.fetchall()
    
    return records

def barSearch(songtitle, albumtitle, name):
    songs = findFromSong(songtitle)
    albums = findFromAlbum(albumtitle)
    artists = findFromArtist(name)
    all_results = songs + albums + artists
    
    return all_results

def findFromGenre(genreName):
    frommsonggenre_query = """SELECT s.song_id, s.song_title, 'song' as type 
                      FROM SONGS s
                      WHERE s.song_genre like '%""" + genreName + """%' """
    db_cursor.execute(frommsonggenre_query)
    recordssong = db_cursor.fetchall()
    
    fromalbumgenre_query = """SELECT a.album_id, a.album_title, 'album' as type 
                      FROM ALBUMS a
                      WHERE a.album_genre like '%""" + genreName + """%' """
    db_cursor.execute(fromalbumgenre_query)
    recordsalbum = db_cursor.fetchall()
    
    fromartistgenre_query = """SELECT a.artist_id, a.artist_fname, 'artist' as type 
                      FROM ARTISTS a
                      WHERE a.artist_genre like '%""" + genreName + """%'  """
    db_cursor.execute(fromartistgenre_query)
    recordsartist = db_cursor.fetchall()
    
    all_records = recordssong + recordsalbum + recordsartist
    
    return all_records


def getLikedSongs(user_id):
    fromlikedsong_query = """SELECT s.song_id, s.song_title
                            FROM SONGS s
                            join LikedSongs ls
                            ON s.song_id = ls.song_id
                            WHERE ls.user_id = user_id """
    db_cursor.execute(fromlikedsong_query)
    records = db_cursor.fetchall()
    
    return records


def getLikedAlbums(user_id):
    fromlikedalbums_query = """SELECT a.album_id, a.album_title
                            FROM ALBUMS a
                            join LikedAlbums la
                            ON a.album_id = la.album_id
                            WHERE la.user_id = user_id """
    db_cursor.execute(fromlikedalbums_query)
    records = db_cursor.fetchall()
    
    return records


def getTop10():
    toptensong_query = """SELECT s.song_id, min(s.song_title) as song_title
                            FROM SONGS S
                            join LikedSongs ls
                            on s.song_id = ls.song_id
                            GROUP BY ls.song_id
                            ORDER BY count(ls.user_id) DESC
                            limit 10 """
    
    db_cursor.execute(toptensong_query)
    records = db_cursor.fetchall()
    
    return records





insert_customers = (
    """INSERT INTO ARTISTS (artist_id, artist_fname, artist_mname, artist_lname, artist_genre) VALUES (%s, %s, %s, %s, %s) """
    
)

populate_table(db_connection, db_cursor, insert_customers, "ARTISTS.csv")
  




### Step 2: Insert Albums
##Each album should be linked to one of the artists. Since there are 80 albums and 50 artists, some artists will be linked to multiple albums.


# Step 2: Insert Albums


insert_customers = (
    """INSERT INTO ALBUMS (album_id, album_title, album_releaseDate, maker_id, album_genre)  VALUES (%s, %s, %s, %s, %s) """
    
)

populate_table(db_connection, db_cursor, insert_customers, "ALBUMS.csv")


### Step 3: Insert Songs
##Now, populate the SONGS table with 300 songs. Each song should be linked to one album and one artist. Here, singer_id can be either the same as the album's maker_id or another artist.





insert_customers = (
    """INSERT INTO SONGS (song_id, song_duration, song_title, song_rating, singer_id, inalbum_id, song_genre)  VALUES (%s, %s, %s, %s, %s,%s,%s) """
    
)

populate_table(db_connection, db_cursor, insert_customers, "SONGS.csv")




def login(event):
    print("hey")
    app.geometry("1320x620")
    login_frame.pack_forget()
    info_frame.pack(side="left")
    profile_frame.pack(side="right", fill="both", expand=True)

def logout(event):
    print("wassup")
    app.geometry("770x750")
    profile_frame.pack_forget()
    info_frame.pack_forget()
    login_frame.pack()



app = CTk()
app.geometry("770x750")

set_default_color_theme("./color_themes/NightTrain.json")

login_frame = LoginFrame(master=app)

login_frame.pack(anchor=CENTER,
                 pady=40)

info_frame = InfoFrame(master=app)
profile_frame = ProfileFrame(master=app)


login_frame.login_button.bind("<Button-1>", login)
info_frame.logout_label.bind("<Button-1>",  logout)



app.mainloop()