import customtkinter as ctk

class AlbumFrame(ctk.CTkFrame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)
        
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

    def returntext(self, event):
         print(self.text)
         return self.text