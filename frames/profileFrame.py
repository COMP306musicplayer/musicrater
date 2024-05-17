import customtkinter as ctk
from PIL import Image, ImageTk

class ProfileFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(fg_color="#20232A", corner_radius=0)
        
        # Outer frame
        self.outer_frame = ctk.CTkFrame(master=self, fg_color="transparent", height=200)
        self.outer_frame.pack(pady=(20, 20), padx=20, fill='x')
        
        # Image frame
        self.image_frame = ctk.CTkFrame(master=self.outer_frame, fg_color="transparent", width=200)
        self.image_frame.pack(side='left', padx=10, fill='y')
        
        # Profile photo
        profile_photo = Image.open("./icons/user_icon.png")
        profile_photo = profile_photo.resize((200, 200))
        profile_photo_image = ImageTk.PhotoImage(profile_photo)
        self.profile_photo_label = ctk.CTkLabel(master=self.image_frame, image=profile_photo_image, fg_color="transparent")
        self.profile_photo_label.image = profile_photo_image  # Keep a reference to avoid garbage collection
        self.profile_photo_label.pack(pady=10)
        
        # Text frame
        self.text_frame = ctk.CTkFrame(master=self.outer_frame, fg_color="transparent")
        self.text_frame.pack(side='left', fill='both', expand=True, padx=(10, 20), pady=(40, 0))
        
        # Profile label frame
        self.profile_label_frame = ctk.CTkFrame(master=self.text_frame, fg_color="transparent")
        self.profile_label_frame.pack(fill='x')
        self.profile_label = ctk.CTkLabel(master=self.profile_label_frame, text="Profile", font=("Kanit", 14), fg_color="transparent", text_color="white")
        self.profile_label.pack(side='left', anchor='w')
        
        # Username frame
        self.username_frame = ctk.CTkFrame(master=self.text_frame, fg_color="transparent")
        self.username_frame.pack(fill='x')
        self.username_label = ctk.CTkLabel(master=self.username_frame, text="Username", font=("Kanit", 60), fg_color="transparent", text_color="white")
        self.username_label.pack(side='left', anchor='w')
        
        # Details frame
        self.details_frame = ctk.CTkFrame(master=self.text_frame, fg_color="transparent")
        self.details_frame.pack(fill='x')
        self.details_label = ctk.CTkLabel(master=self.details_frame, text="36 Playlists • 10 Followers • 22 Following", font=("Kanit", 12), fg_color="transparent", text_color="white")
        self.details_label.pack(side='left', anchor='w')
        
        # Popular frame
        self.popular_frame = ctk.CTkFrame(master=self, fg_color="#333646", width=500, height=200, border_color="white", border_width=1)
        self.popular_frame.pack(side="left", fill="both", expand=True, padx=20, pady=40, anchor='w')
        self.popular_label = ctk.CTkLabel(master=self.popular_frame, text="Most Popular Playlists", font=("Kanit", 18), fg_color="transparent")
        self.popular_label.pack(pady=(20, 10))
        
        # Tracks frame
        self.tracks_frame = ctk.CTkFrame(master=self, fg_color="#333646", width=500, height=200, border_color="white", border_width=1)
        self.tracks_frame.pack(side="left", fill="both", expand=True, padx=20, pady=40, anchor='w')
        self.tracks_label = ctk.CTkLabel(master=self.tracks_frame, text="Most Listened Tracks", font=("Kanit", 18), fg_color="transparent")
        self.tracks_label.pack(pady=(20, 10))
'''
# Usage example
root = ctk.CTk()
profile_page = ctk.CTkFrame(root)
profile_page.pack(fill="both", expand=True)

content_frame = ProfileFrame(master=profile_page)
content_frame.pack(side="right", fill="both", expand=True)

root.mainloop()
'''