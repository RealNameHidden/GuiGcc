from util.util import Util
import tkinter as tk
import subprocess

class MainWindow:
    def __init__(self):
        util = Util();
        root = tk.Tk();
        root.title("Smart Gcc GUI");

        width_of_window = 600;
        height_of_window = 700;
        canvas = tk.Canvas(root, width=width_of_window, height=height_of_window)
        canvas.pack()
        """
        Background frame
        """
        frame0 = tk.Frame(root, bg="#8C8C8C")
        frame0.place(relx=0,rely=0,relwidth=1,relheight=1)

        """
        Frame - user mode
        """
        lbl_user=tk.Label(frame0, text="Novice", font="TimesNewRoman", bg="#8C8C8C", padx=4)
        lbl_user.place(relx=0.02, rely=0.02)
        btn_switch=tk.Button(frame0, text="Switch mode", bd=3, activebackground="#BCE27F")
        btn_switch.place(relx=0.95, rely=0.02 , anchor="ne")

        """
        Frame - all options
        """
        # selected = str()
        # Options = ["-O2",
        #            "-O3"]
        # frameAllOptions = tk.Frame(frame0, bg="#241C15", bd=2)
        # frameAllOptions.place(relx=0.8, rely=0.1, relwidth=0.3, relheight=0.05)
        # btn_alloptions = tk.OptionMenu(frameAllOptions, text="All options",variable= selected, *Options, width=3, bg="#F6F6F4")
        # btn_alloptions.place(relwidth=0.4, relheight=1)


        """
        Frame 1 - run button
        """
        util.center_window(width_of_window,height_of_window,root)
        frame1 = tk.Frame(frame0, bg="#BCE27F", bd=3)
        frame1.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.07, anchor='n')
        btn_run = tk.Button(frame1, text="Run Command", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1)
        btn_run.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

        """
        Frame 2 - output window
        """
        #The out put widget
        frame2 = tk.Frame(frame0,bg="#668E39", bd=2)
        frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.5)
        S = tk.Scrollbar(frame2,bd=3)
        T = tk.Text(frame2, height=4, width=400, background="black", foreground="white", font="cambria")
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = subprocess.run(['C:\\MinGW\\bin\\gcc.exe','gcc','--version'], shell=True, capture_output=True)
        print(quote)
        T.insert(tk.END, quote.stdout.decode())

        """
        Frame 3 - File picker & Label
        """
        frame3 = tk.Frame(frame0, bg="#241C15", bd=2)
        frame3.place(relx=0.02, rely=0.1, relwidth=0.3, relheight=0.05)
        btn_file = tk.Button(frame3, text="File", width=3, bg="#F6F6F4")
        btn_file.place(relwidth=0.4, relheight=1)
        # label
        lbl_file = tk.Label(frame3, text="C:/Hello.c", bg="#241C15", fg="#8C8C8C")
        lbl_file.place(relx=0.5)

        """
        Frame 4 - Checkbox and options frame
        """
        ########
        checkCompile = int()
        checkDebug = int()
        checkLink = int()
        ########

        frame4 = tk.Frame(root, bg="#241C15", bd=2)
        frame4.place(relx = 0.02, rely = 0.2, relwidth = 0.4, relheight = 0.05)
        chk_compile = tk.Checkbutton(frame4, text="Compile", variable= checkCompile,  onvalue=1, offvalue=0, selectcolor="#BCE27F")
        chk_debug = tk.Checkbutton(frame4, text="Debug", variable= checkDebug,  onvalue=1, offvalue=0, selectcolor="#BCE27F")
        chk_link = tk.Checkbutton(frame4, text="Link", variable=checkLink, onvalue=1, offvalue=0, selectcolor="#BCE27F")
        chk_compile.place(relwidth=0.33, relheight=1)
        chk_debug.place(relx=0.35,relwidth=0.33 ,relheight=1)
        chk_link.place(relx=0.7, relwidth=0.33,relheight=1)

        """
        Frame 5 - All options menu 
        """



