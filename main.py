from customtkinter import *
from frames.loginFrame import LoginFrame

app = CTk()
app.geometry("770x750")

set_default_color_theme("./color_themes/NightTrain.json")

login_frame = LoginFrame(master=app)

login_frame.pack(anchor=CENTER,
                 pady=40)







app.mainloop()