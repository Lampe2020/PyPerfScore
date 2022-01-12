#!/usr/bin/python

import sys
import time as t

def run_test(is_graphical = False):
    runs_max = 1000000
    runs_passed = 0
    number = 0
    time_at_start = t.time()
    while runs_passed <= runs_max:
            if runs_passed < runs_max:
                    print(number, end="\r")
                    number +=1
                    runs_passed += 1
            elif runs_passed == runs_max:
                    print(number)
                    time_at_finish = t.time()
                    time_to_complete = time_at_finish - time_at_start
                    print("Your computer needed " + str(round(time_to_complete, 3)) + " seconds to count from zero to " + str(runs_max) + " as fast as it could.")
                    score = runs_max / time_to_complete
                    print("So the score is " + str(round(score)) + ".")
                    return

def load_gui(force_to_run = False):
    gui = Tk()
    gui.title("PyPerfScore GUI")
    if force_to_run == False:
        messagebox.showinfo("Welcome!", """The GUI isn't implemented just yet, please check for new versions that have this feature implemented!\nClicking "OK" below will run the test anyway in command-line mode.""")
        print("The GUI isn't fully implemented yet, anyway, the test will be performed in command-line mode below:")
        gui.destroy()
        run_test(True)
    if force_to_run == True:
        print("Ok, the GUI will be loaded if possible. Note that this will probably cause a traceback.\nThe creator of this code is not responsible for any damage caused by this part of the code itself or its use!")
        messagebox.showinfo("Welcome!", """The GUI isn't fully implemented just yet!\nAnyway, since you run this program with "--force-gui" it will try to load the full GUI. Note that this will probably cause a traceback.\nThe creator of this code is not responsible for any damage caused by this part of the code itself or its use!""")
        #graphical code goes here
        messagebox.showinfo("Done!", """Perfect, the part of the code that is still in development seems to not have crashed anything! If you like to submit issues that occurred, please go to "https://www.github.com/Stehlampe2020/PyPerfScore/issues" to report them.\n\n*End of Code*""")
        gui.destroy()
        print("""Perfect, the part of the code that is still in development seems to not have crashed anything! If you like to submit issues that occurred, please go to "https://www.github.com/Stehlampe2020/PyPerfScore/issues" to report them.\n*End of code*""")
    
def ask_for_args():
    args = sys.argv
    if len(args) == 2:
        if args[-1] == "--load-gui":
            print("Loading GUI...")
            load_gui()
        elif args[-1] == "--force-gui":
            print("Loading GUI...")
            load_gui(True)
        else:
            print("""Incorrect argument used!\nThe only arguments that will be accepted are "--load-gui" and "--force-gui".\n"--load-gui" will only load the parts of the GUI that are fully implemented by now, "--force-gui" will try to run the full GUI even though some parts may cause crashes.""")
            exit()
    elif len(args) >= 3:
        print("Too many arguments!\n(This program only takes one...)")
        exit()
    elif len(args) == 1:
        print("""No command-line options were detected, running in command-line mode.\nIf you intended to run this program in graphical mode, press [Ctrl] + [C] now to cancel and re-run this program with the argument "--load-gui".""")
        run_test()
    else:
        print("An unknown error occurred while checking for command-line options, please report this behaviour and the conditions under which this error occurred!")

try:
    import tkinter
except ImportError:
    print("""Importing Python module "tkinter" failed, you will only be able to run this program in command-line mode!""")
else:
    try:
        from tkinter import *
        from tkinter import messagebox
        ask_for_args()
    except KeyboardInterrupt:
        print("\n[Ctrl]+[C] was pressed, exiting...")
        pass
