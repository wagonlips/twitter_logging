#!/usr/bin/python
import twitter
api = twitter.Api() 
statuses = api.GetUserTimeline('wagonlips')
for s in statuses:
  print s.text 
