from util.util import Util
from src.NoviceWindow import NoviceWindow
from src.TypicalWindow import TypicalWindow
from src.ExpertWindow import ExpertWindow
import tkinter as tk
import pickle as pickle
import os

class Start:
    util = Util()
    preferred_screen=""
    def makeWindow(self,root,type):

        root.destroy()

        if type =='Beginner':
                self.preferred_screen = type

                novice = NoviceWindow()
                with open('settings.txt', 'wb') as settings:
                    pickle.dump(self, settings, -1)
        elif type =='Medium':
                self.preferred_screen = type
                medium = TypicalWindow()
                with open('settings.txt', 'wb') as settings:
                    pickle.dump(self, settings, -1)
                    # pickle.dump(medium, settings, -2)
        elif type =='Expert':
                self.preferred_screen = type
                expert = ExpertWindow()
                with open('settings.txt', 'wb') as settings:
                    pickle.dump(self, settings, -1)
                    # pickle.dump(expert, settings, -2)

    def __init__(self):
            root = tk.Tk()

            root.title("Smart Gcc GUI")

            width_of_window=300
            height_of_window=300
            canvas = tk.Canvas(root,width=width_of_window,height=height_of_window)
            canvas.pack()
            """
            Setting the window to the middle of the screen
            """
            self.util.center_window(width_of_window,height_of_window,root)
            frame0 = tk.Frame(root, bg="#8C8C8C")
            frame0.place(relx=0, rely=0, relwidth=1, relheight=1)
            frame1 = tk.Frame(frame0, bg="#8C8C8C", bd=3)
            frame1.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.6, anchor='n')

            lbl_user = tk.Label(frame0, text="Select your user type", font="TimesNewRoman", bg="#8C8C8C",bd=5, padx=4)
            lbl_user.place(relx=0.24, rely=0.04)

            btn_beginner = tk.Button(frame1, text="Beginner", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1, command= lambda: self.makeWindow(root,btn_beginner.cget('text')))
            btn_beginner.place(relx=0.5, rely=0.01, relwidth=0.98, relheight=0.2, anchor='n')
            btn_medium = tk.Button(frame1, text="Medium", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1, command= lambda: self.makeWindow(root,btn_medium.cget('text')))
            btn_medium.place(relx=0.5, rely=0.25,  relwidth=0.98, relheight=0.2, anchor='n')
            btn_expert = tk.Button(frame1, text="Expert", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1, command= lambda: self.makeWindow(root,btn_expert.cget('text')))
            btn_expert.place(relx=0.5, rely=0.5,relwidth=0.98, relheight=0.2, anchor='n')

            # btn_beginner.bind('<Button-1>', self.makeWindow)
            root.mainloop()
