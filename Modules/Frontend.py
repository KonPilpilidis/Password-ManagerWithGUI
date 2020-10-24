import tkinter as tk
from tkinter import ttk,StringVar,IntVar
import os
from Backend import *
#from Backend import Password
###################################
##         Theme Module          ##
###################################
path = os.path.join(os.path.expanduser('~'),'resources',)
TITLE = "Password Manager"

VERSION = "0.0.1"
LOGO_win = os.path.join(os.getcwd(),'resources',"logo.ico")
LOGO_other = os.path.join(os.getcwd(),'resources',"logo.gif")
    
# Geometry
WFACT = 0.500
PADDI = 20

# Palette
bgColor = "#1A1A2E"
windowColor = "#15213E"
buttonColor = "#E94560"
textColor = "#FFFFFF"

Font = 'Montserrat'
L_font = (Font,12,'bold')
M_font = (Font,10)
S_font = (Font,10,'italic')

class MainApplication(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        height = self.winfo_screenheight()
        width = self.winfo_screenwidth()
        size = str(int(WFACT * width)) + "x" + str(int(WFACT * height))
        self.geometry(size)
        self.configure(background=windowColor)
        self.title(TITLE + ' ' + VERSION)
        try:
            self.iconbitmap(LOGO_win)
            print('entered')
        except:
            self.tk.call('wm', 'iconphoto', self._w, tk.Image('photo', file=LOGO_other))
        container = tk.Frame(self)
        container.place(anchor="c", relx=.5, rely=.5)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for page , Title in [(LoginPage , 'Login'),(MainMenuPage , 'Main Menu') , (PasswordGenerationPage , 'Password Generator')]:
            frame = page(container,self,Title)
            self.frames[page] = frame
            frame.grid(row = 0,column = 0,sticky='news',pady=1,padx=1)
        Manager.show_frame(self,LoginPage)
class MainPage(tk.Frame):
    def __init__(self,parent,controller,title):
        tk.Frame.__init__(self,parent,background=bgColor)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        # Create the menu top levels
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        editmenu = tk.Menu(menubar)

        # Creates the menu items
        ## File menu
        filemenu.add_command(label='Return to main menu',command = lambda: Manager.show_frame(controller,MainMenuPage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=controller.destroy)
        # Creates the edit menu
        editmenu.add_command(label="Undo")

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Edit", menu=editmenu)

        controller.configure(menu=menubar)
        # Adds the pages headline
        ttk.Label(self, text=title,
                 font=L_font,
                 background=bgColor,
                 foreground=textColor).grid(row=0,column=0,columnspan=10,padx = PADDI) # I use a very big columnspan to ensure that
                #the title will always be centered no matter how many columns the rest of the pages have.


class LoginPage(MainPage):
    def __init__(self,parent,controller,title):
        super().__init__(parent,controller,title)
        self.width = 4
        ttk.Label(self, text="Username",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=1,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Password",
                  font=M_font,background=bgColor,
                  foreground=textColor).grid(row=2,column=0,sticky='news',
                                             padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        username = StringVar()
        password = StringVar()
        use = self.entry1 = tk.Entry(self, textvariable = username)
        use.grid(row=1,column=1,columnspan=2,sticky='news',
               padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        pwd = self.entry2 = tk.Entry(self, textvariable = password, show='*')
        pwd.grid(row=2,column=1,columnspan=2,sticky='news',
               padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        pwd.bind("<Enter>", self.entry_cb)
        ttk.Button(self, text="Clear",
                   command = lambda: Manager.clear_text(use.get(),pwd.get())).grid(row=1, column=3,rowspan=2,
                                                pady=int(0.5 * PADDI), padx=int(0.5 * PADDI))
        ttk.Separator(self).grid(row=4,column=0,columnspan=4,sticky='news',ipadx=100)
        # login button
        #loginButton = ttk.Button(parent, text="Login", command=validateLogin).grid(row=4, column=0)
        ttk.Button(self, text="Login", command = lambda: Manager.login(self)).grid(row = 5, column=1,columnspan=1,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
        ttk.Button(self, text="Skip", command = lambda: Manager.show_frame(controller,PasswordGenerationPage)).grid(row = 5, column=2,columnspan=1,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
    def entry_cb(self,event):
        #print('event.char', event.keycode, event.keysym )
        self.entry2.config(show='')
        # Hide text after 1000 milliseconds
        self.entry2.after(1000, lambda: self.entry2.config(show='*'))

class MainMenuPage(MainPage):
    def __init__(self,parent,controller,title):
        super().__init__(parent,controller,title)


class PasswordGenerationPage(MainPage):
    def __init__(self, parent, controller,title):
        super().__init__(parent, controller,title)



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()