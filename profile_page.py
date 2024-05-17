from customtkinter import *
from profileFrame import ProfileFrame
from infoFrame import InfoFrame
from PIL import Image, ImageTk

profile_page = CTk()
profile_page.geometry("1320x620") 
set_default_color_theme("./color_themes/NightTrain.json") 


infoframe = InfoFrame(master=profile_page)
infoframe.pack(side="left")


content_frame = ProfileFrame(master=profile_page)
content_frame.pack(side="right", fill="both", expand=True)


for i in range(6):
    playlist_label = CTkLabel(master=content_frame.popular_frame, text=f"Playlist {i+1}", fg_color="transparent", text_color="white")
    playlist_label.pack(anchor="w", padx=20)  



for i in range(6):
    track_label = CTkLabel(master=content_frame.tracks_frame, text=f"Sound {i+1}", fg_color="transparent", text_color="white")
    track_label.pack(anchor="w", padx=20) 

profile_page.mainloop()
