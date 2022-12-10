import os
from time import sleep
import cursor
import sys
import time
from colorama import Fore,Style,Back
import random
import pytimedinput
from pyfiglet import Figlet



#Pyfiglet Font
f = Figlet(font='braced')

#DEV TOOLS

dev =True

# Starting date for the game
startingDate = 'November 14, 1848'

# Clear the console screen
def clear():
    """Clears the terminal screen."""
    # For Windows
    if os.name == "nt":
        os.system("cls")

    # For Linux and MacOS
    else:
        os.system("clear")

# Function used for development purposes
def buffer():
    if dev == True:
        input('DEVBUF: ')
        return
    else:
        return

# Initialize the game by clearing the screen
clear()

world = {"towns":{}}


#Player Class

class Player():
    def __init__(self,passengers,gold):
        self.gold = gold
        self.passengers = passengers

#Get's key input using the pytimedinput module

def getkey(text = '',timeout = -1):
    key,timeout = pytimedinput.timedKey(text,timeout = timeout,allowCharacters="yn")
    return key

#gets a random list of town names

def getRandomTowns(amount = 1):
    f = open('townNames.txt','r')
    townNames = f.readlines()
    f.close()
    ts = []
    for x in range(amount):
        t = random.choice(townNames)
        t = t.strip('\n')
        ts.append(t)
    return ts





#press Enter to continue function

def pressEnter():
    cursor.hide()
    scrollTxt('Press enter to continue')
    input()
    cursor.show()
    return

#Writes to the console character by character to add a cool effect

def scrollTxt(text, delay=0.02, light=False):
    cursor.hide()

    if light is False:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print("")
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print("")

    cursor.show()

# Reads a file and returns the lines

def read_file(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    return lines

#Loads the Oregon Part of the text and pastes it

def printOregon():
    lines = read_file('OREGON.txt')
    print(''.join(lines))

#Loads the Trail Part of the text and pastes it

def printTrail():
    lines = read_file('TRAIL.txt')
    print(''.join(lines))

#Print's the ascii Town

def printTown():
    lines = read_file('asciiTown.txt')
    print(''.join(lines))
def printTownName(townName):
    print(f.renderText(townName))


def showTown(townName):
    printTownName(townName)
    printTown()

#Title screen

def ShowTitleScreen():
    printOregon()
    sleep(1)

    printTrail()
    sleep(0.5)
    scrollTxt('By: Timeman1111',delay = 0.05)
    pressEnter()


#What loads in when you start the game

def startingScreen():
    if dev == False:
        cursor.hide()
        ShowTitleScreen()
        cursor.show()

    else:

        return


#Generates a seed and asks user if they want to change it

def getSeed():
    global seed
    seed = random.randrange(1,1000000)

    scrollTxt(f'SEED: {str(seed)}\n')

    scrollTxt('This is the world seed\n',delay = 0.01)

    scrollTxt('Do you wish to change it? [y/n]',delay  = 0.01)

    cursor.hide()

    user = getkey()

    cursor.show()
    clear()
    if user == 'y':

        scrollTxt('Enter new seed\n',delay = 0.01)
        seed = input('New seed: ')

    clear()

    return seed

#Generates world (towns, money status, etc.)

def generateWorld():
    #Grabs seed from the seed function
    seed = getSeed()
    random.seed(seed)

    #Generate the amount of towns
    amountOfTowns = 1 * random.randrange(5,10)

    amountOfTowns = getRandomTowns(amountOfTowns)


    for x in amountOfTowns:
        dangerous = random.randrange(1,4)
        shopName = random.choice(['Bokki','Hither','No'])
        world['towns'][x] = {"dangerous": dangerous,"shopName":shopName}


    amountOfPeople = 1 * random.randrange(2,4)
    player = Player(amountOfPeople,500)
    clear()
    showTown(random.choice(list(world['towns'].keys())))
    buffer()

    
    
#Main runtime

def main():
    startingScreen()
    clear()
    generateWorld()


main()