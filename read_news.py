import pyttsx
import urllib2
from xml.dom import minidom

engine = pyttsx.init("espeak", False)
engine.setProperty('voice', 'mb-en1')
engine.setProperty('rate', 130)
engine.say("Hello. News of the Hour")

page = urllib2.urlopen("http://syndication.indianexpress.com/rss/latest-news.xml").read()
news = minidom.parseString(page)

items = news.getElementsByTagName("item")

for item in items:
    title = item.childNodes[1].childNodes[0].nodeValue
    description = item.childNodes[-2].childNodes[0].nodeValue
    engine.say(title)
    engine.say(description)
engine.runAndWait()
