# Question : Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

# Answer :  

import math
N, M = map(int, input().split()) 
for i in range(0,math.floor(N/2)): 
    s='.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))
print ('WELCOME'.center(M,'-'))
for i in reversed(range(0,math.floor(N/2))): 
    s='.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))
