from util.util import Util
from src.NoviceWindow import NoviceWindow
from src.TypicalWindow import TypicalWindow
from src.ExpertWindow import ExpertWindow
import tkinter as tk

class Start:
    util = Util()

    def makeWindow(self,root,type):
        print(type)
        root.destroy()
        if type =='Beginner':
            main = NoviceWindow()
        elif type =='Medium':
            main = TypicalWindow()
        elif type =='Expert':
            main = ExpertWindow()


    def __init__(self):
            root = tk.Tk()

            root.title("Smart Gcc GUI")

            width_of_window=300
            height_of_window=400
            canvas = tk.Canvas(root,width=width_of_window,height=height_of_window)
            canvas.pack()
            """
            Setting the window to the middle of the screen
            """
            self.util.center_window(width_of_window,height_of_window,root)
            frame0 = tk.Frame(root, bg="#8C8C8C")
            frame0.place(relx=0, rely=0, relwidth=1, relheight=1)
            frame1 = tk.Frame(root , bg="#AEB6BF")
            frame1.place(relx=0.01,rely=0.01,relwidth=0.99,relheight=0.99)

            btn_beginner = tk.Button(frame1, text="Beginner", width=6, command= lambda: self.makeWindow(root,btn_beginner.cget('text')))
            btn_beginner.pack()
            btn_medium = tk.Button(frame1, text="Medium", width=6,  command= lambda: self.makeWindow(root,btn_medium.cget('text')))
            btn_medium.pack()
            btn_expert = tk.Button(frame1, text="Expert", width=6,  command= lambda: self.makeWindow(root,btn_expert.cget('text')))
            btn_expert.pack()

            # btn_beginner.bind('<Button-1>', self.makeWindow)
            root.mainloop()
