if __name__ == '__main__':
    print('Please use PyPerfScore.py to start PyPerfScore!')
    raise SystemExit('PyPerfScoreGUI.py was run directly!')

try:
    with open('lang/preferred.ppslng') as langfile:
        strings = eval(langfile.read())[7]
except Exception as e:
    print(f'Error: could not import language into module PyPerfScoreGUI! ({type(e).__name__}: {e})')
    exit('failed_to_import_language')

try:
    import gi
    gi.require_version('Gtk', '4.0')
    from gi.repository import Gtk
except ImportError:
    print(strings[1][0])
    raise Exception(strings[1][0])

class definition():
    print(strings[2])
    exit(strings[3])
def generate_gui():
    
    return False
