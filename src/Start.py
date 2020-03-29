from util.util import Util
from src.MainWindow import MainWindow
import tkinter as tk

class Start:
    util = Util()
    root = tk.Tk()
    def makeWindow(self,event):
        print("Hi")
        self.root.destroy()
        main = MainWindow()


    def __init__(self):

            self.root.title("Smart Gcc GUI")

            width_of_window=300;
            height_of_window=400;
            canvas = tk.Canvas(self.root,width=width_of_window,height=height_of_window)
            canvas.pack()
            """
            Setting the window to the middle of the screen
            """
            self.util.center_window(width_of_window,height_of_window,self.root)
            frame1 = tk.Frame(self.root , bg="#AEB6BF")
            frame1.place(relx=0.01,rely=0.01,relwidth=0.99,relheight=0.99)

            btn_beginner = tk.Button(frame1, text="Beginner", width=6)
            btn_beginner.pack()
            btn_medium = tk.Button(frame1, text="Medium", width=6)
            btn_medium.pack()
            btn_expert = tk.Button(frame1, text="Expert", width=6)
            btn_expert.pack()

            btn_beginner.bind('<Button-1>', self.makeWindow)
            self.root.mainloop()
