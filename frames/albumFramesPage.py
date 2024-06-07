import customtkinter as ctk

def returntext(event, app_frame, self):
    app_frame.profile_frame.pack_forget()
    app_frame.albums_frame.pack_forget()
    app_frame.genres_frame.pack_forget()
    app_frame.playlists_frame.pack_forget()
    album_name = self.text

    # Query to get songs based on album name
    if (self.master.master.kind == "albums"):
        query = """
            SELECT S.song_title, S.song_duration, S.song_rating, A.album_title
            FROM SONGS S
            JOIN ALBUMS A ON S.inalbum_id = A.album_id
            WHERE A.album_title = %s
        """
    elif (self.master.master.kind == "genres"):
        query =  """
            SELECT song_title, song_duration, song_rating, song_genre
            FROM SONGS
            WHERE song_genre = %s
        """
    else:
        query = ""


    # Execute the query with parameter
    app_frame.db_cursor.execute(query, (album_name,))
    songs_by_album = app_frame.db_cursor.fetchall()
    app_frame.song_frame.song_names = songs_by_album
    app_frame.song_frame.kind =self.text
    app_frame.song_frame.create_widgets()
    app_frame.song_frame.pack(side="right",
                              fill="both",
                              expand=True)

class AlbumFrame(ctk.CTkFrame):
    def __init__(self, master, app_frame, text, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master
        self.app_frame = app_frame
        self.text = text
        self.configure(fg_color="#000000", height=350, width=290)
        self.pack_propagate(False)
        
        self.album_image = ctk.CTkLabel(master=self,
                                        fg_color="#ffffff",
                                        height=290,
                                        width=290)
        
        self.album_name = ctk.CTkLabel(master=self,
                                       text=text,
                                       font=("Kanit", 15))
        
        self.album_image.pack(side="top")
        self.album_name.pack(side="bottom")

        # Bind click events to the frame and its child widgets
        self.bind("<Button-1>", lambda event: returntext(event, self.app_frame, self))
        self.album_image.bind("<Button-1>", lambda event: returntext(event, self.app_frame, self))
        self.album_name.bind("<Button-1>", lambda event: returntext(event, self.app_frame, self))

class AlbumFramesPage(ctk.CTkScrollableFrame):
    def __init__(self, master, kind, array, app_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.array = array
        self.kind = kind
        self.app_frame = app_frame
        
        self.frame_container = ctk.CTkFrame(self)  # Create a container frame
        self.frame_container.pack(fill="both", expand=True)
        
        # Use grid in the container frame
        for i in range(len(self.array)): 
            album_frame = AlbumFrame(master=self.frame_container, app_frame=self.app_frame, text=f"{self.array[i]}")
            row = i // 4  # Integer division for row
            col = i % 4   # Modulus for column
            album_frame.grid(row=row, column=col, padx=5, pady=5)  # Use grid with padding

# Example usage
if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()

    # Create dummy frames for demonstration
    class DummyFrame(ctk.CTkFrame):
        def __init__(self, master, text, **kwargs):
            super().__init__(master, **kwargs)
            label = ctk.CTkLabel(self, text=text)
            label.pack()

    app = ctk.CTkFrame(root)
    app.profile_frame = DummyFrame(app, "Profile Frame")
    app.albums_frame = DummyFrame(app, "Albums Frame")
    app.genres_frame = DummyFrame(app, "Genres Frame")
    app.playlists_frame = DummyFrame(app, "Playlists Frame")
    app.song_frame = DummyFrame(app, "Song Frame")
    
    albums = ["Album 1", "Album 2", "Album 3", "Album 4", "Album 5", "Album 6"]
    albums_page = AlbumFramesPage(app, "albums", albums, app)
    albums_page.pack(expand=True, fill="both")

    app.pack(expand=True, fill="both")
    root.mainloop()
