from util.util import Util
from util.commandDict import CommandDict as cd
import tkinter as tk
import subprocess


class MainWindow:
    file = 'C:\\Users\\14387\\Desktop\\winme.c'
    dict = cd()
    executeList=['C:\\MinGW\\bin\\gcc.exe','gcc']

    def getCommands(self,baseList):
        if baseList['checkCompile'].get():
            self.executeList.append(self.dict.gcc_basic['checkCompile'])

        if baseList['checkLink'].get():
            self.executeList.append(self.dict.gcc_basic['checkLink'])
        if baseList['checkDebug'].get():
            self.executeList.append(self.dict.gcc_basic['checkDebug'])
        # for command in basicList:
        #     if command.get():
        #         # self.executeList.append(self.dict.gcc_basic[command])
        #         print(command.get())
        self.executeList.append(self.file)

    def runCommand(self,T,baseList):
         self.getCommands( baseList)
         print(self.executeList)
         quote = subprocess.run(self.executeList, capture_output=True)
         T.delete('1.0', tk.END)
         print(quote)
         if quote.returncode==0:
            T.insert(tk.END, "---Command execution successful---\n\n")
         else:
             T.insert(tk.END, "Error in command!\n\n")
             T.insert(tk.END, quote.stderr.decode())
         T.insert(tk.END, quote.stdout.decode())
         self.executeList = ['C:\\MinGW\\bin\\gcc.exe', 'gcc']
         return quote

    def __init__(self):
        util = Util()
        root = tk.Tk()
        root.title("Smart Gcc GUI")

        width_of_window = 600
        height_of_window = 700
        canvas = tk.Canvas(root, width=width_of_window, height=height_of_window)
        canvas.pack()

        checkCompile = tk.BooleanVar()
        checkDebug = tk.BooleanVar()
        checkLink = tk.BooleanVar()
        ########
        basicList = {'checkCompile':checkCompile,'checkDebug': checkDebug, 'checkLink':checkLink}
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
        Frame 2 - output window
        """
        # The out put widget
        frame2 = tk.Frame(frame0, bg="#668E39", bd=2)
        frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.5)
        S = tk.Scrollbar(frame2, bd=3)
        T = tk.Text(frame2, height=4, width=400, background="black", foreground="white", font="cambria")
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        """
        Frame 1 - run button
        """
        util.center_window(width_of_window,height_of_window,root)
        frame1 = tk.Frame(frame0, bg="#BCE27F", bd=3)
        frame1.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.07, anchor='n')
        btn_run = tk.Button(frame1, text="Run Command", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1, command= lambda: self.runCommand(T,basicList))
        btn_run.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

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


        frame4 = tk.Frame(frame0, bg="#241C15", bd=2)
        frame4.place(relx = 0.02, rely = 0.2, relwidth = 0.4, relheight = 0.05)
        chk_compile = tk.Checkbutton(frame4, text="Compile", variable= checkCompile, selectcolor="#BCE27F")
        chk_link = tk.Checkbutton(frame4, text="Link", variable= checkLink,  selectcolor="#BCE27F")
        chk_debug = tk.Checkbutton(frame4, text="Debug", variable= checkDebug, selectcolor="#BCE27F")
        chk_compile.place(relwidth=0.33, relheight=1)
        chk_debug.place(relx=0.7, relwidth=0.33,relheight=1)
        chk_link.place(relx=0.35,relwidth=0.33 ,relheight=1 )

        """
        Frame 5 - All options menu 
        """
        Options = ['Option 1',
                   'Option 2',
                   'Option 3']
        selected = tk.StringVar()
        selected.set("All Options")
        frameAllOptions = tk.Frame(frame0, bg="#241C15", bd=2)
        frameAllOptions.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.25)
        btn_f = tk.OptionMenu(frameAllOptions, selected, *Options )
        btn_f.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.15, anchor='n')
        ##### List Box ####

        usedOptions =tk.Listbox(frameAllOptions)
        usedOptions.insert(0,"-fopt")
        usedOptions.place(relx=0,rely=0.2, relwidth=1)

        root.mainloop()




