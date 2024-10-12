# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes": BackstagePassStrategy(),
            "Sulfuras": SulfurasStrategy(),
            "Conjured": ConjuredStrategy()
            }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, ItemStrategy())
            strategy.update(item)


class ItemStrategy:
    def update(self, item):
        if item.sell_in > 0:
            item.quality = item.quality - 1
        else:
            item.quality = item.quality - 2

        item.sell_in = item.sell_in - 1
        
        if item.quality < 0:
            item.quality = 0

class AgedBrieStrategy(ItemStrategy):
    def update(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

class BackstagePassStrategy(ItemStrategy):
    def update(self, item):
        if item.sell_in > 10:
            item.quality = item.quality + 1
        elif 5 < item.sell_in <= 10:
            item.quality = item.quality + 2
        elif 0 < item.sell_in <=5:
            item.quality = item.quality + 3
        else:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50

        item.sell_in = item.sell_in - 1

class SulfurasStrategy(ItemStrategy):
    def update(self, item):
        item.quality = 80

class ConjuredStrategy(ItemStrategy):
    def update(self, item):
        if item.sell_in > 0:
            item.quality = item.quality - 2
        else:
            item.quality = item.quality - 4

        item.sell_in = item.sell_in - 1

        if item.quality < 0:
            item.quality = 0
	
