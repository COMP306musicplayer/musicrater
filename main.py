from customtkinter import *
from frames.loginFrame import LoginFrame
from frames.infoFrame import InfoFrame
from frames.profileFrame import ProfileFrame
from frames.albumFramesPage import AlbumFramesPage
from frames.albumFrame import AlbumFrame
from frames.songFrame import SongFrame



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

class AppFrame(CTk):

    def __init__(self):
        super().__init__()
        self.geometry("770x750")
        set_default_color_theme("./color_themes/NightTrain.json")

        self.db_connection = self.connect_to_db()
        self.db_cursor = self.db_connection.cursor(buffered=True)
        self.db_cursor.execute("USE ratingApp")

        self.login_frame = LoginFrame(master=self)
        self.info_frame = InfoFrame(master=self)
        self.profile_frame = ProfileFrame(master=self)
        self.albums_frame = AlbumFramesPage(master=self, kind="albums", array=self.get_album_names(), app_frame=self)
        self.genres_frame = AlbumFramesPage(master=self, kind="genres", array=self.get_album_genres(), app_frame=self)
        self.playlists_frame = AlbumFramesPage(master=self, kind="playlists", array=self.get_album_names(), app_frame=self)
        self.song_frame = SongFrame(master=self, song_names=[], kind="")

        self.setup_bindings()

        self.login_frame.pack(anchor=CENTER, pady=40)

    def connect_to_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234", 
            auth_plugin='mysql_native_password'
        )

    def get_album_names(self):
        query_album_names = "SELECT album_title FROM ALBUMS"
        self.db_cursor.execute(query_album_names)
        album_names_tuples = self.db_cursor.fetchall()
        return [name[0] for name in album_names_tuples]

    def get_album_genres(self):
        query_album_genres = "SELECT DISTINCT album_genre FROM ALBUMS"
        self.db_cursor.execute(query_album_genres)
        album_genres_tuples = self.db_cursor.fetchall()
        return [genre[0] for genre in album_genres_tuples]

    def login(self, event):
        self.geometry("1620x620")
        self.login_frame.pack_forget()
        self.info_frame.pack(side="left")
        self.albums_frame.pack(side="right", fill="both", expand=True)

    def logout(self, event):
        self.geometry("770x750")
        self.profile_frame.pack_forget()
        self.info_frame.pack_forget()
        self.login_frame.pack()

    def albums(self, event):
        self.profile_frame.pack_forget()
        self.genres_frame.pack_forget()
        self.playlists_frame.pack_forget()
        self.song_frame.pack_forget()
        self.albums_frame.pack(side="right", fill="both", expand=True)

    def profile(self, event):
        self.albums_frame.pack_forget()
        self.genres_frame.pack_forget()
        self.playlists_frame.pack_forget()
        self.song_frame.pack_forget()
        self.profile_frame.pack(side="right", fill="both", expand=True)

    def genres(self, event):
        self.albums_frame.pack_forget()
        self.profile_frame.pack_forget()
        self.playlists_frame.pack_forget()
        self.song_frame.pack_forget()
        self.genres_frame.pack(side="right", fill="both", expand=True)

    def playlists(self, event):
        self.albums_frame.pack_forget()
        self.genres_frame.pack_forget()
        self.profile_frame.pack_forget()
        self.song_frame.pack_forget()
        self.playlists_frame.pack(side="right", fill="both", expand=True)

    def setup_bindings(self):
        self.login_frame.login_button.bind("<Button-1>", self.login)
        self.info_frame.logout_label.bind("<Button-1>", self.logout)
        self.info_frame.view_profile.bind("<Button-1>", self.profile)
        self.info_frame.albums.bind("<Button-1>", self.albums)
        self.info_frame.genres.bind("<Button-1>", self.genres)
        self.info_frame.playlists.bind("<Button-1>", self.playlists)

if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()




                            
