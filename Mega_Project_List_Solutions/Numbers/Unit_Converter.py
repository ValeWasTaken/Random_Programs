# Python 2.7
import urllib
import urlparse
from bs4 import BeautifulSoup

def calculate():
        conversion = raw_input("Conversion: ").replace(" ","+") # Stores conversion request in URL-acceptable form.
        url = ("http://www.wolframalpha.com/input/?i="+conversion)
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        try:
                dataChunk = (soup.findAll('div',{'class':"output pnt"})[1].contents[1]) # Web scrape of general chunk of data that contains answer.
                data = urlparse.parse_qs(urlparse.urlparse(str(dataChunk)).query) # Puts answer into dictionary listing under 'i' 
                print(data['i'][0]) # Answer in the form of "<number> <measurement>"
        except:
                print("Invalid input. Please try again. Example: '20 feet to inches' without the quotes is valid input.")
calculate()
