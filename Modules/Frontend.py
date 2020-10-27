import tkinter as tk
from tkinter import ttk,StringVar,IntVar,messagebox,Radiobutton,OptionMenu

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
        for page , Title in [(LoginPage ,'Login'),
                             (RegistrationPage,'Add new user'),
                             (MainMenuPage,'Main Menu'),
                             (PasswordGenerationPage ,'Password Generator')]:
            frame = page(container,self,Title)
            self.frames[page] = frame
            frame.grid(row = 0,column = 0,sticky='news',pady=1,padx=1)
        print(self.frames)
        self.show_frame(LoginPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    @staticmethod
    def clear_text(*args):
        for entry in args:
            entry.delete(0,'end')
        
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
        filemenu.add_command(label='Return to main menu',command = lambda: controller.show_frame(MainMenuPage))
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
                   command = lambda: controller.clear_text(self.entry1,self.entry2)).grid(row=1, column=3,rowspan=2,
                                                pady=int(0.5 * PADDI), padx=int(0.5 * PADDI))
        ttk.Separator(self).grid(row=4,column=0,columnspan=4,sticky='news',ipadx=100)
        # login button
        #loginButton = ttk.Button(parent, text="Login", command=validateLogin).grid(row=4, column=0)
        ttk.Button(self, text="Login", command = lambda: Manager.login(self)).grid(row = 5, column=1,columnspan=1,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
        ttk.Button(self, text="New user", command = lambda: controller.show_frame(RegistrationPage)).grid(row = 5, column=2,columnspan=1,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
        ttk.Button(self, text="Skip", command = lambda: controller.show_frame(PasswordGenerationPage)).grid(row = 6, column=1,columnspan=2,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
    def entry_cb(self,event):
        #print('event.char', event.keycode, event.keysym )
        self.entry2.config(show='')
        # Hide text after 1000 milliseconds
        self.entry2.after(1000, lambda: self.entry2.config(show='*'))
    def login(self):
        pass

class RegistrationPage(MainPage):
    def __init__(self,parent,controller,title):
        super().__init__(parent,controller,title)
        # Variables to be filled in by the user
        Username = StringVar()
        Newpasswd = StringVar()
        Reppasswd = StringVar()
        Name = StringVar()
        Surname = StringVar()
        Email = StringVar()
        Gender = IntVar()
        Country = StringVar()
        list_of_country = ('Greece', 'Germany','UK','USA','Italy','France')
        # Page widgets
        ttk.Label(self, text="User alias",
                  font=M_font,
                  background=bgColor,
                  foreground=textColor).grid(row=1,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="First Name",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=2,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Last Name",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=3,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Email",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=4,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Gender",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=5,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Country",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=6,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Enter masterpassword",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=7,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        ttk.Label(self, text="Re-enter masterpassword",
                font=M_font,
                background=bgColor,
                foreground=textColor).grid(row=8,column=0,sticky='news',
                                      padx= int(PADDI * 0.5),pady= int(PADDI * 0.5))
        
        self.username = tk.Entry(self, text = "alias",textvariable = Username)
        self.username.grid(row=1,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.name = tk.Entry(self, text = "John",textvariable = Name)
        self.name.grid(row=2,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.surname = tk.Entry(self, text = "Doe",textvariable = Surname)
        self.surname.grid(row=3,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.email = tk.Entry(self, text = "johndoe@john_doe.org",textvariable = Email)
        self.email.grid(row=4,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.male = Radiobutton(self,text="Male",variable= Gender, value=1)
        self.male.grid(row=5,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.female = Radiobutton(self,text="Female",variable= Gender, value=2)
        self.female.grid(row=5,column=2,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.droplist = OptionMenu(self,Country, *list_of_country)
        self.droplist.config(width=15)
        self.droplist.grid(row=6,column=1,sticky='news',
               padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        
        
        self.entry1 = pwd1 = tk.Entry(self, text = "Masterpassword", textvariable = Newpasswd, show = '*')
        pwd1.grid(row=7,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        self.entry2 = pwd2 = tk.Entry(self, text = "Masterpassword",textvariable = Reppasswd, show = '*')
        pwd2.grid(row=8,column=1,sticky='news',padx = int(PADDI * 0.5),pady = int(PADDI * 0.5))
        pwd1.bind("<Enter>", lambda event, entry=self.entry1: self.entry_cb(event,entry))
        pwd2.bind("<Enter>", lambda event, entry=self.entry2: self.entry_cb(event,entry))
        ttk.Separator(self).grid(row=9,column=0,columnspan=3,sticky='news',ipadx=100)
        
        
        ttk.Button(self, text="Register", command = self.register).grid(row = 9, column=0,sticky='news',
                                                 pady = int(0.5 * PADDI), padx = int(0.5 * PADDI))
        ttk.Button(self, text="Clear",
                   command = lambda: controller.clear_text(username,name,surname,email,pwd1,pwd2)).grid(row=9, column=1,
                                                pady=int(0.5 * PADDI), padx=int(0.5 * PADDI))
        ttk.Button(self, text="Back to login",
                   command = lambda: controller.show_frame(LoginPage)).grid(row=9, column=2,
                                                pady=int(0.5 * PADDI), padx=int(0.5 * PADDI))
    def entry_cb(self,event,entry):
        entry.config(show='')
        # Hide text after 1000 milliseconds
        entry.after(1000, lambda: entry.config(show='*'))
    
    def register(self):
        if self.entry1.get() == self.entry2.get() and self.entry1.get() != None:
            if self.username.get() != '':
                controller.manager = Manager(self.username.get(),self.entry1.get())    
            else:
                messagebox.showwarning("Username missing","You need to enter a user alias to register as a new user.")
        else:
            messagebox.showwarning("Masterpasswords not matching","The masterpassword you entered the first time is different than the password you entered the second time.")

class MainMenuPage(MainPage):
    def __init__(self,parent,controller,title):
        super().__init__(parent,controller,title)
        pass

class PasswordGenerationPage(MainPage):
    def __init__(self, parent, controller,title):
        super().__init__(parent, controller,title)



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()