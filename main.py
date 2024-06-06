from customtkinter import *
from frames.loginFrame import LoginFrame
from frames.infoFrame import InfoFrame
from frames.profileFrame import ProfileFrame
from frames.albumFramesPage import AlbumsPagesFrame



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

def login(event):
    app.geometry("1320x620")
    login_frame.pack_forget()
    info_frame.pack(side="left")
    #profile_frame.pack(side="right", fill="both", expand=True)
    albums_frame.pack(side="right", fill="both", expand=True)


def logout(event):
    app.geometry("770x750")
    profile_frame.pack_forget()
    info_frame.pack_forget()
    login_frame.pack()

def albums(event):
    profile_frame.pack_forget()
    genres_frame.pack_forget()
    playlists_frame.pack_forget()
    albums_frame.pack(side="right", fill="both", expand=True)

def profile(event):
    albums_frame.pack_forget()
    genres_frame.pack_forget()
    playlists_frame.pack_forget()
    profile_frame.pack(side="right", fill="both", expand=True)

def genres(event):
    albums_frame.pack_forget()
    profile_frame.pack_forget()
    playlists_frame.pack_forget()
    genres_frame.pack(side="right", fill="both", expand=True)


def playlists(event):
    albums_frame.pack_forget()
    genres_frame.pack_forget()
    profile_frame.pack_forget()
    playlists_frame.pack(side="right", fill="both", expand=True)



app = CTk()
app.geometry("770x750")

set_default_color_theme("./color_themes/NightTrain.json")

login_frame = LoginFrame(master=app)

login_frame.pack(anchor=CENTER,
                 pady=40)



# Query to get all album names
query_album_names = "SELECT album_title FROM ALBUMS"
db_cursor.execute(query_album_names)
album_names_tuples = db_cursor.fetchall()

# Extract album names from tuples
album_names = [name[0] for name in album_names_tuples]


# Query to get all unique album genres
query_album_genres = "SELECT DISTINCT album_genre FROM ALBUMS"
db_cursor.execute(query_album_genres)
album_genres_tuples = db_cursor.fetchall()

# Extract album genres from tuples
album_genres = [genre[0] for genre in album_genres_tuples]

info_frame = InfoFrame(master=app)
profile_frame = ProfileFrame(master=app)
albums_frame = AlbumsPagesFrame(master=app,
                                kind="Albums",
                                array=album_names)
genres_frame = AlbumsPagesFrame(master=app,
                                kind="genres",
                                array=album_genres)
playlists_frame = AlbumsPagesFrame(master=app,
                                   kind="playlists",
                                   array=album_names)



login_frame.login_button.bind("<Button-1>", login)
info_frame.logout_label.bind("<Button-1>",  logout)
info_frame.view_profile.bind("<Button-1>", profile)
info_frame.albums.bind("<Button-1>", albums)
info_frame.genres.bind("<Button-1>", genres)
info_frame.playlists.bind("<Button-1>", playlists)






app.mainloop()