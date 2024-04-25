#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('items.faix', 'r')

soup = BeautifulSoup(file, 'xml')

items = soup.find_all("item", { 'id': True })


for item in items:
    print(f"{item['id']}\t {item.find('item').text}\t\t{item.find('type').text}\t\t{item.find('rarity')['value']}")

