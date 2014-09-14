import mingus.core.scales as scales
import mingus.core.notes as notes

class Mapper:
    white_keys = ['C','D','E','F','G','A','B'];
    all_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    
    def searchPreviousNotMatched(self, note, match_map):
        note_to_check = note.replace("#", "");
        
        i = self.white_keys.index(note_to_check);
        while(True):
            if self.white_keys[i] not in match_map:
                return self.white_keys[i];
            else:
                i-=1;
                if i < 0:
                    i = self.white_keys.index('B');
               
    def mapScaleToWhiteKeys(self, scale, white_keys_map):
        for note_in_scale in scale:
            note_to_map = self.searchPreviousNotMatched(note_in_scale, white_keys_map);
            white_keys_map[note_to_map] = note_in_scale;
            
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
    
    def normalizeNotes(self, scale):
        int_scale = [];
        for note in scale:
            int_scale.append(notes.note_to_int(note));
        int_scale.sort(key=int);
        note_scale = [];
        for note in int_scale:
            note_scale.append(notes.int_to_note(note));
        
        return note_scale;
    
    def getMap(self, rootNote, scale):
        white_keys_map = {};
        
        method = getattr(scales, scale);
        if not method:
            raise Exception("Scale %s not implemented" % scale);
        scale_to_map = method(rootNote);
        
        norm_scale = self.normalizeNotes(scale_to_map);
        self.mapScaleToWhiteKeys(norm_scale, white_keys_map);
        self.checkNotMapped(norm_scale, white_keys_map);
        return white_keys_map;
    
