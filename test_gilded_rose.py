# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_sulfuras(self):
        items = [Item("Sulfuras", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)    

    def test_backstage_passes(self):
        items = [Item("Backstage passes", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured", 8, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

if __name__ == '__main__':
    unittest.main()
