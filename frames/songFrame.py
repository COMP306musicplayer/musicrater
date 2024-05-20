import customtkinter as ctk

from infoFrame import InfoFrame

app = ctk.CTk()
app.geometry("1320x620")

info_frame = InfoFrame(master=app)
info_frame.pack(side="left")

song_frame = ctk.CTkFrame(master=app)
song_frame.pack(expand="True",
                fill="both")
song_frame.pack_propagate(False)

upper_frame = ctk.CTkFrame(master=song_frame,
                           height=100)
upper_frame.pack(side="top",
                 fill="x",)
upper_frame.pack_propagate(False)

header_label = ctk.CTkLabel(master=upper_frame,
                            text="ALBUM_OR_GENRE_NAME",
                            font=("Kanit", 18))

header_label.pack(side="top",
                  anchor="nw",
                  padx=10)

details_label = ctk.CTkLabel(master=upper_frame,
                             text="Various Artists * 37 songs * 4.3 rating",
                             font=("Kanit", 10))
details_label.pack(side="top",
                   anchor="nw",
                   padx=10)

search_by_name = ctk.CTkEntry(master=upper_frame,
                              placeholder_text="Search by name")
search_by_name.pack(side="left",
                    anchor="s",
                    padx=10,
                    pady=10)

search_btn = ctk.CTkButton(master=upper_frame,
                           text="Search",
                           font=("Kanit", 12),
                           width=50)
search_btn.pack(side="left",
                anchor="s",
                pady=10)

scroll_songs = ctk.CTkScrollableFrame(master=song_frame)
scroll_songs.pack(expand=True,
                  fill="both")

scroll_songs.columnconfigure(0, weight=1)

song_box = ctk.CTkFrame(master=scroll_songs,
                        height=70,
                        fg_color="#234234")

song_box.grid(row=0, column=0,
              sticky="we")

song_box = ctk.CTkFrame(master=scroll_songs,
                        height=70,
                        fg_color="#123789")

song_box.grid(row=1, column=0,
              sticky="we")

song_box = ctk.CTkFrame(master=scroll_songs,
                        height=70,
                        fg_color="#234789")

song_box.grid(row=2, column=0,
              sticky="we")

song_box = ctk.CTkFrame(master=scroll_songs,
                        height=70,
                        fg_color="#234546")

song_box.grid(row=3, column=0,
              sticky="we")

app.mainloop()