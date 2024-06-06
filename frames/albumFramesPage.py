import customtkinter as ctk
from frames.albumFrame import AlbumFrame

class AlbumsPagesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, kind, array, **kwargs):  # Corrected from _init_
        super().__init__(master, **kwargs)  # Corrected from _init_
        self.kind = kind
        self.array = array
        self.create_widgets()
    
    

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=0)  # Title row
        self.grid_rowconfigure(1, weight=1)  # Content rows
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.title_label = ctk.CTkLabel(master=self, text=f"{self.kind} Page", font=("Kanit", 20))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)

        for i in range(len(self.array)): 
                album_frame = AlbumFrame(master=self, text=f"{self.array[i]}")
                row= i/3

                album_frame.grid(row=int(row), column=(i % 3))
        
        self.bind_class(AlbumFrame, func=album_frame.returntext)
