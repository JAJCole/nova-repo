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


# incomplete fx for financial times
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



'''    
# new FT fx for article content
def FT_sleuth_():
    target = request.get('https://www.ft.com/markets?segmentID=361c623d-11ab-afbb-414a-568dafa8307d&gad_source=1&gclid=Cj0KCQjwhtWvBhD9ARIsAOP0GohdvoM7tCZRwiwhzGyUk250dFid84ybX-sR-TQO65GprC13zN-gP0YaAhenEALw_wcB&gclsrc=aw.ds')
    info = bs4.BeautifulSoup(target.content, 'lxml')
    buzzwords = ['critical', 'record', 'shock', 'expect','low','high']
    query = info.find_all('a',class_ = "js-teaser-heading-link")
    for element in query:
        title = element.text.lower()
        if any(word in title for word in buzzwords):
            article_url = 'https://www.ft.com'+ element['href']
            article_target = request.get(article_url)
            article_info = bs4.BeautifulSoup(article_target.content, 'lxml')
            article_content = article_info.find('div',class_='article-content').text.strip()
            if not os.path.exists('Financial_Times_Hits'):
                os.makedirs('Financial_Times_Hits')
            with open('Financial_Times_Hits/hits.txt', 'a') as ft:
                ft.write(f"Title: {title}\nURL: {article_url}\nContent:\n{article_content}\n\n")
## current error in above block from no exception handling with paywalled article urls
'''
'''
# perp-run and interval
if __name__ == '__main__':
    while True:
        FT_sleuth_()
        time.sleep(10)
'''

# RT fx for aerospace and defense
def RT_sleuth():
    target = request.get('https://www.reuters.com/business/aerospace-defense/')
    info = bs4.BeautifulSoup(target.content, 'lxml')
    buzzwords = ['critical', 'record', 'shock', 'expect','low','high','merger', 'obtained', 'scandal', 'SpaceX', 'regulator']
    query = info.find_all('a', class_='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P media-story-card__headline__tFMEu')
    if not os.path.exists('Reuters_Hits'):
        os.makedirs('Reuters_Hits')
    with open('Reuters_Hits/hits.txt', 'a') as ft:
        for element in query:
            title = element.text.lower()
            if any(word in title for word in buzzwords):
                article_url = 'https://www.reuters.com'+ element['href']
                article_target = request.get(article_url)
                article_info = bs4.BeautifulSoup(article_target.content, 'lxml')
                article_content = ''
                for div in article_info.find_all('div'):
                    article_content += div.text.strip() + "\n"
                ft.write(f"Title: {title}\nURL: {article_url}\nContent:\n{article_content}\n\n")
# the above block needs its buzzwords tweaked as well as program timeout.
# search elements once then stop, not continue searching until a buzzword is found.
                
'''
if __name__ == '__main__':
    while True:
        RT_sleuth()
        time.sleep(100)
'''