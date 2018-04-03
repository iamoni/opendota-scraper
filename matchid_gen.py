
import requests
import time


# generates a recent match_id
def matchid_sample():
    publist_endpoint = 'https://api.opendota.com/api/publicMatches'
    result = requests.get(publist_endpoint).json()
    current_match = result[1]['match_id']
    return current_match


# creates a text file containing the match_ids
# from the edges of an interval between +2h and +4h
def sample_maker():
    result1 = matchid_sample()
    time.sleep(7200)
    result2 = matchid_sample()
    time.sleep(7200)
    write_me = str(result1) + ',' + str(result2)
    with open('matches.txt', 'w') as f:
        f.write(write_me)
