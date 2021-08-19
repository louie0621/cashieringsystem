import tkinter as tk

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen = f"{screen_width}{'x'}{screen_height}"
window.geometry(screen)
window.configure(bg = "#b6c0ff")

#login
logincanvas = tk.Canvas(
    bg = "#9fa6ce",
    width = 350,
    height = 450,
    bd = 5
)
logincanvas.pack()
logincanvas.place(x=500,y=150)

lbladminfont = window.option_add('*font','Times 35')
lbladmin = tk.Label(
    lbladminfont,
    text = "Admin",
    fg = "white",
    bg = "#9fa6ce"
)
lbladmin.pack()
lbladmin.place(x=610,y=160)

login_btn = PhotoImage(file='icon/loginkey.png')
img_label = Label(image=login_btn)

window.config(cursor="none")
window.overrideredirect(1)
window.mainloop()
