import feedparser
from pprint import pprint

link = 'https://www.thehindu.com/news/feeder/default.rss'


NewsFeed = feedparser.parse(link)

print('Number of RSS posts :', len(NewsFeed.entries))

# entry = NewsFeed.entries[1]
# print('Post Title :',entry.title)

pprint(NewsFeed)