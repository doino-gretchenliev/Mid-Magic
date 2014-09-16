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
    
    def __init__(self):
        self.utils = Utils();
        self.all_keys = self.utils.getNotes();
        self.white_keys = self.utils.getWhiteKeys();
    
    def searchPreviousNotMatched(self, note, map_to_match, white_keys_only=False):
        if white_keys_only is True:
            keys_to_match = self.white_keys;
            note_to_check = note.replace("#", "");
        else:
            keys_to_match = self.all_keys;
            note_to_check = note;
        
        #Direct match check
        if(note in keys_to_match):
            return note;
        
        i = keys_to_match.index(note_to_check);
        while(len(map_to_match) != len(keys_to_match)):
            if keys_to_match[i] not in map_to_match:
                return keys_to_match[i];
            else:
                if (i == 0): i = (len(keys_to_match) - 1);
                else: i-=1;
        return None;

    def mapScaleToWhiteKeys(self, scale):
        map_to_match = {};
        for note_in_scale in scale:
            note_to_map = self.searchPreviousNotMatched(note_in_scale, map_to_match, True);
            if note_to_map is not None:
                map_to_match[note_to_map] = note_in_scale;
        return map_to_match;
            
    def checkNotMapped(self, scale, map_to_match):
        for i in range(0, len(self.all_keys)):
            if self.all_keys[i] not in map_to_match:
                y = i;
                while(True):
                    if self.all_keys[y] in scale:
                        map_to_match[self.all_keys[i]] = self.all_keys[y];
                        break;
                    else:
                        if (y == 0): y = (len(map_to_match) - 1);
                        else: y-=1;
                        
    def checkNotMappedScaleKey(self, scale, map_to_match):
        for note in scale:
            if note not in map_to_match:
                note_to_map = self.searchPreviousNotMatched(note, map_to_match);
                if note_to_map is not None:
                    map_to_match[note_to_map] = note;
                else: break;
            
    def getMap(self, rootNote, scale):
        method = getattr(scales, scale);
        if not method:
            raise Exception("Scale %s not implemented" % scale);
        scale_to_map = method(rootNote);
        norm_scale = self.utils.normalizeScale(scale_to_map);

        mapped_scale_to_white_keys = self.mapScaleToWhiteKeys(norm_scale);
        self.checkNotMappedScaleKey(norm_scale, mapped_scale_to_white_keys);
        self.checkNotMapped(norm_scale, mapped_scale_to_white_keys);
        return mapped_scale_to_white_keys;
    
    def mapScaleToWhiteKeys_new(self, scale):
        result_map = {};
        for note in scale:
            result_map[note] = note;
        
        not_mapped_keys = self.diff(result_map.keys(), self.all_keys);
        mapped_keys = result_map.keys();
        
        for note in not_mapped_keys:
            result_map[note] = self.searchEmpty(note, mapped_keys);
            
        return result_map;
    
    def searchEmpty(self, note, result_map):
        dim_candidate = note;
        aug_candidate = note;
        print note
        print result_map
        print "---------"
        
        while(True):
            dim_candidate = self.utils.normalizeNote(notes.diminish(dim_candidate));
            aug_candidate = self.utils.normalizeNote(notes.augment(aug_candidate));
            print "Dim: %s; Aug: %s" % (dim_candidate, aug_candidate); 
            
            if dim_candidate in result_map:
                print "return " + dim_candidate;
                return dim_candidate;
            if aug_candidate in result_map:
                print "return " + aug_candidate;
                return aug_candidate;
            
    def diff(self, a, b):
        return [bb for bb in b if bb not in a]

    def getMap_new(self, rootNote, scale):
        method = getattr(scales, scale);
        if not method:
            raise Exception("Scale %s not implemented" % scale);
        scale_to_map = method(rootNote);
        norm_scale = self.utils.normalizeScale(scale_to_map);
        return self.mapScaleToWhiteKeys_new(norm_scale);
    