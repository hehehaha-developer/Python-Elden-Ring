# this is the main file
# main.py was constructed completely bythe hehehaha developer

# this is not the full game this is a cli knockoff

# imports

from time import *

# variebles


sr = " "    # score read from file
s = 0       # score

h = 1000   # health
mh = 0     # monsters health
ma = 0     # monsters attack

stxt = open("score.txt" , "a")    # score data file


# function definitions


def upscore(n):    # adding the n value to the score
    sr = int(stxt.readline([1]))
    sr = sr + n
    stxt.write(sr) # update the score

def practice():    # practice monster
    mh = 500         # set monsters health
    ma = 50          # monters attack
    while mh > 0 & h > 0 :
        


# main game code

