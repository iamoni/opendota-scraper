# opendota-scraper

A simple scraper pulling information from OpenDota API's match/matchid endpoint, and storing the results in a MongoDB database.

The scraper consists of a sample generator, which  produces an interval of matches between 2 and 4 hours old. The actual scraper then generates random matchids in the interval, checks to make sure there are no duplicates, and then pulls the result from the API. If the match actually exists, the result is added to the database. The two parts (interval generator and scraper) run separately, to allow one to change details about the scraper without interrupting the generator, which should pretty much run constantly. 

The scraper respects the API's rate limit.

To use, simply pull the repo and run generator.py and scraper.py. Keep in mind it'll be four hours before the generator produces the right match intervals. Make sure you have mongodb installed on the machine running the scraper, and if needed, edit the connection details as neccessary.

Keep in mind that I'm new to programming so there might be things that don't work right, or at all, but my results so far seem fine.
