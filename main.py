from Modules import Frontend
#import Backend
import tkinter as tk

root = tk.Tk()
root.geometry(Frontend.WindowsSize)
root.title(Frontend.TITLE + ' ' + Frontend.VERSION)
try:
    root.iconbitmap(Frontend.LOGO_win)
except:
    root.tk.call('wm', 'iconphoto', root._w, tk.Image('photo', file=Frontend.LOGO_other))
    print("Entered")
canvas = tk.Canvas(root, height = Frontend.Height, width = Frontend.Width, bg = Frontend.bgColor)
# frame = tk.Frame(root, bg = windowColor)
# labelMain = tk.Label(text="Main Menu")
# labelMain.pack()
# canvas.pack()
# frame.place(relwidth=1-paddingLEFT-paddingRIGHT,
#             relheight=1-paddingUP-paddingDOWN,
#             relx=paddingLEFT,
#             rely=paddingUP)
root.mainloop()