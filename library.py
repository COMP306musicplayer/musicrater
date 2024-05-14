from customtkinter import *

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

view_profile = CTkButton(master=infoframe,
                    text="View Profile",
                    font=("Kanit", 15),
                    anchor="w")
view_profile.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

genres = CTkButton(master=infoframe,
                    text="Genres",
                    font=("Kanit", 15),
                    anchor="w")
genres.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

albums = CTkButton(master=infoframe,
                    text="Albums",
                    font=("Kanit", 15),
                    anchor="w")
albums.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")

playlists = CTkButton(master=infoframe,
                    text="Playlists",
                    font=("Kanit", 15),
                    anchor="w")
playlists.pack(side="top",
                  padx=15,
                  pady=5,
                  fill="x",
                  anchor="w")



logout_label = CTkLabel(master= infoframe,
                        text="Log Out",
                        font=("Kanit", 13))
logout_label.pack(side="left",
                  padx=10,
                  pady=5,
                  anchor="s")

settings_label = CTkLabel(master= infoframe,
                        text="Settings",
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

musicframe.rowconfigure(0, weight=1)
musicframe.rowconfigure(1, weight=1)
musicframe.rowconfigure(2, weight=1)

album_frame = CTkFrame(master=musicframe,
                       fg_color="#000000",
                       height=300,
                       width=300)
album_frame.place(x=10,
                  y=20)





library.mainloop()
