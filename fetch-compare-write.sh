#!/bin/bash
RDIR=~/twitter_logging # the root directory
$RDIR/wagonlips-twitter.py > $RDIR/latest_tweets.html
diff $RDIR/latest_tweets.html $RDIR/tweets.html
if [ $? -eq 1 ] 
  then 
  cp $RDIR/latest_tweets.html $RDIR/tweets.html
  cat $RDIR/tweets.html >> $RDIR/tweets-full.html
  cat $RDIR/tweets-full.html | sort -r | uniq > $RDIR/index-body.html
  (for r in $RDIR/index-head.html $RDIR/index-body.html $RDIR/index-tail.html;do cat $r >> $RDIR/index.html;done) > $RDIR/index.html
# lftp -f $RDIR/wagonlips-index-upload.lftp
scp -i ~/.ec2/ami-wagon-key-pair.pem $RDIR/index.html ec2-user@ec2-52-8-132-77.us-west-1.compute.amazonaws.com:site-wagonlips
fi
