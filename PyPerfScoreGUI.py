if __name__ == "__main__":
    print("Please use PyPerfScore.py to start PyPerfScore!")
    raise SystemExit("PyPerfScoreGUI.py was run directly!")

try:
    with open("lang/preferred.ppslng") as langfile:
        strings = eval(langfile.read())[7]
except Exception as e:
    print("Error: could not import language into module PyPerfScoreGUI! (Error message: {error_message})".format(error_message=e))
    exit("failed_to_import_language")

try:
    import tkinter
except ImportError:
    print(strings[1][0])
    raise Exception(strings[1][0])

class definition():
    print(strings[2])
    exit(strings[3])
def generate_gui():
    main_window = tkinter.Tk()
    info_not_implemented_label = tkinter.Label(main_window, strings[4])
    info_not_implemented_label.place()
    return main_window
