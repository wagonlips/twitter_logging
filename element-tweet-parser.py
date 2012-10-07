#!/usr/bin/python2.6
from datetime import datetime
from lxml import etree
myXmlFile = etree.parse("latest_tweets.xml")
myText = myXmlFile.xpath('//text')
myDate = myXmlFile.xpath('//status/created_at')
textList = []
dateList = []
for x in myText:
  textList.append(x.text)
for y in myDate:
  y.text = y.text[4:]
  y.text = y.text.replace("+0000 ","")
  myDate = datetime.strptime(y.text, "%b %d %H:%M:%S %Y") 
  #myDate = myDate.strftime("%b %d %H:%M:%S %Y")
  myDate = "[" + str(myDate) + "]"
  dateList.append(myDate)
#TODO replace the hard-coded username with a variable
for a, b in zip(dateList, textList):
  print a, "&lt;wagonlips&gt;", b
