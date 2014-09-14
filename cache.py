import mingus.core.scales as scales

from mapper import Mapper
from utils import Utils

class ScaleCache:    
    cache = {};

    available_scales = ["diatonic", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian", "natural_minor", "harmonic_minor", "chromatic", "whole_note"];
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

    def __init__(self, cacheAll = True):
        self.mapper = Mapper();
        self.utils = Utils();
        if cacheAll:
            self.cacheAllScales();
            
    def cacheAllScales(self):
        for scale in self.available_scales:
            self.cacheHoleScale(scale);
                
    def cacheHoleScale(self, scale):
        for note in self.notes:
            self.cacheScale(note, scale);
            
    def cacheScale(self, note, scale):
        self.cache[scale + note] = self.mapper.getMap(note, scale);
                
    def checkInCache(self, note, scale):
        return note+scale in self.cache;
    
    def getScaleFromCache(self, note, scale):
        note_name = utils.getNote(note);
        if self.checkInCache(note_name, scale):
            return self.cache[note_name+scele];
        else:
            self.cacheScale(note_name, scale);
            return self.cache[note_name+scele];
        