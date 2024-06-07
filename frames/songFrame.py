import customtkinter as ctk

class SongBox(ctk.CTkFrame):
    def __init__(self, master, song_name, **kwargs):
        super().__init__(master, **kwargs)
        
        self.pack_propagate(False)
        self.configure(fg_color="#000000")
        self.song_name = song_name
        self.master = master
        
        # Song name label
        self.song_label = ctk.CTkLabel(master=self, text=song_name)
        self.song_label.pack(side="left", padx=10, pady=10)

        # Rating ComboBox
        self.rating_combobox = ctk.CTkComboBox(master=self, values=[str(i) for i in range(1, 6)])
        self.rating_combobox.pack(side="right", padx=10, pady=10)
        
        # Rating label
        self.rating_label = ctk.CTkLabel(master=self, text="Rating:")
        self.rating_label.pack(side="right", padx=10, pady=10)
        



class SongFrame(ctk.CTkFrame):
    def __init__(self, master, song_names, kind,**kwargs):
        super().__init__(master, **kwargs)
        
        self.pack_propagate(False)
        self.song_names = song_names
        self.master = master
        self.kind = kind
        self.create_widgets()

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        # Upper Frame
        self.upper_frame = ctk.CTkFrame(master=self, height=100)
        self.upper_frame.pack(side="top", fill="x")
        self.upper_frame.pack_propagate(False)
        
        self.header_label = ctk.CTkLabel(master=self.upper_frame,
                                         text=f"{self.kind}",
                                         font=("Kanit", 18))
        self.header_label.pack(side="top", anchor="nw", padx=10)

        self.details_label = ctk.CTkLabel(master=self.upper_frame,
                                          text=f"{len(self.song_names)} songs",
                                          font=("Kanit", 10))
        self.details_label.pack(side="top", anchor="nw", padx=10)

        self.search_by_name = ctk.CTkEntry(master=self.upper_frame,
                                           placeholder_text="Search by name")
        self.search_by_name.pack(side="left", anchor="s", padx=10, pady=10)

        self.search_btn = ctk.CTkButton(master=self.upper_frame,
                                        text="Search",
                                        font=("Kanit", 12),
                                        width=50)
        self.search_btn.pack(side="left", anchor="s", pady=10)

        # Scrollable Frame for Songs
        self.scroll_songs = ctk.CTkScrollableFrame(master=self)
        self.scroll_songs.pack(expand=True, fill="both")
        self.scroll_songs.columnconfigure(0, weight=1)

        # Add Song Boxes
        for i, song_name in enumerate(self.song_names):
            song_box = SongBox(master=self.scroll_songs,
                               song_name=song_name,
                               height=70,
                               fg_color="#e0e0e0")
            song_box.grid(row=i, column=0, sticky="we")

if __name__ == "__main__":
    app = ctk.CTk()
    song_frame = SongFrame(master=app, song_names=[], kind="")
    song_frame.pack(expand=True, fill="both")
    app.mainloop()
