"""
Brian Yang & Kevin Wang
SoftDev
k05 -- Parsing a txt file and putting devos' information into a dictionary called krewes
2022/9/28
time spent: 1 hr
Disco:
-Saving a text file creates a new line at the end
-You can put a list in a list
-open() and read() enables you to read over the file
-Indexing a 2d array
-You can return multiple things when using comma in a return
QCC:
-Why must we instaniate a list before appending?

OPS Summary:
parse_krewes
1. We took in a txt file and used split to seperate the different people, class period and ducky
2. Using a for loop to go through the information of the Devos and split them up into a list
3. Using append() we add a devo's information into the dictionary
4. We return the dictionary
"""

import random
import math

def parse_krewes():
    info = open('krewes.txt')
    str_file = info.read().replace('\n','').split('@@@')
    krewes = {}
    for i in str_file:
        temp_info = i.split('$$$')
        period = int(temp_info[0])
        name = temp_info[1]
        duckie = temp_info[2]
        if period not in krewes.keys():
            krewes[period] = []
        krewes[period].append([name, duckie])
    return krewes

krewes = parse_krewes()
print(krewes)


#takes a period and returns a random devo from that period
def randomDevoPeriod(period):
    if (period in krewes.keys()): #validates that the user input is actually an existing period
        devosFromPeriod = krewes[period] #array of devos
        index = math.floor(random.random() * len(devosFromPeriod)) #random index of devosFromPeriod

        return period, devosFromPeriod[index][0], devosFromPeriod[index][1]
    else:
        return None

print(randomDevoPeriod(7))

#returns a random devo across any period
def randomDevoOverall():
    #generate a random period using the same algorithm
    periods = list(krewes.keys())
    randomIndex = math.floor(random.random() * len(periods))
    randomPeriod = periods[randomIndex]
    #reuse randomDevoPeriod
    return randomDevoPeriod(randomPeriod)

print(randomDevoOverall())
