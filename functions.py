
import requests
import random
import numpy as np


# reads the text file generated by the match sample generator
# returns the two interval edge matches
def read_matches():
    with open('matches.txt', 'r') as f:
        f1 = f.read()
        f1 = f1.split(',')
        m1 = int(f1[0])
        m2 = int(f1[1])
        return m1, m2


# generates random match ids within a specific interval
# also takes a numpy array as arguments, checks if the match is in the
# array and appends the random match to the list
def gen_match(m1, m2, match_list):
    match = random.randint(m1, m2)
    if match not in match_list:
        return match
    else:
        gen_match(m1, m2, match_list)


# gets a specific match's json response
def getmatch(matchid):
    req_url = f'https://api.opendota.com/api/matches/{matchid}'
    response = requests.get(req_url).json()
    return response
