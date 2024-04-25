#!/usr/bin/python3

from xml.dom import minidom

faix = minidom.parse('items.faix')

items = faix.getElementsByTagName('item')


for item in items:
    id = item.getAttribute('id')

    name = item.getElementsByTagName('item')
    item_value = name[0].firstChild.nodeValue

    type = item.getElementsByTagName('type')
    type_value = type[0].firstChild.nodeValue

    rarity = item.getElementsByTagName('rarity')
    rarity_value = rarity[0].getAttribute('value')

    print(f"{id}\t {item_value}\t {type_value}\t {rarity_value}")

    print("="*30) 

    print(f"\t{items.length}")
