#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# magic.py
#
"""Magic midi processor"""

import argparse
import logging
import Queue
import sys
import threading
import time
from cache import ScaleCache

import mingus.core.notes as notes
import rtmidi
from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *


log = logging.getLogger("midifilter")
cache = ScaleCache();

class MidiDispatcher(threading.Thread):
    scale = {};
    def __init__(self, midiin, midiout):
        super(MidiDispatcher, self).__init__()
        self.midiin = midiin
        self.midiout = midiout

    def __call__(self, event, date = None ):
        
        event_types = (NOTE_ON, NOTE_OFF)
        if (event[0][0] & 0xF0) in event_types:
            if(event[0][1] < 60):
                self.scale = mapper.getMap(event[0][1]);
                self.midiout.send_message(event[0]);
            else:
                octave = event[0][1] / int(12);
                note = event[0][1] % 12;
                note_name = notes.int_to_note(note);
                print notes.note_to_int(self.scale[note_name]);
                event[0][1] = notes.note_to_int(self.scale[note_name]) + (12 * octave);
                self.midiout.send_message(event[0]);
                print notes.int_to_note(event[0][1] %12) + "(" + str(event[0][1]) +")" + " instead of " + notes.int_to_note(note) + "(" + str(note * octave) + ")";
        

    def run(self):
        log.debug("Attaching MIDI input callback handler.")
        self.midiin.set_callback(self)

    def stop(self):
        self.queue.put(None)


def main(args=None):
    cache = ScaleCache(False);
    scale = cache.getScaleFromCache(60,"whole_note");
    print scale

    try:
        midiin, inport_name = open_midiport('Nord Piano 2 MIDI Output', "input")
        midiout, outport_name = open_midiport('Nord Piano 2 MIDI Input', "output")
        
    except IOError as exc:
        print(exc)
        return 1
    except (EOFError, KeyboardInterrupt):
        return 0
    
    dispatcher = MidiDispatcher(midiin, midiout)

    print("Entering main loop. Press Control-C to exit.")
    try:
        dispatcher.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        dispatcher.stop()
        dispatcher.join()
        print('')
    finally:
        print("Exit.")
        midiin.close_port()
        midiout.close_port()
        del midiin
        del midiout

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
