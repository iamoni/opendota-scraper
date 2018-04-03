
import numpy as np
import time
import pymongo
import logging
from functions import *

logging.basicConfig(filename='error.log', level=logging.ERROR)

# connect to MongoDB
conn = pymongo.MongoClient()
db = conn.local
dota = db.dota

# load a list of already parsed matches
match_list = np.load('match_list.npy')


# actual scraping function 
def scrape_loop():
    mt = read_matches()
    rand_match = gen_match(mt[0], mt[1], match_list)
    match_resp = getmatch(rand_match)
    if len(match_resp)!=1:
        dota.insert_one(match_resp)
        np.append(match_list, match_resp)
        time.sleep(0.4)
        logging.debug(f'{time.ctime()} Added match {rand_match} to database')
    else:
        time.sleep(0.4)
        logging.debug(f'{time.ctime()} Skipped empty match {rand_match}')



# scrape loop, includes some extremely basic error handling and logging,
# also saves the matches list to disk every now and then
x = 0
while True:
    try:
        scrape_loop()
        x += 1
        if x >= 3600:
            np.save('match_list.npy', match_list)
            logging.debug('saved match_list numpy array to disk')
            x = 0

    except Exception as e:
        logging.error(f'{time.ctime()} EXCEPTION: {e}')
        np.save('match_list.npy', match_list)
        time.sleep(600)
