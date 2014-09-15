#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_utils.py
#
"""Tests for utils"""

import unittest
from utils import Utils

class UtilsTests(unittest.TestCase):
    test_get_note = {'C': 60,'C': 0, 'G': 127, 'E': 64, 'A#': 70};
    test_get_note_number = {0: 60, 1:85,2:122,3:99,4:16,5:41,6:90,7:55,8:44,9:21,10:70,11:83};
    test_get_midi_number = {0:['C',-1],60:['C',4],12:['C',0],120:['C',9],127:['G',9]};
    test_normalize_scale = [['G', 'C##', 'Bb', 'B##b', 'A#', 'D', 'B#'],['C','D', 'G', 'A#']]

    def setUp(self):
        self.utils = Utils();

    def test_getNote(self):
        for note, midi_note in self.test_get_note.iteritems():
            self.assertEqual(note, self.utils.getNote(midi_note));
            
    def test_getNoteNumber(self):
        for note_number, midi_note in self.test_get_note_number.iteritems():
            self.assertEqual(note_number, self.utils.getNoteNumber(midi_note));
    
    def test_getMidiNumber(self):
        for midi_note, note_octave in self.test_get_midi_number.iteritems():
            self.assertEqual(midi_note, self.utils.getMidiNumber(note_octave[0],note_octave[1]));
            
    def test_getNoteAndOctave(self):
        for midi_note, note_octave in self.test_get_midi_number.iteritems():
            self.assertEqual(note_octave[0], self.utils.getNoteAndOctave(midi_note)[0]);
            self.assertEqual(note_octave[1], self.utils.getNoteAndOctave(midi_note)[1]);
            
    def test_normalizeScale(self):
        norm_scale = self.utils.normalizeScale(self.test_normalize_scale[0]);
        self.assertSequenceEqual(norm_scale, self.test_normalize_scale[1]);
        
if __name__ == '__main__':
    unittest.main();
