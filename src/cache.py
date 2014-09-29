#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cache.py
#
"""Midi scales cache"""


import mingus.core.scales as scales

from mapper import Mapper
from utils import Utils

class ScaleCache:    
    cache = {};

    def __init__(self, cacheAll = True):
        self.mapper = Mapper();
        self.utils = Utils();
        if cacheAll:
            self.cacheAllScales();

    def cacheAllScales(self):
        for scale in self.utils.getAllAvailableScales():
            self.cacheHoleScale(scale);

    def cacheHoleScale(self, scale):
        for note in self.utils.getNotes():
            self.cacheScale(note, scale);

    def cacheScale(self, note, scale):
        scale_to_map = self.mapper.getScaleToMap(note, scale);
        mapped_scale = self.mapper.getMap(scale_to_map);
        
        result = {'scale_to_map':scale_to_map, 'mapped_scale': mapped_scale}
        
        self.cache[note + scale] = result;

    def checkInCache(self, note, scale):
        return (note + scale) in self.cache;

    def clearCache(self):
        self.cache.clear();

    def getScaleFromCache(self, note, scale):
        if self.checkInCache(note, scale):
            return self.cache[note + scale];
        else:
            self.cacheScale(note, scale);
            return self.cache[note + scale];

    def __del__(self):
        self.clearCache();