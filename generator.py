
import time

from matchid_gen import sample_maker

while True:
    try:
        sample_maker()
    except:
        time.sleep(360)
