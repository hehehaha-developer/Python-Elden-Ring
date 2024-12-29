# this is the main file
# main.py was constructed completely bythe hehehaha developer

# this is not the full game this is a cli knockoff

# imports

from time import *
import random

# variebles

sr = " "    # score read from file
s = 0       # score

h = 1000   # health
mh = 0     # monsters health
ma = 0     # monsters attack

r = 0    # ranndom var

stxt = open("score.txt" , "a")    # score data file


# function definitions
    

def upscore(n):    # adding the n value to the score
    sr = int(stxt.readline([1]))
    sr = sr + n
    stxt.write(sr) # update the score

def practice():    # practice monster
    print("practice beast approches")
    mh = 500         # set monsters health
    ma = 50          # monters attack
    if random.randint(1, 4) != 1:   # if it isint 1 do
        while mh > 0 & h > 0 :
            sleep(3)
            print("You beat the practice beast")    # when the beast is beat 
            upscore(500)
            print("Your score is " + str(stxt.readline([1])))   # add score
    else:
        print("haha you died")  # kill beast
        exit(1)

def supersmall():
    print("supersmall")
    ma = random.randint(5, 100)
    h = h - ma
    if h <= 0:
        print("well you had a good run. See you in heaven")
        exit(1) 

def small():
    print("small")
    ma = random.randint(20, 170)
    h = h - ma
    if h <= 0:
        print("Wahahahahah i small beast killed the great warrior")
        exit(1) 

def beast():
    r = random.randint(1, 3)
    if r == 1:
        practice()

    elif r == 2:
        supersmall()

    elif r == 3:
        small()


# main game code 

sleep(2)
print("Hehehaha Developer forced you to fight the practice beast")
practice()
while h > 0:
    sleep(int(random.randint(1, 10)))
    beast()

exit(1)