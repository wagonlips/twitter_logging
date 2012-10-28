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
from dateutil.tz import tzoffset

USERNAME = 'ttytter'

api = twitter.Api()

# get a 'tzinfo' instance with the UTC offset for the user's local time
user = api.GetUser(USERNAME)
localtime_tz = tzoffset(user.time_zone, user.utc_offset)

statuses = api.GetUserTimeline(USERNAME)
for s in statuses[:1]:
    # get UTC timestamp from seconds since epoch
    utc_dt = datetime.utcfromtimestamp(s.created_at_in_seconds).replace(tzinfo=pytz.utc)
    print('utc: {}'.format(utc_dt))
    # convert to local time in the user's timezone
    localtime_dt = utc_dt.astimezone(localtime_tz)
    print('localtime [{}]: {}'.format(localtime_dt.tzname(), localtime_dt))
