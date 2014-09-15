import mingus.core.notes as notes

class Utils:
    midi_int_to_note_map = {};
    midi_int_to_note_int_map = {};
    note_octave_to_midi_note_map = {};
    midi_note_to_note_octave_map = {};
    
    def __init__(self):
        self.createIntToNoteMap();
    
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