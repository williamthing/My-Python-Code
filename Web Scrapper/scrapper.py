#!/usr/bin/Python
# William Thing
# Trying to Scrape some Data
#

from xml import etree # NOT SURE IF NEEDED
# IMPORTANT NOTE
# keep getting an error importing need to fix
# from reading stackoverflow and other online resources
# think its a pathing issue with reading my system's Python
# than the python software I installed, fix during free time
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

# This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices
