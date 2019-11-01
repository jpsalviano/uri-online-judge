from bs4 import BeautifulSoup

html = input('type html pathway: ') # http://morsecode.scphillips.com/morse2.html

with open(html) as f:
    soup = BeautifulSoup(f, features='html.parser')

morse = dict()

for t in soup.find_all(attrs={'class': 'tile morse'}):
    morse[t.text] = t.next_element.next_element.next_element.text
