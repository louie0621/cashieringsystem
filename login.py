from tkinter import *

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen = f"{screen_width}{'x'}{screen_height}"
window.geometry(screen)
window.configure(bg = "#b6c0ff")

#login
logincanvas = Canvas(
    bg = "#9fa6ce",
    width = 350,
    height = 390,asd
    bd = 5
)
logincanvas.pack()
logincanvas.place(x=500,y=150)


lbladmin = Label(window,
    text = "Admin",
    fg = "white",
    bg = "#9fa6ce",
    font = ('Times',35)
)
lbladmin.pack()
lbladmin.place(x=610,y=160)

#username
usrlbl = Label(window, text = "Username", font=('Times',25), bg="#9fa6ce", fg="white")
usrlbl.pack()
logincanvas.create_window(100, 110,window=usrlbl)
usrentry = Entry(window, font=('Times',20))
usrentry.pack()
logincanvas.create_window(180,150, window=usrentry)

#password
passlbl = Label(window, text="Password", font=('Times',25), bg="#9fa6ce",fg= "white")
passlbl.pack()
logincanvas.create_window(100,200,window=passlbl)
passentry = Entry(window, font=('Times',20))
passentry.pack(ipady=3)
logincanvas.create_window(180,240,window=passentry)


#login btn
login_btn = PhotoImage(file='icon/loginkey.png')
submit_btn = Button(window, image=login_btn, borderwidth=0 , bg="#9fa6ce")
submit_btn.pack()
logincanvas.create_window(190,325, window=submit_btn)


window.config(cursor="")
window.overrideredirect(1)
window.mainloop()