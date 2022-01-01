# PyPerfScore
This is a little Python 3.7 (or could also be 3.9...) program that's supposed to spit out a number that's rapidly changing and the suddenly freezes. That's the computing speed score for your computer at that time. I will release a list of scores as soon as this little program behaves properly. 

# How this program works: 
This program counts up by +1 steps as fast as it can and every fourth of a second it subtracts 10000. The number it has at the moment is immeadiately shown on screen and the program stops after *runs_max* times counting up. The number that's in the variable *number* at that moment is printed to the screen and then the program exits. 
