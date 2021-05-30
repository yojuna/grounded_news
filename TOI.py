import requests
import bs4
import pandas as pd
import time
import re

url = "https://timesofindia.indiatimes.com/home/headlines"


response = requests.get(url)
soup = bs4.BeautifulSoup(response.content)

soup2 = soup.find_all('div', {'id':'c_headlines_wdt_1', 'class':''})[0]
prev = "https://timesofindia.indiatimes.com/"
title_link_top = {line.find('a')['title']: prev + line.find('a')['href']
              for line in soup2.find('div', {'class':'top-newslist'}).find_all('li')}

title_link_other = {line.find('a')['title']: prev + line.find('a')['href']
              for line in soup2.find('div', {'class':'headlines-list'}).find_all('li')}

headlines = pd.DataFrame(list(title_link_top.items()),columns = ['title','link'])\
.append(pd.DataFrame(list(title_link_other.items()),columns = ['title','link']))\
.reset_index().drop(['index'], axis = 1)

def get_body(link):
    body = ''
    response = requests.get(link)
    soup_body = bs4.BeautifulSoup(response.content)
    for br in soup_body.findAll('br'):
        next_s = br.nextSibling
        if not (next_s and isinstance(next_s,bs4.NavigableString)):
            continue
        next2_s = next_s.nextSibling
        if next2_s and isinstance(next2_s,bs4.Tag) and next2_s.name == 'br':
            text = str(next_s).strip()
            if text:
                body += text
    return body

headlines['body'] = headlines['link'].map(lambda x:get_body(x))

print(headlines)