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

def populate_table(db_connection, db_cursor, insert_query, file_path):
    
    with open(file_path, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        csv_data_list = list(reader)
        for row in csv_data_list[1:]:
            row = tuple(map(lambda x: None if x == "" else x, row[0].split(',')))
            db_cursor.execute(insert_query, row)
        
    db_connection.commit()

insert_artists = (
    """INSERT INTO ARTISTS (artist_id, artist_fname, artist_mname, artist_lname, artist_genre) VALUES (%s, %s, %s, %s, %s) """
    
)

populate_table(db_connection, db_cursor, insert_artists, "ARTISTS.csv")
  




### Step 2: Insert Albums
##Each album should be linked to one of the artists. Since there are 80 albums and 50 artists, some artists will be linked to multiple albums.


# Step 2: Insert Albums


insert_albums = (
    """INSERT INTO ALBUMS (album_id, album_title, album_releaseDate, maker_id, album_genre)  VALUES (%s, %s, %s, %s, %s) """
    
)

populate_table(db_connection, db_cursor, insert_albums, "ALBUMS.csv")


### Step 3: Insert Songs
##Now, populate the SONGS table with 300 songs. Each song should be linked to one album and one artist. Here, singer_id can be either the same as the album's maker_id or another artist.





insert_songs = (
    """INSERT INTO SONGS (song_id, song_title, song_duration, song_rating, singer_id, inalbum_id, song_genre)  VALUES (%s, %s, %s, %s, %s,%s,%s) """
    
)

populate_table(db_connection, db_cursor, insert_songs, "SONGS.csv")
