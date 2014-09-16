#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# utils.py
#
"""Utils"""

import collections
import mingus.core.notes as notes

class Utils:
    available_scales = ["diatonic", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian", "natural_minor", "harmonic_minor", "chromatic", "whole_note"];
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    white_keys = ['C','D','E','F','G','A','B'];
    
    
    
    midi_int_to_note_map = {};
    midi_int_to_note_int_map = {};
    note_octave_to_midi_note_map = {};
    midi_note_to_note_octave_map = {};
    
    def __init__(self):
        self.createIntToNoteMap();
            
    def normalizeNote(self, note):
        int_note = notes.note_to_int(note);
        return notes.int_to_note(int_note);
    
    def createIntToNoteMap(self):
        for i in range(0, 128):
            note = i % 12;
            note_name = notes.int_to_note(note);
            octave = (i / 12) - 1;
            self.midi_int_to_note_int_map[i] = i % 12;
            self.midi_int_to_note_map[i] = notes.int_to_note(i % 12);
            self.note_octave_to_midi_note_map[note_name + str(octave)] = i;
            self.midi_note_to_note_octave_map[i] = [note_name,octave];
        
    def getNote(self, midiNumber):
        return self.midi_int_to_note_map[midiNumber];
    
    def getNoteNumber(self, midiNumber):
        return self.midi_int_to_note_int_map[midiNumber];
        
    def getMidiNumber(self, note, octave):
        return  self.note_octave_to_midi_note_map[note + str(octave)];
    
    def getNoteAndOctave(self, midiNumber):
        return  self.midi_note_to_note_octave_map[midiNumber];
    
    def getWhiteKeys(self):
        return self.white_keys;
    
    def getAvailableScales(self):
        return self.available_scales;
    
    def getNotes(self):
        return self.notes;
    
    def normalizeScale(self, scale):
        int_scale = {};
        note_scale = [];
        
        for note in scale:
            int_scale[notes.note_to_int(note)] = note;
        
        od = collections.OrderedDict(sorted(int_scale.items(), key=lambda t: t[0]));
        
        for key in od.iterkeys():
            note_scale.append(notes.int_to_note(key));
        
        return note_scale;
    