import tkinter as tk
import os

class FileWindow:
    def __init__(self, file):
        root = tk.Tk()
        root.title("Smart Gcc GUI")

        width_of_window = 600
        height_of_window = 700
        canvas = tk.Canvas(root, width=width_of_window, height=height_of_window)
        canvas.pack()
        frame0 = tk.Frame(root, bg="#8C8C8C")
        frame0.place(relx=0, rely=0, relwidth=1, relheight=1)
        frame1 = tk.Frame(frame0, bg="#668E39", bd=2)
        frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=1)
        S = tk.Scrollbar(frame1, bd=3)
        T = tk.Text(frame1, height=10, width=400, background="white", foreground="black", font=("sans-serif", 10))
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        with open(file, 'r') as filehandle:
            filehandle.seek(0,0)
            while True:
                # read a single line
                line = filehandle.readline()
                if not line:
                    break
                T.insert(tk.END,line)
                
        T.config(state=tk.DISABLED)
        root.mainloop()
        filehandle.close()