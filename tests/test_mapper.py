#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_mapper.py
#
"""Tests for mapper"""
import unittest
import csv
from mapper import Mapper

class MapperTests(unittest.TestCase):
    
    test_map_scale_to_white_keys = [];
    
    def setUp(self):
        self.mapper = Mapper();
        
        with open('test_corpus/map_to_white_keys_corpus.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"');
            for row in spamreader:
                input = row[0].split(';');
                expected = row[1].split(';');
                expected_map = dict(pair.split('-') for pair in expected);
                self.test_map_scale_to_white_keys.append([input, expected_map]);
                
    def test_mapScaleToWhiteKeys(self):
        for case in self.test_map_scale_to_white_keys:
            mapped_scale = self.mapper.mapScaleToWhiteKeys(case[0]);
            self.assertDictEqual(mapped_scale, case[1]);
        