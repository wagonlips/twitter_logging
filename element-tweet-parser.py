#!/usr/bin/python2.6
from datetime import datetime
from lxml import etree
myXmlFile = etree.parse("latest_tweets.xml")
myDoc = myXmlFile.xpath('//text')
myDate = myXmlFile.xpath('//status/created_at')
textList = []
dateList = []
for x in myDoc:
  textList.append(x.text)
for y in myDate:
  y.text = y.text[4:]
  y.text = y.text.replace("+0000 ","")
  myDate = datetime.strptime(y.text, "%b %d %H:%M:%S %Y") 
  dateList.append(myDate)
for a, b in zip(dateList, textList):
  print a, "&lt;wagonlips&gt;", b
