#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Youtube Trends Mapから動画をスクレイピングするスクリプト
from selenium import webdriver
import re

# 取得する年齢層と性別と地域
age = ['--', '13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65-']       # '--'は全て
gen = ['male', 'female']
loc = 'jpn'  # '--'だとアメリカ

for a in age:
        for g in gen:
                print a, g

                # ブラウザ起動
                driver = webdriver.Firefox()
                url = 'http://www.youtube.com/trendsdashboard#age0=' + \
                a + '&gen0=' + g + '&loc0=' + loc
                driver.get(url)

                # 動画URL抽出
                html = driver.page_source.encode('utf-8')
                r = re.compile("/watch\?.+\>")
                m = r.findall(html)

                # ダブるので奇数番目だけ
                for url in m[0::2]:
                        print 'http://www.youtube.com' + url[:-2]
        driver.quit()
