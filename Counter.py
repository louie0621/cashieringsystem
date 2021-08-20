from tkinter import *

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen = f"{screen_width}{'x'}{screen_height}"
window.geometry(screen)
window.configure(bg = "#afb6bd")

sidewidth = screen_width * .25
sideframe = Frame(window,
                  bg = "#4884d4",
                  height = screen_height,
                  width = sidewidth,
                  relief = GROOVE
)
sideframe.pack(side=RIGHT)

mainwidth = screen_width * .75
mainframe = Frame(window,
                  bg = "#afb6bd",
                  height = screen_height,
                  width = mainwidth,
                  relief = GROOVE
)
mainframe.pack(side=LEFT)


window.config(cursor="none")
window.overrideredirect(1)
window.mainloop()