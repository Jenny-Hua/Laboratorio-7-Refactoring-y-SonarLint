# -*- coding: utf-8 -*-

def create_item(name, sell_in, quality):
    if name == "Aged Brie":
        return aged_brie_item(name, sell_in, quality)
    if name == "Sulfuras, Hand of Ragnaros":
        return sulfuras_item(name, sell_in, quality)
    if name == "Backstage passes to a TAFKAL80ETC concert":
        return backstage_item(name, sell_in, quality)
    if name == "Conjured Mana Cake":
        return conjured_item(name, sell_in, quality)
    else:
        return Item(name, sell_in, quality)
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
# class create_item(object):

class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1

class aged_brie_item (Item):
        def update_quality(self):
            if self.quality < 50:
                self.quality = self.quality + 1

            self.sell_in = self.sell_in - 1

class sulfuras_item (Item):
    def update_quality(self):
        pass

class backstage_item (Item):
    def update_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in = self.sell_in - 1

class conjured_item (Item):
    def update_quality(self):
        if self.quality > 2:
            self.quality = self.quality - 2
        else:
            self.quality = 0

        self.sell_in = self.sell_in - 1