from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("Antoni Screen")

icon = PhotoImage(file='img.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop()