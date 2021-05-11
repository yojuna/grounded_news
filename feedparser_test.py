import feedparser
from pprint import pprint

import config

links_dict = config.rss_links

links = list(links_dict.values())

NewsFeed = feedparser.parse(links[0])


# print('Number of RSS posts :', len(NewsFeed.entries))

# # entry = NewsFeed.entries[1]
# # print('Post Title :',entry.title)

# pprint(NewsFeed)