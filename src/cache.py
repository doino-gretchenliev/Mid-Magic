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
        self.cache[note + scale] = self.mapper.getMap(note, scale);

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