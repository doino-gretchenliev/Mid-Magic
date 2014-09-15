#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# m.py
#
"""Magic midi mapper"""


import mingus.core.scales as scales
import mingus.core.notes as notes
from utils import Utils

class Mapper:
    all_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    
    def __init__(self):
        self.utils = Utils();
        self.white_keys = self.utils.getWhiteKeys();
    
    def searchPreviousNotMatched(self, note, match_map):
        note_to_check = note.replace("#", "");
        
        i = self.white_keys.index(note_to_check);
        while(len(match_map) != 7): #not some magical number(7 = white keys number)
            if self.white_keys[i] not in match_map:
                return self.white_keys[i];
            else:
                i-=1;
                if i < 0:
                    i = self.white_keys.index('B');
                    
    def checkAllWhiteKeysMapped(self, match_map):
        return None in match_map.values();
        
    def mapScaleToWhiteKeys(self, scale):
        mapped_scale = {};
        for note_in_scale in scale:
            note_to_map = self.searchPreviousNotMatched(note_in_scale, mapped_scale);
            mapped_scale[note_to_map] = note_in_scale;
        return mapped_scale;
            
    def checkNotMapped(self, scale, white_keys_map):
        for i in range(0, len(self.all_keys)):
            if self.all_keys[i] not in white_keys_map:
                y = i;
                found = False;
                while(found == False):
                    if self.all_keys[y] in scale:
                        white_keys_map[self.all_keys[i]] = self.all_keys[y];
                        found = True;
                    else:
                        y-=1;
    
    def getMap(self, rootNote, scale):
        
        method = getattr(scales, scale);
        if not method:
            raise Exception("Scale %s not implemented" % scale);
        scale_to_map = method(rootNote);
        
        norm_scale = self.utils.normalizeScale(scale_to_map);
        mapped_scale_to_white_keys = self.mapScaleToWhiteKeys(norm_scale);
        self.checkNotMapped(norm_scale, mapped_scale_to_white_keys);
        return mapped_scale_to_white_keys;
    
