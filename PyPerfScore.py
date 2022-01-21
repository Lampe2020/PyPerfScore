#!/usr/bin/python

import sys
import time as t

global version
version = "0.2.2-alpha"
print("You are now running version " + version + """ of PyPerfScore. To check for newer versions, please check out "https://github.com/Stehlampe2020/PyPerfScore".""")

def run_test(is_graphical = False):
    cycles = 1000000    # This is the number that this program counts up to. Chage it if you want, it will only change how long the test takes and how accurate the score is (higher number -> test takes longer -> score is more accurate). 
    number = 0  # This is the number the program counts up from. Do not change this number. 
    time_at_start = t.time()    # Take a timestamp.
    if is_graphical == False:
        while number <= cycles:
                if number < cycles:
                        print(number, "/", cycles, end="\r")    # Print the number the program has by now to the terminal. Also show the target number for comparison. Set the line end to "\r" to move the cursor back to the start of the line, so the line is automatically overwritten when the new number is printed in the next cycle of the test.
                        number += 1 # Increment the number by one, this is what actually counts up. 
                elif number == cycles:
                        print(number, "=", cycles, end="\r")    # Print the final number, now equaling the target number. Set the line end to "\r" to move the cursor back to the start of the line, so the line is automatically overwritten when the conclusion is printed to the terminal later on.
                        time_at_finish = t.time()   # Take a timestamp. 
                        time_to_complete = time_at_finish - time_at_start   # Subtract the first timestamp off the second one to get the time in seconds the counting took. 
                        print("Your computer needed " + str(round(time_to_complete, 3)) + " seconds to count from zero to " + str(cycles) + " as fast as it could.")    # Print a conclusion to the terminal, overwriting the line where the testing happened. 
                        try:
                            score = cycles / time_to_complete   # Compute the score: divide the time the counting took by the number of cycles that the loop was run. 
                        except DivisionByZero:
                            print("Your computer seems to be too fast to run this test with a target number of", cycles, """cycles. Maybe multiply the value of the variable "cycles"?""")
                            return 1    # Return a 1 as a return code for this function. Later I will add a system to handle return values, for this reason I add the codes themselves already now.
                        print("So the score is " + str(round(score)) + ".") # Print the score in a nice form and rounded to a whole number to the terminal.
                        return 0    # Return a zero to signal the return value handler that everything went right. The return value handler will be added later. 
    elif is_graphical == True:
        load_gui(True)

def load_gui(force_to_run = False): # This function is for loading the GUI of the program but I think I will merge this function with the is_graphical=True part of run_test() later.
    gui = Tk()  # Define a windoe with the ID "gui".
    gui.title("PyPerfScore GUI")    # Give the window with the ID "gui" a title. 
    if force_to_run == False:
        messagebox.showinfo("Welcome!", """The GUI isn't implemented just yet, please check for new versions that have this feature implemented!\nClicking "OK" below will run the test anyway in command-line mode.""")
        print("The GUI isn't fully implemented yet, anyway, the test will be performed in command-line mode below:")    # Print a shortened version of the same message to the terminal for the case that the window doesn't show up or someone wants to understand what happened just based on the terminal output.
        gui.destroy()   # Destroy (close) the window with the ID "gui" after "OK" has been clicked in the messagebox above. 
        run_test(False) # Run the test itself in command-line mode. (Why I had this one set to True before? I don't know!)
    if force_to_run == True:
        print("Ok, the GUI will be loaded if possible. Note that this will probably cause a traceback.\nThe creator of this code is not responsible for any damage caused by this part of the code itself or its use!") # Warn the user in the command-line that errors could occur here. If the window doesn't show up or somehow freezes before displaying the warning graphically the user is warned. 
        messagebox.showwarning("Welcome!", """The GUI isn't fully implemented just yet!\nAnyway, since you run this program with "--full-gui" it will try to load the full GUI. Note that this will probably cause a traceback.\nThe creator of this code is not responsible for any damage caused by this part of the code itself or its use!""")  # Show the same warning, but in GUI mode.
        #graphical code goes here
        messagebox.showinfo("Done!", """Perfect, the part of the code that is still in development seems to not have crashed anything! If you like to submit issues that occurred, please go to "https://github.com/Stehlampe2020/PyPerfScore/issues" to report them.\n\n*End of Code*""")  # Congratulations! If you see that message the program didn't crash! 
        gui.destroy()   # Destroy (close) the window with the ID "gui" after "OK" has been clicked in the messagebox above. 
        print("""Perfect, the part of the code that is still in development seems to not have crashed anything! If you like to submit issues that occurred, please go to "https://github.com/Stehlampe2020/PyPerfScore/issues" to report them.\n*End of code*""")   # Congratulating also in command-line mode if (for some reason) the graphical message doesn't get displayed. 
        return 0    # Return a zero to signal the return value handler that everything went right. The return value handler will be added later. 
    
def ask_for_args():
    args = sys.argv
    if len(args) == 2:  # If two arguments are given, do one of the following things: 
        # The program name is also counted as an argument when using sys.argv to ask for the command-line arguments. 
        # Because computers are counting from zero up and not from one, we ask for argument 1 (which is the second argument in sys.argv) to get the first argument AFTER the program name. If we asked for the first argument we would get the program name but that doesn't interest us at all at the moment.
        if args[1] == "--gui":  # If the second argument is --gui we load the GUI:
            print("Loading GUI...")
            load_gui()
            return 0    # This time we didn't fail.
        elif args[1] == "--full-gui":   # If the second argument is --full-gui we load the GUI with the input value True for force_to_run to load even the unstable parts of the GUI. This option will be commented out as soon as I finish writing the GUI and the program gets into the release phase.
            print("Loading GUI...")
            load_gui(True)
            return 0    # This time we didn't fail.
        elif args[1] == "--cmdline":    # If the second argument is --cmdline we simply run the test in command-line mode. This option is useless for now but will be useful when I switch the default value for is_graphical  for run_test() from False to True. 
            print("Running in command-line mode...")
            run_test(False)
            return 0    # This time we didn't fail.
        else:
            print("""Incorrect argument used!\nThe only arguments that will be accepted are "--cmdline", "--gui" and "--full-gui".\n "--cmdline" will run this program in command-line mode, "--gui" will only load the parts of the GUI that are fully implemented by now and "--full-gui" will try to run the full GUI even though some parts may cause crashes.""")
            exit()
            return 2    # This time fe failed. Returning a 2 for "wrong argument".
    elif len(args) >= 3:    # Warn the user if too many arguments were used and the quit the program. 
        print("Too many arguments!\n(This program only takes one...)")
        exit()
        return 3    # This time we failed. Returning a 3 for "too many arguments were used".
    elif len(args) == 1:    # If there's only one argument given (the name of the program, like described in line 51 of the source code) we warn the user that no arguments (in the way we think of them when entering them) were detected and run the test in default mode. For now, that's command-line mode but that'll change later.
        print("""No command-line options were detected, running in default mode.\nIf you intended to run this program in graphical mode, press [Ctrl] + [C] now to cancel and re-run this program with the argument "--gui".""")
        run_test()
        return 0    # This time we didn't fail. We were just running in a pre-defines mode instead of a user-specified one.
    else:   # If somehow less than zero arguments (in the way we think of them when entering them) were detected we warn the user and ask to report the issue.
        print("An unknown error occurred while checking for command-line options, please report this behaviour and the conditions under which this error occurred!")
        return 4    # This time we failed. Returning a 4 for "unknown error while checking for command-line arguments".

try:
    import tkinter  # Try to import tkinter
except ImportError: # If importing tkinter fails: 
    print("""Importing module "tkinter" failed, you will only be able to run this program in command-line mode!""") # Print a little notify that tkinter could not be imported and the test will run in command-line mode. 
    try:
        run_test(False) # directly run the test in command-line mode without even checking for arguments because they are (at least for now) just to tell the program to run in graphical mode, which is impossible without tkinter. 
    except KeyboardInterrupt:
        print("\n[Ctrl]+[C] has been pressed, exiting...")  # Notify the user in command-line that [Ctrl]+[C] has been presseed so it's clear what made the program stop. 
        pass
else:
    try:     #If importing of tkinter doesn't fail, run the program in an own try-except-construct to easily handle KeyboardInterrupts: 
        from tkinter import *
        from tkinter import messagebox
        ask_for_args()  # Now, let's check for command-line arguments and run the program! (Running the test is done by ask_for_args().)
    except KeyboardInterrupt:   # If a KeyboardInterrupt occurrs: 
        print("\n[Ctrl]+[C] has been pressed, exiting...")  # Notify the user in command-line that [Ctrl]+[C] has been presseed so it's clear what made the program stop. 
        pass
