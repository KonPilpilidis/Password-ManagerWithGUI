import tkinter as tk
from tkinter import filedialog, Text
from theme_module import *
from pmMethods import *
root = tk.Tk()
root.geometry(WindowsSize)
root.title(TITLE+' '+VERSION)
if platform.system() != "Linux":
    root.iconbitmap(LOGO)
else:
    root.tk.call('wm', 'iconphoto', root._w, tk.Image('photo',file=LOGO))
canvas = tk.Canvas(root, height = Height, width = Width, bg = bgColor)
# frame = tk.Frame(root, bg = windowColor)
# labelMain = tk.Label(text="Main Menu")
# labelMain.pack()
# canvas.pack()
# frame.place(relwidth=1-paddingLEFT-paddingRIGHT,
#             relheight=1-paddingUP-paddingDOWN,
#             relx=paddingLEFT,
#             rely=paddingUP)
root.mainloop()