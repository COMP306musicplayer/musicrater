from customtkinter import *
from albumFrame import AlbumFrame
from PIL import Image, ImageTk

library = CTk()
library.geometry("1320x620")

set_default_color_theme("./color_themes/NightTrain.json")

infoframe = CTkFrame(master=library,
                    height=620,
                    width=280,
                    fg_color="#090B1A",
                    corner_radius=0)

infoframe.pack(side="left")
infoframe.pack_propagate(False)

username = CTkLabel(master=infoframe,
                    text="username",
                    font=("Kanit", 25))
username.pack(side="top",
              padx=10,
              pady=5,
              anchor="w")

profile_icon_image = Image.open("./icons/profile_icon.png")
profile_icon_image = profile_icon_image.resize((36, 36)) 
profile_icon_photoimage = ImageTk.PhotoImage(profile_icon_image)
view_profile = CTkButton(master=infoframe,
                         text="View Profile",
                         font=("Kanit", 15),
                         image=profile_icon_photoimage,
                         compound="left",
                         anchor="w")
view_profile.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

genres_icon_image = Image.open("./icons/genres_icon.png")
genres_icon_image = genres_icon_image.resize((38, 38)) 
genres_icon_photoimage = ImageTk.PhotoImage(genres_icon_image)
genres = CTkButton(master=infoframe,
                    text="Genres",
                    font=("Kanit", 15),
                    image=genres_icon_photoimage,
                    compound="left",
                    anchor="w")
genres.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

albums_icon_image = Image.open("./icons/albums_icon.png")
albums_icon_image = albums_icon_image.resize((36, 36)) 
albums_icon_photoimage = ImageTk.PhotoImage(albums_icon_image)
albums = CTkButton(master=infoframe,
                    text="Albums",
                    font=("Kanit", 15),
                    image=albums_icon_photoimage,
                    compound="left",
                    anchor="w")
albums.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

playlists_icon_image = Image.open("./icons/playlists_icon.png")
playlists_icon_image = playlists_icon_image.resize((36, 36)) 
playlists_icon_photoimage = ImageTk.PhotoImage(playlists_icon_image)
playlists = CTkButton(master=infoframe,
                    text="Playlists",
                    font=("Kanit", 15),
                    image=playlists_icon_photoimage,
                    compound="left",
                    anchor="w")
playlists.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")


logout_icon_image = Image.open("./icons/logout_icon.png")
logout_icon_image = logout_icon_image.resize((36, 36))
logout_icon_photoimage = ImageTk.PhotoImage(logout_icon_image)
logout_label = CTkLabel(master= infoframe,
                        text="",
                        image=logout_icon_photoimage,
                        font=("Kanit", 13))
logout_label.pack(side="left",
                  padx=10,
                  pady=5,
                  anchor="s")

settings_icon_image = Image.open("./icons/settings_icon.png")
settings_icon_image = settings_icon_image.resize((36, 36))
settings_icon_photoimage = ImageTk.PhotoImage(settings_icon_image)
settings_label = CTkLabel(master= infoframe,
                        text="",
                        image=settings_icon_photoimage,
                        font=("Kanit", 13))
settings_label.pack(side="bottom",
                  padx=2,
                  pady=5,
                  anchor="w")


musicframe = CTkScrollableFrame(master=library,
                                height=620,
                                width=1040,
                                corner_radius=0)
musicframe.pack(side="right")

musicframe.columnconfigure(0, weight=1)
musicframe.columnconfigure(1, weight=1)
musicframe.columnconfigure(2, weight=1)
musicframe.columnconfigure(3, weight=1)

#PUTTING DUMMY FRAMES SO COLUMNS PROTECT THEIR SIZES
#IF THERE IS NO DUMMY, FRAMES APPEAR IN THE MIDDLE WHEN LESS THAN 4 IN FIRST ROW
album_frame = CTkFrame(master=musicframe)
album_frame.grid(column=0, row=0)

album_frame = CTkFrame(master=musicframe)
album_frame.grid(column=1, row=0)

album_frame = CTkFrame(master=musicframe)
album_frame.grid(column=2, row=0)

album_frame = CTkFrame(master=musicframe)
album_frame.grid(column=3, row=0)

musicframe.rowconfigure(0, weight=1)
musicframe.rowconfigure(1, weight=1)
musicframe.rowconfigure(2, weight=1)


album_frame = AlbumFrame(master=musicframe, text="za")

album_frame.grid(column=0, row=0)

album_frame = AlbumFrame(master=musicframe, text="zazer")


album_frame.grid(column=1, row=0)







library.mainloop()
