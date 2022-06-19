from cgi import print_exception
from os import link
from unittest import result
from webbrowser import get
from bs4 import BeautifulSoup
import requests
import time

url = None
results = None
doc = None
li_tags = None

def get_title():
    refreshpage()
    #Grabs first LI element in carousel
    title_tags = li_tags.find(["h3"], class_="s-item__title").getText()
    #Formatting (Removes "New listing")
    item_title = title_tags.replace(title_tags[:11], '')
    return(item_title)

def get_price():
    refreshpage()
    #Grabs LI element's span tag containing price
    price_tags = li_tags.find(["span"], class_= "s-item__price")
    #Formatting for just dollar amount
    item_price = (price_tags.string)
    return(item_price)

def get_link():
    refreshpage()
    #Grabs LI element's a tag containing link
    link_tags = li_tags.find(["a"], class_= "s-item__link")
    #Formatting for just the link
    item_link = link_tags['href']
    return(item_link)

def refreshpage():
    #updates the global variables the functions pull from
    global url
    global results
    global doc
    global li_tags

    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=gamecube&_sacat=139973&LH_ItemCondition=1000&_sop=10"
    #Sends HTTP Request and stores results
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")
    #Grabs first item in carousel
    li_tags = doc.find(["li"], class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
