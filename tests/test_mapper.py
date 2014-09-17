#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_mapper.py
#
"""Tests for mapper"""
import unittest
import csv
import collections
from mapper import Mapper
from utils import Utils
from utils_for_tests import UtilsForTests
import timeit


class MapperTests(unittest.TestCase):
        
    def setUp(self):
        self.mapper = Mapper();
        self.utils = Utils();
        utils_for_tests = UtilsForTests();
        self.test_map_scale_to_white_keys = utils_for_tests.loadTestCorpus('test_corpus/test_to_white_keys_corpus');
        self.test_get_map = utils_for_tests.loadTestCorpus('test_corpus/test_get_map_corpus');
    
                
    def test_mapScaleToWhiteKeys(self):
        for case in self.test_map_scale_to_white_keys:
            mapped_scale = self.mapper.mapScaleToWhiteKeys(case[0]);
            self.assertDictEqual(mapped_scale, case[1]);
    
    def test_getMap(self):
        for case in self.test_get_map:
            map = self.mapper.getMap(case[0],case[1]);
            self.assertDictEqual(map, case[2]);
            
    @unittest.skip("Preformance test")        
    def test_TimeitGetMap(self):
        setup = "from utils import Utils; from mapper import Mapper; mapper = Mapper(); utils = Utils();"
        code_to_test = """
        for scale in utils.getAvailableScales():
            for note in utils.getNotes():
                mapper.getMap(note, scale);
        """
        result_first = timeit.repeat(code_to_test, setup = setup,repeat=100, number=100);
        result_avg = reduce(lambda x, y: x + y, result_first) / len(result_first)
        print("Result avg: " + str(result_avg));
        
    