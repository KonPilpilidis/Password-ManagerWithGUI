import platform
import configparser
from config import *
from random import choice
from string import ascii_letters, digits, punctuation
import tkinter as tk
from tkinter import filedialog, Text

def generateSalt():
    """
    The function generates a random four character string to make dictionnairy attacks more difficult.
    :return: str len(4)
    """
    salt = ""
    for i in range(4):
        salt += choice(ascii_letters + digits + punctuation)
    return salt

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(setup)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


configuration = configparser.ConfigParser()

with open("config.ini","w") as file:
    configuration.add_section('global')       # Information important for the function of parts of the programm
    configuration.set('global', 'salt', generateSalt())
    configuration.write(file)




UserInput = 'Username', 'Master Password'

if __name__ == '__main__':
    setup = tk.Tk()
    setup.geometry(f"{str(int(Height/2))}x{str(int(Width/2))}")
    setup.title(f'Setup: {Title} {Version}')
    if platform.system() != "Linux":
        setup.iconbitmap('setup.ico')
    else:
        setup.tk.call('wm', 'iconphoto', root._w, tk.Image('photo', file='setup.png'))
    Explanation = tk.Text(setup, height=10, width=int(Width/2-BorderRight-BorderLeft))
    Explanation.pack()
    quote = """If you are too lazy to give a passphrase and a password for each of your amazing passwords. You can
    provide a user name and a masterpassword.
    \nMake sure to chose a a user name and a password which you can remember... or write it down somewhere.
    \nIf you lose them, you would have to reset all your passwords."""
    Explanation.insert(tk.END, quote)
    ents = makeform(setup, UserInput)
    setup.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(setup, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(setup, text='Quit', command=setup.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    setup.mainloop()


#canvas = tk.Canvas(root, height = Height, width = Width, bg = bgColor)
# frame = tk.Frame(root, bg = windowColor)
# labelMain = tk.Label(text="Main Menu")
# labelMain.pack()
# canvas.pack()
# frame.place(relwidth=1-paddingLEFT-paddingRIGHT,
#             relheight=1-paddingUP-paddingDOWN,
#             relx=paddingLEFT,
#             rely=paddingUP)
#root.mainloop()