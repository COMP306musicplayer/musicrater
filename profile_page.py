from customtkinter import *
from PIL import Image, ImageTk

profile_page = CTk()
profile_page.geometry("1320x620") 
set_default_color_theme("./color_themes/NightTrain.json") 


infoframe = CTkFrame(master=profile_page,
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


main_menu_icon_image = Image.open("main_menu_icon.png") 
main_menu_icon_image = main_menu_icon_image.resize((36, 36))
main_menu_icon_photoimage = ImageTk.PhotoImage(main_menu_icon_image)
main_menu_button = CTkButton(master=infoframe,
                             text="Main Menu",
                             font=("Kanit", 15),
                             image=main_menu_icon_photoimage,
                             compound="left",
                             anchor="w")
main_menu_button.pack(side="top",
                      padx=15,
                      pady=5,
                      fill="x",
                      anchor="w")


genres_icon_image = Image.open("genres_icon.png")  
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


albums_icon_image = Image.open("albums_icon.png")  
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


playlists_icon_image = Image.open("playlists_icon.png")  
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


content_frame = CTkFrame(master=profile_page, fg_color="#20232A", corner_radius=0)
content_frame.pack(side="right", fill="both", expand=True)


outer_frame = CTkFrame(master=content_frame, fg_color="transparent", height=200)
outer_frame.pack(pady=(20, 20), padx=20, fill='x') 


image_frame = CTkFrame(master=outer_frame, fg_color="transparent", width=200)
image_frame.pack(side='left', padx=10, fill='y')  


profile_photo = Image.open("user_icon.png") 
profile_photo = profile_photo.resize((200, 200))
profile_photo_image = ImageTk.PhotoImage(profile_photo)
profile_photo_label = CTkLabel(master=image_frame, image=profile_photo_image, fg_color="transparent")
profile_photo_label.image = profile_photo_image  
profile_photo_label.pack(pady=10) 


text_frame = CTkFrame(master=outer_frame, fg_color="transparent")
text_frame.pack(side='left', fill='both', expand=True, padx=(10, 20), pady=(40,0)) 


profile_label_frame = CTkFrame(master=text_frame, fg_color="transparent")
profile_label_frame.pack(fill='x')
profile_label = CTkLabel(master=profile_label_frame, text="Profile", font=("Kanit", 14), fg_color="transparent", text_color="white")
profile_label.pack(side='left', anchor='w')  


username_frame = CTkFrame(master=text_frame, fg_color="transparent")
username_frame.pack(fill='x')
username_label = CTkLabel(master=username_frame, text="Username", font=("Kanit", 60), fg_color="transparent", text_color="white")
username_label.pack(side='left', anchor='w')  


details_frame = CTkFrame(master=text_frame, fg_color="transparent")
details_frame.pack(fill='x')
details_label = CTkLabel(master=details_frame, text="36 Playlists • 10 Followers • 22 Following", font=("Kanit", 12), fg_color="transparent", text_color="white")
details_label.pack(side='left', anchor='w')  



popular_frame = CTkFrame(master=content_frame, fg_color="#333646", width=500, height=200, border_color="white", border_width=1)
popular_frame.pack(side="left", fill="both", expand=True, padx=20, pady=40, anchor='w')
popular_label = CTkLabel(master=popular_frame, text="Most Popular Playlists", font=("Kanit", 18), fg_color="transparent")
popular_label.pack(pady=(20, 10))  
for i in range(6):
    playlist_label = CTkLabel(master=popular_frame, text=f"Playlist {i+1}", fg_color="transparent", text_color="white")
    playlist_label.pack(anchor="w", padx=20)  


tracks_frame = CTkFrame(master=content_frame, fg_color="#333646", width=500, height=200, border_color="white", border_width=1)
tracks_frame.pack(side="left", fill="both", expand=True, padx=20, pady=40, anchor='w')
tracks_label = CTkLabel(master=tracks_frame, text="Most Listened Tracks", font=("Kanit", 18), fg_color="transparent")
tracks_label.pack(pady=(20, 10))
for i in range(6):
    track_label = CTkLabel(master=tracks_frame, text=f"Sound {i+1}", fg_color="transparent", text_color="white")
    track_label.pack(anchor="w", padx=20) 

profile_page.mainloop()
