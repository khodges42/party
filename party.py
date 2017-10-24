import urllib2 , random
from bs4 import BeautifulSoup

print (random.choice((BeautifulSoup((urllib2.urlopen("https://twitter.com/AndrewWK")).read())).findAll('p', 'js-tweet-text')).get_text().encode("utf-8"))
