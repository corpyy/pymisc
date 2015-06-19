#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Yahoo Newsのトピックをスクレイピングするスクリプト
 
import urllib2
from pprint import pprint
from BeautifulSoup import BeautifulSoup
 
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0    .04506.30; .NET CLR 3.0.04506.648)')]
html = opener.open('http://www.yahoo.co.jp/').read()
 
linklist = []
soup = BeautifulSoup(html)
lis = soup.find('ul', {'class': 'emphasis'}).findAll('li')
for li in lis:
    ahref = li.find('a')
    print "%s - %s" % (ahref.string, dict(ahref.attrs)['href'])
