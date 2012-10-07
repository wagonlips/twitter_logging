#!/bin/bash
curl "https://api.twitter.com/1/statuses/user_timeline.xml?include_rts=true&screen_name=wagonlips&count=5" > /tmp/tweets.xml
diff latest_tweets.xml /tmp/tweets.xml
if [ $? -eq 1 ] 
  then 
  cp /tmp/tweets.xml latest_tweets.xml
  python element-tweet-parser.py > /tmp/tweets.html
  cat twitter-full.html >> /tmp/tweets.html
  cp /tmp/tweets.html twitter-full.html
  cat index-head.html > index.html
  cat twitter-full.html >> index.html
  cat index-tail.html >> index.html
fi
