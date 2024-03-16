# NOVA MAIN

import bs4
import requests as request
import time


target = request.get('https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds')
'''addresses:
FT: https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds
WSJ (energy): https://www.wsj.com/business/energy-oil?mod=nav_top_subsection 
'''
info = bs4.BeautifulSoup(target.content, 'lxml')
buzzwords = ['critical', 'record', 'shock', 'expect','low','high']
'''
FT tags: <a class="js-teaser-heading-link"
        data-trackable="heading-link"
'''

query = info.find_all('a',class_ = "js-teaser-heading-link")
#print(query)
#spec_query = query.find('a', class_= )

for element in query:
    text = element.text.lower()
    if any(word in text for word in buzzwords):
        print(text)