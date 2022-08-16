#!/usr/bin/python3
# -*- encoding: utf-8 -*-

if __name__ != "__main__":
    print("Please don't import PyPerfScore into other programs!")
    completion_status = "cancelled"
    exit("{}\n{}".format(completion_status, None))

# ------------------------------ Initialization begin ------------------------------
try:
    with open("ver") as version_file:
        version = version_file.read().strip()
except OSError:
    print("Could not get own version! Setting to 0.0.0...")
    version = "0.0.0"
release_type = "alpha"
update_nickname = "Complete recode update"

try:
    with open("lang/preferred.ppslng") as langfile:
        strings = eval(langfile.read())
        if type(strings) != dict:
            raise SyntaxError("Tried to import a faulty language file into PyPerfScore!")
        if strings["ppsver"] != version:
            print(strings["ppsver_warning"].format(strings["ppsver"], version))
        language_string = strings["language_string"]
        lang = strings["language"]
except Exception as e:
    print("Error: could not import language! (Error message: {error_message})".format(error_message=e))
    exit("failed_to_import_language")
else:
    print(strings[0].format(language_string, lang))

cycles = 100000000 # This number is the number the program counts up to. If you increase this value the score is more accurate, if you decrease this value the score is less accurate.

completion_status = None # This definition is only for avoiding tracebacks with the last line of code. (which returns the completion_status and the score to the interpreter/os)
score = None # This definition is only for avoiding tracebacks with the last line of code. (which returns the completion_status and the score to the interpreter/os)

try:
    import os
    import sys
    import time
    import traceback
    
    args = sys.argv # This is just there to make the name shorter.
    
    core_count = len(os.sched_getaffinity(0))
    
    def argument(argument_to_search_for):
        return argument_to_search_for in args

    def exists(var):
        if var != "":
            try:
                eval(var)
                return True
            except NameError:
                return False
        elif var == "":
            return False

    def build_version_string():
        if update_nickname:
            version_string = "v{}-{} - {}".format(version, release_type, update_nickname)
        else:
            version_string = "v{}-{}".format(version, release_type)
        return strings[1].format(version_string)
    
    print(build_version_string())
    
    if argument("--update"):
        completion_status = "update"
        args.remove("--update")
        import ppsupdater
        if argument("--exit"):
            exit()

    class debug():
        def __init__(self):
            print(strings[11])
            pass
        """ String-commented out because exec(<expression>) (in difference to eval(<expression>)) can interpret keywords:
        # Definition of the keyword replacements for the minishell:
        # <var1> in <var2>
        def contains(to_search_through, to_search_for):
            return to_search_for in to_search_through
        
        # raise <exception>
        def raise_exception(exception = Exception):
            raise exception
        
        # <value_1> == <value_2>
        def is_equal(value_1, value_2):
            return value_1 == value_2
        
        # <value_1> != <value_2>
        def is_unequal(value_1, value_2):
            return value_1 != value_2
        """
        
        # Traceback functions:
        def last_traceback():
            return traceback.format_exc()
        
        def print_last_traceback():
            print(debug.last_traceback())
        
        # Set the number of cycles the test loop should take:
        def set_cycles(number = 10000000): # The value for number set here is just the default and only gets applied when calling debug.set_cycles() without a number.
            global cycles
            cycles = number
            return cycles
        
        # The debug minishell:
        def minishell(fail_status = "", advanced_minishell = False):
            if not advanced_minishell in (True, False):
                print(strings[3][0].format(advanced_minishell, type(advanced_minishell)))
                return
            def help():
                help_text_raw = strings[3][1]
                if advanced_minishell:
                    print(help_text_raw.format(strings[3][2], strings[3][3]))
                elif not advanced_minishell:
                    return help_text_raw.format("", strings[3][4])
            if fail_status == "failed":
                print(strings[3][5])
            elif fail_status == "cancelled":
                print(strings[3][6])
            elif fail_status == "finished":
                print(strings[3][7])
            elif fail_status == "switching_shells":
                print(strings[3][8])
            elif fail_status == "":
                print(strings[3][9])
            else:
                print(strings[3][10].format(fail_status, type(fail_status)))
            
            print(strings[3][11])
            while True:
                pyperfscore_debug_minishell_user_input = ""
                try:
                    if advanced_minishell:
                        pyperfscore_debug_minishell_user_input = input("PyPerfScore (ams)> ") # I use this long name for the input to avoid colliding with the user's inputs.
                    elif not advanced_minishell:
                        pyperfscore_debug_minishell_user_input = input("PyPerfScore> ") # I use this long name for the input to avoid colliding with the user's inputs.
                    if pyperfscore_debug_minishell_user_input not in ("", "exit()"): # If the entered command is not handled by debug.minishell():
                        if advanced_minishell:
                            exec(pyperfscore_debug_minishell_user_input) # I don't use the print() function here because exec(<expression>) function doesn't seem to return anything.
                        elif not advanced_minishell:
                            print(eval(pyperfscore_debug_minishell_user_input))
                    elif pyperfscore_debug_minishell_user_input == "exit()":
                        print(strings[3][12])
                        return
                except KeyboardInterrupt:
                    print(strings[3][13].format("KeyboardInterrupt", strings[3][12]))
                    return
                except SystemExit:
                    print(strings[3][14].format("SystemExit", strings[3][12]))
                    return
                except Exception:
                    if pyperfscore_debug_minishell_user_input != "":
                        if pyperfscore_debug_minishell_user_input != "exit()":
                            debug.print_last_traceback()
                        elif pyperfscore_debug_minishell_user_input == "exit()":
                            print(strings[3][12])
                            return
                    elif pyperfscore_debug_minishell_user_input == "":
                        print("\n{}".format(strings[3][12]))
                        return

    class multithreading():
        corecount = len(os.sched_getaffinity(0))
        def run(corecount):
            print(strings[4][0])

    # ------------------------------ Initialization end ------------------------------

    if len(args) == 1:
        print(strings[5][0])
    elif len(args) == 2 and argument("--debug"):
        print(strings[5][1])
    
    if argument("--gui"):
        import PyPerfScoreGUI as gui
    """
    New run plan:
    if argument("--gui") or argument("gui")
        try:
            import gui
            main_window = gui.PyPerfScoreGUI(full = argument("--gui-alpha-features"))
            run_test(main_window)
        except ModuleNotFoundError:
            print("Das GUI-Modul wurde nicht gefunden!")
    else:
        run_test(graphical=False)
    """
    
    def test_nogui(core_count = 1):
        # cycles = 10000000 # This is the default value. The actual definition of the value is at the top of this file for debug purposes.
        def generate_load():
            cycles_passed = 0
            test_percentage = 0
            print("{}...   ".format(strings[6][0]), end="\r")
            while cycles_passed <= cycles:
                test_percentage_before = test_percentage
                test_percentage = round((cycles_passed / 100) / (cycles / 100) * 100, 1)
                if test_percentage != test_percentage_before:
                    print("{}: {}%   ".format(strings[6][0], test_percentage), end="\r")
                cycles_passed += 1
        time_at_start = time.time() # Take a timestamp.
        if core_count == 1:
            generate_load()
#         elif core_count <= 2:
#             # Two core test.
#         elif core_count <= 4:
#             # Four core test.
#         elif core_count <= 8:
#             # Eight core test.
#         elif core_count <= 16:
#             # Sixteen core test.
        time_to_complete = time.time() - time_at_start # Subtract the first timestamp off the time now to get the time in seconds the counting took. 
        print(strings[6][1].format(round(time_to_complete, 3), cycles))
        try:
            global score
            score = cycles / time_to_complete # Calculate the score: divide the time the counting took by the number of cycles that the loop was run. 
        except DivisionByZero:
            print(strings[8][0].format(cycles))
        print(strings[6][2].format(round(score))) # Print the score in a nice form and rounded to a whole number to the terminal.
        return score
    
    def run_test(is_graphical = argument("--gui"), force_gui = argument("--gui-alpha-features")):
        if is_graphical:
            print(strings[7][0])
            gui_main_window = gui.generate_gui()
        elif not is_graphical:
            if not argument("--singlecore") and not argument("--multicore"):
                print(strings[4][1])
                test_nogui()
            elif argument("--singlecore"):
                test_nogui(1)
            elif argument("--multicore"):
                print(strings[4][2])
                return test_nogui() # Give test_nogui() as argument the number of available cores.
    
    run_test()
    
    completion_status = "finished" # This definition will not be reached in case of a Traceback above, so here's no need for an if statement.
except ImportError:
    print(strings[8][1])
    debug.print_last_traceback()
    completion_status = "failed"
except KeyboardInterrupt:
    print("\r{}".format(strings[8][2]))
    completion_status = "cancelled"
except SystemExit as e:
    print(strings[8][3].format(e))
    # debug.print_last_traceback()
    if argument("--debug"):
        print("\n{}".format(strings[3][14]))
    completion_status = "cancelled"
    sys.exit()
except Exception as e:
    print(strings[8][4].format(type(e).__name__, e))
    # debug.print_last_traceback()
    completion_status = "failed"
finally:
    if argument("--debug"):
        debug.minishell(completion_status)
    print(strings[9])
    exit("{}\n{}".format(completion_status, score))
