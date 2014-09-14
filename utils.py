import mingus.core.notes as notes

class Utils:
    midi_int_to_note_map = {};
    midi_int_to_note_int_map = {};
    
    def __init__(self):
        self.createIntToNoteMap();
    
    def createIntToNoteMap(self):
        for i in range(0, 127):
            note = i % 12;
            octave = i / 12;
            self.midi_int_to_note_int_map[i] = i % 12;
            self.midi_int_to_note_map[i] = notes.int_to_note(i % 12);
            
    def getNote(self, midiNumber):
        return self.midi_int_to_note_map(midiNumber);
    
    def getNoteNumber(self, midiNumber):
        return self.midi_int_to_note_int_map(midiNumber);
        
    def getMidiNumber(self, note, octave):
        note_number = self.getNoteNumber(note);
        return note_number + (12 * octave);