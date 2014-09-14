import mingus.core.scales as scales
from mapper import Mapper 

class ScaleCache:
    mapper = Mapper();
    cache = {};
    available_scales = ["diatonic", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian", "natural_minor", "harmonic_minor", "chromatic", "whole_note"];
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

    def __init__(self, cacheAll = True):
        if cacheAll:
            cacheAllScales();
            
    def cacheAllScales(self):
        for scale in self.available_scales:
            self.cacheHoleScale(scale);
                
    def cacheHoleScale(self, scale):
        for note in self.notes:
            self.cacheScale(note, scale);
            
    def cacheScale(self, note, scale):
        self.cache[scale + note] = self.mapper(note, scale);
                
    def checkInCache(self, note, scale):
        return note+scale in self.cache;
    
    def getScaleFromCache(self, note, scale):
        if self.checkInCache(note, scale):
            return self.cache[note+scele];