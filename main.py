# this is the main file
# main.py was constructed completely bythe hehehaha developer

# this is not the full game this is a cli knockoff

# imports

from time import *
import random

# variebles


b = [practice()]

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
    if random.randint(1, 4) != 1:   # if it isint 1 do
        while mh > 0 & h > 0 :
            sleep(3)
            print("You beat the practice beast")
            upscore(500)
            print("Your score is " + sr = int(stxt.readline([1]))
    else
        print("haha you died")
        exit(1)

def beast():
    r = random.randint(1, 1)
    if r == 1:
        practice()
    #elif r == 2:


# main game code

print("Your score is " + sr = int(stxt.readline([1]))
sleep(2)
print("Hehehaha Developer forced you to fight the practice beast")
practice()