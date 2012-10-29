#!/usr/bin/python
#import twitter
#api = twitter.Api() 
#statuses = api.GetUserTimeline('ttytter')
#for s in statuses:
#  print s.created_at + " " + s.text
#
import pytz
import twitter

from datetime import  datetime

USERNAME = 'wagonlips'

api = twitter.Api()

user = api.GetUser(USERNAME)
pst_tz = pytz.timezone('America/Los_Angeles')

statuses = api.GetUserTimeline(USERNAME)
for s in statuses:
    # get UTC timestamp from seconds since epoch
    utc_dt = datetime.utcfromtimestamp(s.created_at_in_seconds).replace(tzinfo=pytz.utc)
    # convert to given timezone
    pst_dt = pst_tz.normalize(utc_dt.astimezone(pst_tz))
    print '[' + (pst_dt.strftime('%Y-%m-%d %H:%M:%S')) + '] &lt;wagonlips&gt; ' + s.text
