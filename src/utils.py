#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# utils.py
#
"""Utils"""

import collections
import mingus.core.notes as notes

class Utils:
    __available_scales = ["diatonic", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian", "natural_minor", "harmonic_minor", "chromatic", "whole_note"];
    __custom_scales = [];
    __custom_scales_intervals_map = {};
    
    __all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    __white_keys = ['C','D','E','F','G','A','B'];
    
    
    
    __midi_int_to_note_map = {};
    __midi_int_to_note_int_map = {};
    __note_octave_to_midi_note_map = {};
    __midi_note_to_note_octave_map = {};
    
    def __init__(self):
        self.createIntToNoteMap();
        self.loadCustomScales();
        
    def loadCustomScales(self):
        self.custom_scales = [];
        with open('custom_scales/custom_scales') as f:
            lines = f.readlines();
        for line in lines:
            result = eval(line);
            for key, intervals in result.iteritems():
                if key not in self.__custom_scales:
                    self.__custom_scales.append(key);
                    self.__custom_scales_intervals_map[key] = intervals;
    
    def createIntToNoteMap(self):
        for i in range(0, 128):
            note = i % 12;
            note_name = notes.int_to_note(note);
            octave = (i / 12) - 1;
            self.__midi_int_to_note_int_map[i] = i % 12;
            self.__midi_int_to_note_map[i] = notes.int_to_note(i % 12);
            self.__note_octave_to_midi_note_map[note_name + str(octave)] = i;
            self.__midi_note_to_note_octave_map[i] = [note_name,octave];
        
    def getNote(self, midiNumber):
        return self.__midi_int_to_note_map[midiNumber];
    
    def getNoteNumber(self, midiNumber):
        return self.__midi_int_to_note_int_map[midiNumber];
        
    def getMidiNumber(self, note, octave):
        return  self.__note_octave_to_midi_note_map[note + str(octave)];
    
    def getNoteAndOctave(self, midiNumber):
        return  self.__midi_note_to_note_octave_map[midiNumber];
    
    def getWhiteKeys(self):
        return self.__white_keys;
    
    def getCustomScales(self):
        return self.__custom_scales;
    
    def getAvailableScales(self):
        return self.__available_scales;
    
    def getAllAvailableScales(self):
        return list(self.getAvailableScales() + self.getCustomScales());
    
    def checkIsCustom(self, scale_name):
        return scale_name in self.getCustomScales();
    
    def getIntervalsForScale(self, scale_name):
        return self.__custom_scales_intervals_map[scale_name];
    
    def getNotes(self):
        return self.__all_notes;
    
    def normalizeScale(self, scale):
        int_scale = {};
        note_scale = [];
        
        for note in scale:
            int_scale[notes.note_to_int(note)] = note;
        
        od = collections.OrderedDict(sorted(int_scale.items(), key=lambda t: t[0]));
        
        for key in od.iterkeys():
            note_scale.append(notes.int_to_note(key));
        
        return note_scale;
    
    def normalizeNote(self, note):
        int_note = notes.note_to_int(note);
        return notes.int_to_note(int_note);
    
    