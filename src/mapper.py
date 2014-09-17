#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# m.py
#
"""Magic midi mapper"""


import mingus.core.scales as scales
import mingus.core.notes as notes
from utils import Utils
from sets import Set

class Mapper:
    
    def __init__(self):
        self.utils = Utils();
        self.all_keys = self.utils.getNotes();
        self.white_keys = self.utils.getWhiteKeys();
    
    def mapScaleToWhiteKeys(self, scale):
        result_map = {};
        for note in scale:
            result_map[note] = note;
        
        not_mapped_keys = self.getNotMapped(result_map.keys(), self.all_keys);
        mapped_keys = result_map.keys();
        
        for note in not_mapped_keys:
            result_map[note] = self.searchEmpty(note, mapped_keys);
            
        return result_map;
    
    def searchEmpty(self, note, result_map):
        dim_candidate = note;
        aug_candidate = note;
        
        while(True):
            dim_candidate = self.utils.normalizeNote(notes.diminish(dim_candidate));
            aug_candidate = self.utils.normalizeNote(notes.augment(aug_candidate));
            
            if dim_candidate in result_map:
                return dim_candidate;
            if aug_candidate in result_map:
                return aug_candidate;
            
    def getNotMapped(self, a, b):
        return [bb for bb in b if bb not in a]
    
    def getMap(self, rootNote, scale):
        method = getattr(scales, scale);
        if not method:
            raise Exception("Scale %s not implemented" % scale);
        scale_to_map = method(rootNote);
        norm_scale = self.utils.normalizeScale(scale_to_map);
        return self.mapScaleToWhiteKeys(norm_scale);
    