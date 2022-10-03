"""
Devorinoes - Brian Yang & Kevin Wang
SoftDev
k05 -- Parsing a csv and returning a random occupation based on percentages
2022-10-02
time spent: 1.5 hrs

Disco:
* Unpacking a return with multiple outputs can be done with return1, return2 = func(), where func returns two outputs
* str[::-1] reverses a string
* pprint to prettify while printing
* unpack key, value in a for loop using dict.items()

QCC:
* modularity is king
* how many times does it take to run a random algorithm to prove randomness?
* what is randomness?

HOW THIS SCRIPT WORKS:
1. First, it parses the csv into the dictionary by reading the csv and then seperating the occupation and percentage through the position of the last comma
2. Generate a random seed by doing random.random() and multiplying that by the total percentage (99.8)
3. Loop through each percentage and if the cumulative values of those percentages exceeds that of the random seed, then that occupation is selected
4. Test it by running it 50000 times and comparing the results to the original percentage
"""

import random
from pprint import pprint

def get_last_comma(str):
    #takes a sting and returns the index of the last comma (for use in parsing a csv)
    reversed_string = str[::-1]
    for index in range(len(reversed_string)):
        if reversed_string[index] == ",":
            return len(str) - index - 1
    return -1

def csv_to_dictionary():
    #takes a csv containing occupations and the % of people employed in them and converts it into a dict
    info = open("occupations.csv")
    lines = info.read().split("\n")

    occupation_to_percentage = {}
    for i in lines[1:-1]:
        last_comma = get_last_comma(i)
        occupation = i[:last_comma]
        percentage = i[last_comma + 1:]

        occupation_to_percentage[occupation] = float(percentage)

    total_line = lines[-1]
    total_line_comma = get_last_comma(total_line)
    total_percentage = float(total_line[total_line_comma + 1:])

    return occupation_to_percentage, total_percentage


def get_random_occupation():
    #finds a random occupation based on the % they appear
    occupation_to_percentage, total_percentage = csv_to_dictionary()
    random_seed = random.random() * total_percentage #0 inclusive - 99.8 exclusive 

    cumulative_value = 0
    for key, value in occupation_to_percentage.items():
        cumulative_value += value

        if cumulative_value > random_seed:
            return key


def test_random_occupation(times):
    #tests to make sure get_random_occupation is sufficiently random
    occupation_to_outcomes = {}
    for i in range(times):
        occupation = get_random_occupation()
        if occupation not in occupation_to_outcomes.keys():
            occupation_to_outcomes[occupation] = 0
        occupation_to_outcomes[occupation] += 1
    
    occupation_to_outcomes_percentages = {}
    for key, value in occupation_to_outcomes.items():
        occupation_to_outcomes_percentages[key] = value * 100 / times
        
    return occupation_to_outcomes_percentages

pprint(csv_to_dictionary())
pprint(test_random_occupation(50000))