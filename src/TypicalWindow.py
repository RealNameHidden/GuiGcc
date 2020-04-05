import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import src.FileWindow as fileWindow
import src.Start as start
from util.commandDict import CommandDict as cd
from util.util import Util


class TypicalWindow:
    defaultFile = 'Select a file'
    filename = defaultFile
    dict = cd()
    executeList = ['C:\\MinGW\\bin\\gcc.exe']
    selectedOptions = set([])
    listBoxBuffer = set([])

    def typicalUserOption (self, value):
        self.selectedOptions.add(value)

    def selectUsedOption(self, event):
        widget = event.widget
        selection = widget.curselection()
        if len(selection) != 0:
            value = widget.get(selection[0])
            self.selectedOptions.add(value)

    def selectOptionUpdateListBox(self, listBox, value):
        if self.listBoxBuffer.__contains__(value):
            idx = listBox.get(0, tk.END).index(value)
            listBox.delete(idx)
            listBox.insert(0, value)
            self.selectedOptions.add(value)
        else:
            self.listBoxBuffer.add(value)
            listBox.insert(0, value)
            self.selectedOptions.add(value)

    def askSwitchMode(self, root):
        ans = messagebox.askquestion(title="Switch user mode",
                                     message="Switching user mode will close the current window, do you want proceed?")
        if ans == 'yes':
            root.destroy()
            start_window = start.Start()

    def openFileDialog(self, lbl_file):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                   filetypes=(("c files", "*.c"), ("all files", "*.*")))
        if self.filename != "":
            lbl_file.configure(text=self.filename)
            fileWindow.FileWindow(self.filename)

    def getCommands(self, baseList):
        if baseList['checkCompile'].get():
            self.executeList.append(self.dict.gcc_basic['checkCompile'])
        if baseList['checkLink'].get():
            self.executeList.append(self.dict.gcc_basic['checkLink'])
        if baseList['checkDebug'].get():
            self.executeList.append(self.dict.gcc_basic['checkDebug'])

        # Adding options
        for option in self.selectedOptions:
            self.executeList.append(option)

        if self.filename != self.defaultFile and self.filename != "":
            self.executeList.append(self.filename)

    def runCommand(self, T, baseList):
        self.getCommands(baseList)

        if self.filename != self.defaultFile and self.filename != "":
            commandListString = ""
            quote = subprocess.run(self.executeList, shell=True, capture_output=True)
            T.delete('1.0', tk.END)
            print(quote)
            if quote.returncode == 0:
                T.insert(tk.END, "---Command execution successful---\n\n")
                itercom = iter(self.executeList)
                next(itercom)
                for com in itercom:
                    commandListString = commandListString + com + " "
                print(commandListString)
                T.insert(tk.END, "command:" + " gcc " + commandListString)
            else:
                T.insert(tk.END, "Error in command!\n\n")
                T.insert(tk.END, quote.stderr.decode())
            T.insert(tk.END, quote.stdout.decode())

            # Emtying lists
            self.executeList = ['C:\\MinGW\\bin\\gcc.exe']
            self.selectedOptions.clear()
        else:
            messagebox.showerror("No file selected.", "Please select a file to compile.")

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
        basicList = {'checkCompile': checkCompile, 'checkDebug': checkDebug, 'checkLink': checkLink}
        ########

        """
        Background frame
        """
        frame0 = tk.Frame(root, bg="#8C8C8C")
        frame0.place(relx=0, rely=0, relwidth=1, relheight=1)

        """
        Frame - switch user mode
        """
        lbl_user = tk.Label(frame0, text="Typical", font="TimesNewRoman", bg="#8C8C8C", padx=4)
        lbl_user.place(relx=0.02, rely=0.02)
        btn_switch = tk.Button(frame0, text="Switch mode", bd=3, activebackground="#BCE27F",
                               command=lambda: self.askSwitchMode(root))
        btn_switch.place(relx=0.95, rely=0.02, anchor="ne")

        """
        Frame 2 - output window
        """
        # The out put widget
        frame2 = tk.Frame(frame0, bg="#668E39", bd=2)
        frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.5)
        S = tk.Scrollbar(frame2, bd=3)
        T = tk.Text(frame2, height=4, width=400, background="black", foreground="white", font=("sans-serif", 10))
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        """
        Frame 1 - run button
        """
        util.center_window(width_of_window, height_of_window, root)
        frame1 = tk.Frame(frame0, bg="#BCE27F", bd=3)
        frame1.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.07, anchor='n')
        btn_run = tk.Button(frame1, text="Run Command", width=6, bg="#EFEEEA", activebackground="#BCE27F", bd=1,
                            command=lambda: self.runCommand(T, basicList))
        btn_run.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

        """
        Frame 3 - File picker & Label
        """
        frame3 = tk.Frame(frame0, bg="#241C15", bd=2)
        frame3.place(relx=0.02, rely=0.1, relwidth=0.5, relheight=0.05)
        lbl_file = tk.Label(frame3, text=self.filename, bg="#241C15", fg="#8C8C8C")
        lbl_file.place(relx=0.1, relwidth=1)
        btn_file = tk.Button(frame3, text="File", width=3, bg="#F6F6F4", command=lambda: self.openFileDialog(lbl_file))
        btn_file.place(relwidth=0.2, relheight=1)
        # label

        lbl_file = tk.Label(frame3, text=self.filename, bg="#241C15", fg="#8C8C8C")
        lbl_file.place(relx=0.5)

        """
        Frame 4 - Checkbox and options frame
        """
        ########

        frame4 = tk.Frame(frame0, bg="#241C15", bd=2)
        frame4.place(relx=0.02, rely=0.2, relwidth=0.45, relheight=0.05)
        chk_compile = tk.Checkbutton(frame4, text="Compile", variable=checkCompile, selectcolor="#BCE27F")
        chk_link = tk.Checkbutton(frame4, text="Link", variable=checkLink, selectcolor="#BCE27F")
        chk_debug = tk.Checkbutton(frame4, text="Debug", variable=checkDebug, selectcolor="#BCE27F")
        chk_compile.place(relwidth=0.33, relheight=1)
        chk_debug.place(relx=0.7, relwidth=0.33, relheight=1)
        chk_link.place(relx=0.35, relwidth=0.33, relheight=1)

        """
        Typical user options
        """
        codeGenerationOptions = cd.gcc_codegeneration.values()
        codeGenerationOption = tk.StringVar()
        codeGenerationOption.set("Code generation")

        codeOptimizationOptions = cd.gcc_codeoptimization.values()
        codeOptimizationOption = tk.StringVar()
        codeOptimizationOption.set("Code optimization")

        frameTOptions = tk.Frame(frame0, bg="#241C15", bd=2)
        frameTOptions.place(relx=0.02, rely=0.27, relwidth=0.45, relheight=0.05)
        btn_cg = tk.OptionMenu(frameTOptions, codeGenerationOption, *codeGenerationOptions,
                               command=lambda x: self.typicalUserOption(x))
        btn_cg.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        btn_co = tk.OptionMenu(frameTOptions, codeOptimizationOption, *codeOptimizationOptions,
                               command=lambda x: self.typicalUserOption(x))
        btn_co.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        """
        Frame 5 - All options menu 
        """
        Options = cd.gcc_codegeneration.values()
        selected = tk.StringVar()

        selected.set("All Options")
        frameAllOptions = tk.Frame(frame0, bg="#241C15", bd=2)
        frameAllOptions.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.25)
        usedOptions = tk.Listbox(frameAllOptions, selectmode=tk.MULTIPLE)
        usedOptions.place(relx=0, rely=0.2, relwidth=1)
        usedOptions.bind("<<ListboxSelect>>", self.selectUsedOption)
        btn_f = tk.OptionMenu(frameAllOptions, selected, *Options,
                              command=lambda x: self.selectOptionUpdateListBox(usedOptions, x))
        btn_f.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.15, anchor='n')

        ##### List Box ####
        root.mainloop()
