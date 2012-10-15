#!/usr/bin/python
import twitter
api = twitter.Api(consumer_key='zam8ZID2I7vkEU3idTgm4Q', consumer_secret='z1moldb9Zm95vzY1QELPxRE1M3VRKAfDABO3ZARJ6c', access_token_key='7712962-htcVVjE1gOult9bprMby57Fc0cO2smA3vVzW8rzUw', access_token_secret='Mzn8E4s7YO4A9TxBSCwMHolw4DeWQqQA2qCYzmBQtA') 
statuses = api.GetUserTimeline('wagonlips')
for s in statuses:
  print s.text 
