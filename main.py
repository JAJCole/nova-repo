# NOVA MAIN

import os
import bs4
import requests as request
import time

### Web scraping function
'''def sleuth(url):
    # GET request
    target = request.get(url)
    # Parse HTML
    info = bs4.BeautifulSoup(target.content, 'lxml')
    # Extract relevant information
    # scraping here
    return scraped_data
'''

#target = request.get('https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds')
'''addresses:
FT: https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds
WSJ (energy): https://www.wsj.com/business/energy-oil?mod=nav_top_subsection 
'''
#info = bs4.BeautifulSoup(target.content, 'lxml')
#buzzwords = ['critical', 'record', 'shock', 'expect','low','high']
'''
FT tags: <a class="js-teaser-heading-link"
        data-trackable="heading-link"
'''

#query = info.find_all('a',class_ = "js-teaser-heading-link")
#print(query)
#spec_query = query.find('a', class_= )

#for element in query:
#    text = element.text.lower()
#    if any(word in text for word in buzzwords):
#        print(text)


def FT_sleuth():
    target = request.get('https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds')
    info = bs4.BeautifulSoup(target.content, 'lxml')
    buzzwords = ['critical', 'record', 'shock', 'expect','low','high']
    query = info.find_all('a',class_ = "js-teaser-heading-link")
    for element in query:
        text = element.text.lower()
        if any(word in text for word in buzzwords):
            if not os.path.exists('Financial_Times_Hits'):
                os.makedirs('Financial_Times_Hits')
            with open('Financial_Times_Hits/hits.txt', 'a') as ft:
                ft.write(text + '\n')


if __name__ == '__main__':
    while True:
        FT_sleuth()
        time.sleep(999)

    
