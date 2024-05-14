from customtkinter import *

app = CTk()
app.geometry("770x750")

set_default_color_theme("./color_themes/NightTrain.json")

login_frame = CTkFrame(master=app,
                       height=580,
                       width=550)

login_frame.pack(anchor=CENTER,
                 pady=40)

login_frame.pack_propagate(False)

name_label = CTkLabel(master=login_frame,
                      text="MusicRater",
                      font=("Kanit", 20))

name_label.pack(side="top",
                pady=20)

username = CTkEntry(master=login_frame,
                    placeholder_text="username",
                    corner_radius=20)
username.pack(side="top",
              pady=10,
              padx=40,
              fill="x")

password = CTkEntry(master=login_frame,
                    placeholder_text="password",
                    corner_radius=20)
password.pack(side="top",
              pady=10,
              padx=40,
              fill="x")

password_again = CTkEntry(master=login_frame,
                    placeholder_text="enter password again",
                    corner_radius=20)



login_button = CTkButton(master=login_frame,
                         text="Login",
                         font=("Kanit", 18),
                         height=60,)
login_button.pack(side="top",
                  pady=50)

signup_button = CTkButton(master=login_frame,
                         text="Sign Up",
                         font=("Kanit", 18),
                         height=60)


sign_in_label = CTkLabel(master=login_frame,
                               text="Have no account? Sign up right now!",
                               font=("Kanit", 10))
sign_in_label.pack(side="right",
                         padx=10,
                         pady=5,
                         anchor="s")

login_label = CTkLabel(master=login_frame,
                               text="Already have an account? Login right now!",
                               font=("Kanit", 10))


def pack_login(event):

    #UNPACKS SIGNUP WIDGETS
    username.pack_forget()
    password.pack_forget()
    password_again.pack_forget()
    signup_button.pack_forget()
    login_label.pack_forget()

    #PACKS LOGIN WIDGETS 
    username.pack(side="top",
              pady=10,
              padx=40,
              fill="x")
    password.pack(side="top",
              pady=10,
              padx=40,
              fill="x")
    login_button.pack(side="top",
                  pady=50)
    sign_in_label.pack(side="right",
                         padx=10,
                         pady=5,
                         anchor="s")


def pack_signin(event):
    
    #UNPACKS LOGIN WIDGETS
    username.pack_forget()
    password.pack_forget()
    login_button.pack_forget()
    sign_in_label.pack_forget()

    #PACKS SIGNUP WIDGETS 
    username.pack(side="top",
              pady=10,
              padx=40,
              fill="x")
    password.pack(side="top",
              pady=10,
              padx=40,
              fill="x")
    password_again.pack(side="top",
              pady=10,
              padx=40,
              fill="x")
    signup_button.pack(side="top",
                  pady=50)
    login_label.pack(side="right",
                         padx=10,
                         pady=5,
                         anchor="s")


login_label.bind("<Button>", pack_login)    
sign_in_label.bind("<Button>", pack_signin)





app.mainloop()