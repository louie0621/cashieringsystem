from tkinter import *

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen = f"{screen_width}{'x'}{screen_height}"
window.geometry(screen)
window.configure(bg = "#b6c0ff")

bgphoto = PhotoImage(file = 'icon/bg.png')
bglbl = Label(window,image=bgphoto)
bglbl.pack()
bglbl.place(x=0,y=0)

#login
logincanvas = Canvas(
    bg = "#46caf2",
    width = 350,
    height = 390,
    bd = 5,
    relief = "groove"
)
logincanvas.pack()
logincanvas.place(x=500,y=150)


lbladmin = Label(window,
    text = "Admin",
    fg = "black",
    bg = "#46caf2",
    font = ('Times',35)
)
lbladmin.pack()
lbladmin.place(x=610,y=160)

#username
usrlbl = Label(window, text = "Username", font=('Times',25), bg="#46caf2", fg="black")
usrlbl.pack()
logincanvas.create_window(100, 110,window=usrlbl)
usrentry = Entry(window, font=('Times',20), relief="flat")
usrentry.pack()
logincanvas.create_window(180,150, window=usrentry)

#password
passlbl = Label(window, text="Password", font=('Times',25), bg="#46caf2",fg= "black")
passlbl.pack()
logincanvas.create_window(100,200,window=passlbl)
passentry = Entry(window, font=('Times',20), relief="flat", show="*")
passentry.pack(ipady=3)
logincanvas.create_window(180,240,window=passentry)


#login btn
login_btn = PhotoImage(file='icon/loginkey.png')
submit_btn = Button(window,
                    image=login_btn,
                    borderwidth=0 ,
                    bg="#46caf2",
                    activebackground = "#46caf2",
                    relief="groove",
                    cursor = "arrow")
submit_btn.pack()
logincanvas.create_window(190,325, window=submit_btn)


#window.config(cursor="none")
#window.overrideredirect(1)
window.mainloop()