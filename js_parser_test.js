let Parser = require('rss-parser');
let parser = new Parser();
// var rssLink = 'https://www.thehindu.com/news/feeder/default.rss'
var rssLink = 'http://feeds.feedburner.com/NDTV-LatestNews';

(async () => {

  let feed = await parser.parseURL(rssLink);
  console.log(feed);

  // feed.items.forEach(item => {
  //   console.log(item.title + ':' + item.link)
  // });

})();