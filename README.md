# What is "PyPerfScore" and how does it work? 
This is a little Python program that's supposed to count up from zero to 1,000,000 (that's the default value for *max_runs*) as fast as the CPU allows. The program takes a timestamp before and after the *while* loop runs. When it finishes counting from zero to 1,000,000 the program subtracts the first timestamp from the second one to get the time the loop actually took to run through. Then it divides the amount of runs through the loop (the value of *runs_max*) with the time it needed to complete.   
Before it exits it prints the resulting score to the screen, rounding the time it took to complete to three decimal points and the score to zero decimal points using the *round()* function so the user doesn't need to understand the big mass of numbers and just gets accurate but still easily understandable numbers to work with.   
And the rounding has another benefit: it makes the measuring insccuracy completely unimportant. 

# Future plans for developing this program:
I want to add a GUI using *tkinter* to make it more easily usable even for non-command-line users. 

# Why is there a difference between release tags and release titles? 
pre-alpha will be version 0.1.x, 
alpha will be version 0.2.x, 
beta will be version 0.3.x and
after that we'll get versions 1.x.x, 2.x.x, and so on. 

# Dependencies:
-> Python 3.5 or higher   
-> everything to run Python 3.5 or higher  
-> Python module *tkinter* (will only be tried to load if "--load-gui" or "--force-gui" command-line arguments are used)
   
# Example run of pyperfscore-0.2.1-alpha
sorry for the pixelating, that happened when converting the WebM video to GIF...   

An example run of the program on pretty bad hardware can be found below:   
![example_run_of_pyperfscore](https://user-images.githubusercontent.com/94976382/149187622-4e1974ee-e416-4722-aafb-ab3cd72e7574.gif#gh-dark-mode-only)
![example_run_of_pyperfscore](https://user-images.githubusercontent.com/94976382/149190990-7a03fbd0-1792-4692-a533-78c7ab118e83.gif#gh-light-mode-only)
   
OS: Linux Mint 20.3 Cinnamon   
(The Windows logo in the bottom left is just a screenshot of the real Windows7 start button, put down there as an image)
