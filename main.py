from customtkinter import *
from frames.loginFrame import LoginFrame
from frames.infoFrame import InfoFrame
from frames.profileFrame import ProfileFrame

def login(event):
    print("hey")
    app.geometry("1320x620")
    login_frame.pack_forget()
    info_frame.pack(side="left")
    profile_frame.pack(side="right", fill="both", expand=True)

def logout(event):
    print("wassup")
    app.geometry("770x750")
    profile_frame.pack_forget()
    info_frame.pack_forget()
    login_frame.pack()



app = CTk()
app.geometry("770x750")

set_default_color_theme("./color_themes/NightTrain.json")

login_frame = LoginFrame(master=app)

login_frame.pack(anchor=CENTER,
                 pady=40)

info_frame = InfoFrame(master=app)
profile_frame = ProfileFrame(master=app)


login_frame.login_button.bind("<Button-1>", login)
info_frame.logout_label.bind("<Button-1>",  logout)



app.mainloop()