## What is newsreader? ##

Newsreader is a python script that fetches the RSS feeds from
IndianExpress for the latest news, uses espeak to read out loud that news feed.


    Voice used: mbrola-en1
    News courtesy: RSS feeds by IndianExpress


## Requirements ##

    espeak, mbrola and mbrola-en1 voice, pyttsx


## TODO ##

Run the install.sh file once before running the script to meet all
requirements. (this is a onetime run)

Finally run read_news.py each time you want to listen to the news or
follow the tip below.


## Tip ##

You can use crontab to schedule the newsreader to read news every hour.
First make the read_news.py executable by:

    chmod +x read_news.py

Then run the following command:

    EDITOR="gedit" crontab -e

And add the following line to that file and save.

     */60 * * * * /home/tejas/espeak.py

60 is for the news to be read every 60minutes.


## Created By ##

Tejas Bubane ( tejasbubane@gmail.com )

Any suggestions/bugs feel free to mail me or tweet @tejas_bubane.


## Licence ##

    Covered under GNU-GPL v3.0.
    NO WARRANTY IS PROVIDED.

More info at http://www.gnu.org/licenses/gpl.txt
