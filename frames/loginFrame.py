import customtkinter as ctk
from tkinter import CENTER

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(height=580, width=550)
        self.pack(anchor=CENTER, pady=40)
        self.pack_propagate(False)
        
        self.name_label = ctk.CTkLabel(master=self, text="MusicRater", font=("Kanit", 20))
        self.name_label.pack(side="top", pady=20)
        
        self.username = ctk.CTkEntry(master=self, placeholder_text="username", corner_radius=20)
        self.username.pack(side="top", pady=10, padx=40, fill="x")
        
        self.password = ctk.CTkEntry(master=self, placeholder_text="password", corner_radius=20)
        self.password.pack(side="top", pady=10, padx=40, fill="x")
        
        self.password_again = ctk.CTkEntry(master=self, placeholder_text="enter password again", corner_radius=20)
        
        self.login_button = ctk.CTkButton(master=self, text="Login", font=("Kanit", 18), height=60)
        self.login_button.pack(side="top", pady=50)
        
        self.signup_button = ctk.CTkButton(master=self, text="Sign Up", font=("Kanit", 18), height=60)
        
        self.sign_in_label = ctk.CTkLabel(master=self, text="Have no account? Sign up right now!", font=("Kanit", 10))
        self.sign_in_label.pack(side="right", padx=10, pady=5, anchor="s")
        
        self.login_label = ctk.CTkLabel(master=self, text="Already have an account? Login right now!", font=("Kanit", 10))
        
        self.login_label.bind("<Button-1>", self.pack_login)
        self.sign_in_label.bind("<Button-1>", self.pack_signin)
        
    def pack_login(self, event):
        # Unpack sign-up widgets
        self.password_again.pack_forget()
        self.signup_button.pack_forget()
        self.login_label.pack_forget()

        # Pack login widgets
        self.username.pack(side="top", pady=10, padx=40, fill="x")
        self.password.pack(side="top", pady=10, padx=40, fill="x")
        self.login_button.pack(side="top", pady=50)
        self.sign_in_label.pack(side="right", padx=10, pady=5, anchor="s")
    
    def pack_signin(self, event):
        # Unpack login widgets
        self.login_button.pack_forget()
        self.sign_in_label.pack_forget()
        
        # Pack sign-up widgets
        self.username.pack(side="top", pady=10, padx=40, fill="x")
        self.password.pack(side="top", pady=10, padx=40, fill="x")
        self.password_again.pack(side="top", pady=10, padx=40, fill="x")
        self.signup_button.pack(side="top", pady=50)
        self.login_label.pack(side="right", padx=10, pady=5, anchor="s")
'''
# Usage example
root = ctk.CTk()
app = ctk.CTkFrame(root)
app.pack(fill="both", expand=True)

login_frame = LoginFrame(master=app)
login_frame.pack()

root.mainloop()
'''