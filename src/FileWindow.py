import tkinter as tk

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


