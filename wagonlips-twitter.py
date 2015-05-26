#!/usr/bin/python
import pytz
import twitter
import mysecret
from datetime import datetime
api = twitter.Api(mysecret.my_consumer_key,mysecret.my_consumer_secret,mysecret.my_access_token_key,mysecret.my_access_token_secret)
pst_tz = pytz.timezone('America/Los_Angeles')
statuses = api.GetUserTimeline()
for s in statuses:
#    # get UTC timestamp from seconds since epoch
  utc_dt = datetime.utcfromtimestamp(s.created_at_in_seconds).replace(tzinfo = pytz.utc)
#    # convert to given timezone
  pst_dt = pst_tz.normalize(utc_dt.astimezone(pst_tz))
  print '[' + (pst_dt.strftime('%Y-%m-%d %H:%M:%S')) + '] &lt;wagonlips&gt; ' + s.text
