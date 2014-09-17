#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_cache.py
#
"""Tests for cache"""
import unittest

from cache import ScaleCache
from utils import Utils

class CacheTests(unittest.TestCase):
    
    def setUp(self):
        self.utils = Utils();
    
    def test_cacheScale(self):
        cache = ScaleCache(False);
        cache.cacheScale('E', 'diatonic');
        self.assertIn('diatonicE', cache.cache);
        self.assertNotIn('diatonicA', cache.cache);
    
    def test_cacheHoleScale(self):
        cache = ScaleCache(False);
        cache.cacheHoleScale('diatonic');
        for note in self.utils.getNotes():
            self.assertIn('diatonic' + note, cache.cache);
        self.assertNotIn('lydian' + 'C', cache.cache);
        
    def test_checkInCache(self):
        cache = ScaleCache(False);
        cache.cacheHoleScale('diatonic');
        self.assertTrue(cache.checkInCache('C', 'diatonic'));
        self.assertFalse(cache.checkInCache('C', 'lydian'));
        
    def test_cacheAllScales(self):
        cache = ScaleCache(False);
        cache.cacheAllScales();
        for scale in self.utils.getAvailableScales():
            for note in self.utils.getNotes():
                self.assertIn(scale + note, cache.cache);
                
   