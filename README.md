## What is newsreader? ##

Newsreader is a python script that fetches the RSS feeds from IndianExpress for the latest news,
uses espeak to read out loud that news feed.

    Voice used: mbrola-en1
    News courtesy: RSS feeds by IndianExpress


## Requirements ##

espeak, mbrola and mbrola-en1 voice, pyttsx

Run the install.sh file once before running the script to meet all requirements.

## Tip ##

You can use crontab to schedule the newsreader to read news every hour.
run the following command:

    EDITOR="gedit" crontab -e

Then add the following line to that file and save.

     */60 * * * * /home/tejas/espeak.py

60 is for the news to be read every 60minutes.


## Licence ##

Covered under GNU-GPL v3.0.
NO WARRANTY IS PROVIDED.
More info at http://www.gnu.org/licenses/gpl.txt
