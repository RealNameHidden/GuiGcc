from util.util import Util
import tkinter as tk
import subprocess

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
        frame1.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.1)

        #The out put widget
        frame2 = tk.Frame(root)
        frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.5)
        S = tk.Scrollbar(frame2)
        T = tk.Text(frame2, height=4, width=100, background="black", foreground="white", font="cambria")
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = subprocess.run(['C:\\MinGW\\bin\\gcc.exe','gcc','--version'], shell="true", capture_output="true")
        print(quote)
        T.insert(tk.END, quote.stdout.decode())
        btn_compile = tk.Button(frame1, text="Compile", width=6)
        btn_compile.pack()


