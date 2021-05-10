from newsapi import NewsApiClient
from pprint import pprint
from time import time

print('1 ', time())
# Init
newsapi = NewsApiClient(api_key='7b531272b6d54f2083b7ad07d7d8ce8e')

# /v2/top-headlines
print('2 ', time())
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')
print('3 ', time())
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
print('4 ', time())
# /v2/sources
sources = newsapi.get_sources()
print('5 ', time())

pprint(top_headlines)
print('6 ', time())
print('------------------------------------------------------------------')

pprint(all_articles)
print('7 ', time())
print('------------------------------------------------------------------')

pprint(sources)
print('8 ', time())
print('------------------------------------------------------------------')
