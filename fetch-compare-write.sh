#!/bin/bash
curl "https://api.twitter.com/1/statuses/user_timeline.xml?include_rts=true&screen_name=wagonlips&count=5" > /tmp/tweets.xml
diff /twitter_logging/latest_tweets.xml /tmp/tweets.xml
if [ $? -eq 1 ] 
  then 
  cp /tmp/tweets.xml /twitter_logging/latest_tweets.xml
  python /twitter_logging/element-tweet-parser.py > /tmp/tweets.html
  cat /twitter_logging/twitter-full.html >> /tmp/tweets.html
  cp /tmp/tweets.html /twitter_logging/twitter-full.html
  cat /twitter_logging/index-head.html > /twitter_logging/index.html
  cat /twitter_logging/twitter-full.html | sort -r | uniq >> /twitter_logging/index.html
  cat /twitter_logging/index-tail.html >> /twitter_logging/index.html
  lftp -f /twitter_logging/wagonlips-index-upload.lftp
fi
