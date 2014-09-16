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

class MapperTests(unittest.TestCase):
        
    def setUp(self):
        self.mapper = Mapper();
        self.utils = Utils();
        self.test_map_scale_to_white_keys = self.loadInputToResultMap('test_corpus/map_to_white_keys_corpus.csv');
        self.test_check_not_mapped_scale_key = self.loadInputToResultMap('test_corpus/map_check_not_mapped_white_key.csv', 'double-map');
        self.test_check_not_mapped = self.loadInputToResultMap('test_corpus/map_check_not_mapped.csv', 'double-map');
        self.test_get_map = self.loadInputToResultMap('test_corpus/map_get_map.csv', 'note-scale');
    
    def loadInputToResultMap(self, file, input_format = None):
        input_result_map = [];
        with open(file, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"');
            for row in spamreader:
                if input_format == 'double-map':
                    input_scale = row[0].split(';');
                    input_map = row[1].split(';');
                    input_map_dict = dict(pair.split('-') for pair in input_map);
                    expected = row[2].split(';');
                    expected_map = dict(pair.split('-') for pair in expected);
                    input_result_map.append([input_scale, input_map_dict, expected_map]);
                elif input_format == 'note-scale':
                    input_note = row[0];
                    input_scale = row[1];
                    expected = row[2].split(';');
                    expected_map = dict(pair.split('-') for pair in expected);
                    input_result_map.append([input_note, input_scale, expected_map]);
                else:
                    input_scale = row[0].split(';');
                    expected = row[1].split(';');
                    expected_map = dict(pair.split('-') for pair in expected);
                    input_result_map.append([input_scale, expected_map]);
        del spamreader;
        return input_result_map;
                
    def test_mapScaleToWhiteKeys(self):
        for case in self.test_map_scale_to_white_keys:
            mapped_scale = self.mapper.mapScaleToWhiteKeys(case[0]);
            self.assertDictEqual(mapped_scale, case[1]);
        
    def test_checkNotMappedScaleKey(self):
        for case in self.test_check_not_mapped_scale_key:
            self.mapper.checkNotMappedScaleKey(case[0],case[1]);
            self.assertDictEqual(case[1], case[2]);
    
    def test_checkNotMapped(self):
        for case in self.test_check_not_mapped:
            self.mapper.checkNotMapped(case[0],case[1]);
            self.assertDictEqual(case[1], case[2]);
    

    def test_getMap(self):
        for case in self.test_get_map:
            #map = self.mapper.getMap_new(case[0],case[1]);
            map = self.mapper.mapScaleToWhiteKeys_new(['F' , 'B']);
            print "-------------------------------"
            print case[0] + case[1];
            print map
            print "-------------------------------"
            
            self.assertDictEqual(map, ass_map);
            
            
            