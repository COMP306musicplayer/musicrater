import customtkinter as ctk
from PIL import Image, ImageTk

class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(height=620, width=280, fg_color="#090B1A", corner_radius=0)
        self.pack_propagate(False)
        
        # Username label
        self.username = ctk.CTkLabel(master=self, text="username", font=("Kanit", 25))
        self.username.pack(side="top", padx=10, pady=5, anchor="w")
        
        # View Profile button
        profile_icon_image = Image.open("./icons/profile_icon.png")
        profile_icon_image = profile_icon_image.resize((36, 36))
        profile_icon_photoimage = ImageTk.PhotoImage(profile_icon_image)
        self.view_profile = ctk.CTkButton(master=self, text="View Profile", font=("Kanit", 15), image=profile_icon_photoimage, compound="left", anchor="w")
        self.view_profile.pack(side="top", padx=15, pady=5, fill="x", anchor="w")
        
        # Genres button
        genres_icon_image = Image.open("./icons/genres_icon.png")
        genres_icon_image = genres_icon_image.resize((38, 38))
        genres_icon_photoimage = ImageTk.PhotoImage(genres_icon_image)
        self.genres = ctk.CTkButton(master=self, text="Genres", font=("Kanit", 15), image=genres_icon_photoimage, compound="left", anchor="w")
        self.genres.pack(side="top", padx=15, pady=5, fill="x", anchor="w")
        
        # Albums button
        albums_icon_image = Image.open("./icons/albums_icon.png")
        albums_icon_image = albums_icon_image.resize((36, 36))
        albums_icon_photoimage = ImageTk.PhotoImage(albums_icon_image)
        self.albums = ctk.CTkButton(master=self, text="Albums", font=("Kanit", 15), image=albums_icon_photoimage, compound="left", anchor="w")
        self.albums.pack(side="top", padx=15, pady=5, fill="x", anchor="w")
        
        # Playlists button
        playlists_icon_image = Image.open("./icons/playlists_icon.png")
        playlists_icon_image = playlists_icon_image.resize((36, 36))
        playlists_icon_photoimage = ImageTk.PhotoImage(playlists_icon_image)
        self.playlists = ctk.CTkButton(master=self, text="Playlists", font=("Kanit", 15), image=playlists_icon_photoimage, compound="left", anchor="w")
        self.playlists.pack(side="top", padx=15, pady=5, fill="x", anchor="w")
        
        # Logout label
        logout_icon_image = Image.open("./icons/logout_icon.png")
        logout_icon_image = logout_icon_image.resize((36, 36))
        logout_icon_photoimage = ImageTk.PhotoImage(logout_icon_image)
        self.logout_label = ctk.CTkLabel(master=self, text="", image=logout_icon_photoimage, font=("Kanit", 13))
        self.logout_label.pack(side="left", padx=10, pady=5, anchor="s")
        
        # Settings label
        settings_icon_image = Image.open("./icons/settings_icon.png")
        settings_icon_image = settings_icon_image.resize((36, 36))
        settings_icon_photoimage = ImageTk.PhotoImage(settings_icon_image)
        self.settings_label = ctk.CTkLabel(master=self, text="", image=settings_icon_photoimage, font=("Kanit", 13))
        self.settings_label.pack(side="bottom", padx=2, pady=5, anchor="w")
'''
# Usage example
root = ctk.CTk()
library = ctk.CTkFrame(root)
library.pack(fill="both", expand=True)

infoframe = InfoFrame(master=library)
infoframe.pack(side="left")

root.mainloop()
'''