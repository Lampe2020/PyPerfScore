# What is "PyPerfScore" and how does it work? 
This is a little Python program that counts up from zero to 1,000,000 (that's the default value for `cycles`) as fast as the CPU allows. The program takes a timestamp before and after the `while` loop runs. When it finishes counting from zero to 1,000,000 the program subtracts the first timestamp from the second one to get the time the loop actually took to run through. Then it divides the amount of runs through the loop (the value of `cycles`) with the time it needed to complete.   
Before it exits it prints the resulting score to the screen, rounding the time it took to complete to three decimal points and the score to zero decimal points using the `round()` function so the user doesn't need to understand the big mass of numbers and just gets accurate but still easily understandable numbers to work with.   
And the rounding has another benefit: it makes probable measuring inaccuracies completely unimportant. 

# Future plans for developing this program:
I want to add a GUI using `tkinter` to make it more easily usable even for non-command-line users. 

# Why is there a difference between release tags and release titles? 
`pre-alpha` will be version `0.1.x`,   
`alpha` will be version `0.2.x`,   
`beta` will be version 0.3.x and   
after that we'll get versions `1.x.x`, `2.x.x`, and so on.   
   
The release tags contain the full version number and   
the release titles contain the title version (`v0.2.1-alpha` becomes `alpha-1.2` and so on) and then the full release name (`v0.2.1-alpha` becomes `(pps-0.2.1-alpha)`).

# Dependencies:
-> Python 3.5 or higher   
-> everything to run Python 3.5 or higher  
-> Python module `tkinter` (will only be tried to load if `--gui` or `--full-gui` command-line arguments are used)
   
# Example run of `pyperfscore-0.2.1-alpha`
sorry for the pixelating, that happened when converting the WebM video to GIF...   

An example run of the program on pretty bad hardware can be found below:   
![example_run_of_pyperfscore](https://user-images.githubusercontent.com/94976382/149187622-4e1974ee-e416-4722-aafb-ab3cd72e7574.gif#gh-dark-mode-only)
![example_run_of_pyperfscore](https://user-images.githubusercontent.com/94976382/149190990-7a03fbd0-1792-4692-a533-78c7ab118e83.gif#gh-light-mode-only)
   
OS: Linux Mint 20.3 Cinnamon   
(The Windows logo in the bottom left is just a screenshot of the real Windows7 start button, put down there as an image)

# Usage
*In the examples below I used the installed version, you will have to use the command to start your copy instead of `pyperfscore`, if you don't have it installed as `pyperfscore`!*    

|Command|Description|
|-------|-----------|
|`~$ `|This represents your terminals input prompt.|
|||
|`~$ pyperfscore`|This will run the program in default mode, which is (for now) the command-line mode.|
|`~$ pyperfscore --cmdline`|Explicitly run the program in command-line mode.|
|`~$ pyperfscore --gui`|Explicitly run the program in GUI mode. *Note: This will run the program in command-line mode and just show a little warning in the GUI until the GUI is implemented usably and free of bugs.*|
|`~$ pyperfscore --full-gui`|Force-load the full GUI (as far as it's implemented) and not run the test in command-line mode at all. *Note: this option will later be disabled, as soon as the GUI is fully bug-free.*|
|||
|`~$ pyperfscore --cmdline --debug`|Explicitly run the program in command-line mode. Go into an interactive shell on EOF or errors.|
|`~$ pyperfscore --gui --debug`|Explicitly run the program in GUI mode. Go into an interactive shell on EOF or errors.|
|`~$ pyperfscore --full-gui --debug`|Force-load the full GUI (as far as it's implemented) and not run the test in command-line mode at all. Go into an interactive shell on EOF or errors. *Note: `--full-gui` will later be disabled, as soon as the GUI is fully bug-free.*|
