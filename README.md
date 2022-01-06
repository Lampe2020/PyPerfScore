# What is "PyPerfScore" and how does it work? 
This is a little Python program that's supposed to cout up from zero to 1,000,000 (that's the default value for *max_runs*) as fast as the CPU allows. The program takes a timestamp before and after the *while* loop finishes counting from zero to 1,000,000 and after that the program subtracts the first timestamp from the second one to get the time the loop actually took to run through. Then it divides the amount of runs through the loop (the value of *runs_max*) with the time it needed to complete.   
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
-> Python module *tkinter* (will only be tried to load if "--load-gui" or "--force-gui" command-line arguments are activated)
