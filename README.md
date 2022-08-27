*Because not every bugfix or README.md change will result in a version change it may be good to delete the file `ver` after downloading and then running the updater. This is not required with the installer, only with the manual download from the "Releases" page.*

# What is "PyPerfScore" and how does it work? 
This is a little Python program that counts up from zero to 100,000,000 (that's the default value for `cycles`) as fast as the CPU allows. The program takes a timestamp before and after the `while` loop runs. When it finishes counting from zero to 1,000,000 the program subtracts the first timestamp from the second one to get the time the loop actually took to run through. Then it divides the amount of runs through the loop (the value of `cycles`) with the time it needed to complete.   
Before it exits it prints the resulting score to the screen, rounding the time it took to complete to three decimal points and the score to zero decimal points so the user doesn't need to understand the big mass of numbers and just gets accurate but still easily understandable numbers to work with.   
And the rounding has another benefit: it makes probable measuring inaccuracies mostly unimportant. 

# Future plans for developing this program:
* Section moved to [ToDo.md](ToDo.md)
   
# Dependencies:
-> Python 3.8 or higher (lower versions may cause bugs that I don't support!)   
-> everything to run Python 3.8 or higher  
-> Python module `tkinter` (will only be tried to load if `--gui` or `--full-gui` command-line arguments are used)
   
# Usage
*In the examples below the command is simplified, you will have to use `./PyPerfScore.py` instead of `pyperfscore` and `./ppsupdater.py` instead of `ppsupdater`, from the directory PyPerfScore was installed in!*    

|Command|Description|
|-------|-----------|
|`~$ `|This represents your terminals input prompt.|
|||
|`~$ pyperfscore`|This will run the program in default mode, which is (for now) the command-line mode.|
|`~$ pyperfscore --help`|This will display the version of PyPerfScore you have installed and the help text and then exit.|
|`~$ pyperfscore --cmdline`|Explicitly run the program in command-line mode.|
|`~$ pyperfscore --gui`|Explicitly run the program in GUI mode. *Note: This option isn't currently implemented and will fail on run.*|
|`~$ pyperfscore --update`|Tell PyPerfScore to check for the newest version and install it if possible. Run the test if no update happened.|
|`~$ pyperfscore --update --exit`|Tell PyPerfScore to check for the newest version and install it if possible. NOT run the test after checking for updates.|
|*The following two options can be used together:*||
|`~$ ppsupdater --ver=v0.0.0-version`|This will install the version `v0.0.0-version` instead of the latest version (if possible, otherwise it will show an error message and quit).|
|`~$ ppsupdater --path=/path/to/existing/directory`|This will install the update in `/path/to/existing/directory` instead of overwriting the current installation with the new one.|
