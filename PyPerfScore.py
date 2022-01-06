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
                    exit()

def load_gui():
    gui = Tk()
    gui.title("PyPerfScore GUI")
    messagebox.showinfo("Welcome!", """The GUI isn't implemented just yet, please check for new versions that have this feature implemented!\nClicking "OK" below will run the test anyway in command-line mode.""")
    print("The GUI isn't implemented yet, anyway, the test will be performed in command-line mode below:")
    gui.destroy()
    run_test(True)
    
def ask_for_args():
    args = sys.argv
    if len(args) == 2:
        if args[-1] == "--load-gui":
            print("Loading GUI...")
            load_gui()
        else:
            print("""Incorrect argument used!\nThe only argument that will be accepted is "--load-gui"!""")
            exit()
    elif len(args) >= 3:
        print("Too many arguments!\n(This program only takes one...)")
        exit()
    elif len(args) == 1:
        print("""No command-line options were detected, running in command-line mode.\nIf you intended to run this program in graphical mode, press [Ctrl] + [C] now to cancel and re-run this program with the argument "--load-gui".\nDon't worry if a traceback is generated when pressing [Ctrl] + [C], that's intended Python behaviour.""")
        run_test()
    else:
        print("An unknown error occurred while checking for command-line options, please report this behaviour and the conditions under which this error occurred!")

try:
    import tkinter
except ImportError:
    print("""Importing Python module "tkinter" failed, you will only be able to run this program in command-line mode!""")
else:
    from tkinter import *
    from tkinter import messagebox
    ask_for_args()
