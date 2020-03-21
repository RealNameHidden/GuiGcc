from util.util import Util
import tkinter as tk

class MainWindow:
    def __init__(self):
        util = Util();
        root = tk.Tk();
        root.title("Smart Gcc GUI");

        width_of_window = 500;
        height_of_window = 500;
        canvas = tk.Canvas(root, width=width_of_window, height=height_of_window)
        canvas.pack()
        """
        Setting the window to the middle of the screen
        """
        util.center_window(width_of_window,height_of_window,root)
        frame1 = tk.Frame(root, bg="#AEB6BF")
        frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=1)

        btn_compile = tk.Button(frame1, text="Compile", width=6)
        btn_compile.pack()


