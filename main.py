import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
canvas = tk.Canvas(root, height = Height, width = Width, bg = bgColor)
frame = tk.Frame(root, bg = windowColor)
labelMain = tk.Label(text="Main Menu")
labelMain.pack()
canvas.pack()
frame.place(relwidth=1-paddingLEFT-paddingRIGHT,
            relheight=1-paddingUP-paddingDOWN,
            relx=paddingLEFT,
            rely=paddingUP)
root.mainloop()