# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:59:19 2019

@author: BensonHsieh
"""

from selenium import webdriver
import time
#import unittest
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/webdriver/chromedriver")
driver.get("http://google.com")
element = driver.find_element_by_name("q")
element.send_keys("寒流")
element.submit()

time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items = soup.select('div.r > a')
for i in items:
    print("標題：" + i.select('h3')[0].text)
    print("網址：" + i.get('href'))
    print('\n')

driver.quit()