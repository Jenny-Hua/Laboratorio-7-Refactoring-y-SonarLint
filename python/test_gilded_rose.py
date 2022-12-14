# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, create_item

class GildedRoseTest(unittest.TestCase):
    # item(name, sell_in, quality)
    def test_elixir(self):
        items = [create_item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)
    def test_aged_brie(self):
        items = [create_item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_sulfuras(self):
        items = [create_item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage(self):
        items = [create_item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(42, items[0].quality)

    # Test para articulos conjurados
    def test_conjured(self):
        items = [create_item("Conjured Mana Cake", 6, 2)]  # <-- :O
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
if __name__ == '__main__':
    unittest.main()
