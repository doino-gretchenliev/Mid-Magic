#------------------------------------------------------------------------------#
#                                                                              #
#                                    GUI                                       #
#                                                                              #
#------------------------------------------------------------------------------#
from Tkinter import *
from utils import Utils
from cache import ScaleCache
from mapper import Mapper
import mingus.core.notes as notes
import logging

import rtmidi_python as rtmidi
from rtmidi.midiconstants import *

log = logging.getLogger("mid-magic")

class Gui(Frame):
    
    transpose = 0;
    scale_to_map = [];
    mapped_scale = {};
    
    auto_mode = False;
    button_state_map = {};
    
    button_color_state_map_black = {True:'#00CCA9',False:'#2b3633'};
    button_color_state_map_white = {True:'#00CCA9',False:'#FFFFCD'};
    
    def __init__(self,Master=None,*pos,**kw):
        self.utils = Utils();
        self.cache = ScaleCache();
        self.mapper = Mapper();
        self.load_init_button_states();
        
        ############### GUI ############### 
        apply(Frame.__init__,(self,Master),kw)
        self._Frame4 = Frame(self)
        self._Frame4.pack(expand='yes',fill='both',side='left')
        self._Frame3 = Frame(self,background='#016678')
        self._Frame3.pack(expand='yes',fill='both',side='left')
        self._Frame29 = Frame(self._Frame4,background='#016678')
        self._Frame29.pack(expand='yes',fill='both',side='top')
        self._ListboxNote = Listbox(self._Frame29,background='#014455'
            ,foreground='#CCFFDE',highlightthickness='0',selectmode='extended'
            ,width='15')
        self._ListboxNote.pack(expand='yes',fill='both',side='left')
        self._Frame28 = Frame(self._Frame4,background='#016678')
        self._Frame28.pack(expand='yes',fill='both',side='top')
        self._ListboxScale = Listbox(self._Frame28,background='#014455'
            ,foreground='#CCFFDE',highlightthickness='0',selectmode='extended'
            ,width='15')
        self._ListboxScale.pack(expand='yes',fill='both',side='left')
        self._Frame17 = Frame(self._Frame3)
        self._Frame17.pack(expand='yes',fill='both',side='top')
        self._LabelStatus = Label(self._Frame17,background='#FFFFCD'
            ,relief='groove',state='disabled',text='This is test text.')
        self._LabelStatus.pack(expand='yes',fill='both',side='top')
        self._Frame11 = Frame(self._Frame3,background='#016678')
        self._Frame11.pack(expand='yes',fill='both',side='top')
        self._Frame10 = Frame(self._Frame3,background='#016678')
        self._Frame10.pack(side='top')
        self._Frame19 = Frame(self._Frame3)
        self._Frame19.pack(side='top')
        self._Frame18 = Frame(self._Frame3)
        self._Frame18.pack(expand='yes',fill='both',side='top')
        self._Frame32 = Frame(self._Frame11,background='#016678')
        self._Frame32.pack(side='left')
        self._MenuInput = Menubutton(self._Frame32,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#FFFFCD',menu='_MenuInputs'
            ,text='Input',width='30')
        self._MenuInput.pack(expand='yes',fill='both',side='top')
        self._Frame33 = Frame(self._Frame11,background='#016678')
        self._Frame33.pack(expand='yes',fill='both',side='left')
        self._ButtonScanMidi = Button(self._Frame33,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonScanMidi_command,foreground='#CCFFDE'
            ,text='Scan for midi devices')
        self._ButtonScanMidi.pack(side='top')
        self._Frame31 = Frame(self._Frame11,background='#016678')
        self._Frame31.pack(side='left')
        self._MenuOutput = Menubutton(self._Frame31,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#FFFFCD',text='Output'
            ,width='30')
        self._MenuOutput.pack(expand='yes',fill='both',side='top')
        self._Frame22 = Frame(self._Frame10,background='#016678',width='30')
        self._Frame22.pack(expand='yes',fill='both',side='left')
        self._Frame24 = Frame(self._Frame10,background='#016678'
            ,highlightbackground='Black',width='20')
        self._Frame24.pack(expand='yes',fill='both',side='left')
        self._ButtonCSharp = Button(self._Frame24,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonCSharp_command,foreground='#CCFFDE'
            ,relief='flat',text='C#',width='1')
        self._ButtonCSharp.pack(expand='yes',fill='both',side='left')
        self._Frame13 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame13.pack(side='left')
        self._Frame14 = Frame(self._Frame10)
        self._Frame14.pack(side='left')
        self._ButtonDSharp = Button(self._Frame14,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonDSharp_command,foreground='#CCFFDE'
            ,height='10',text='D#',width='1')
        self._ButtonDSharp.pack(expand='yes',fill='both',side='left')
        self._Frame7 = Frame(self._Frame10,background='#016678',width='50')
        self._Frame7.pack(expand='yes',fill='both',side='left')
        self._Frame8 = Frame(self._Frame10,background='#016678')
        self._Frame8.pack(expand='yes',fill='both',side='left')
        self._ButtonFSharp = Button(self._Frame8,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonFSharp_command,foreground='#CCFFDE'
            ,text='F#',width='1')
        self._ButtonFSharp.pack(expand='yes',fill='both',side='left')
        self._Frame15 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame15.pack(side='left')
        self._Frame26 = Frame(self._Frame10)
        self._Frame26.pack(expand='yes',fill='both',side='left')
        self._ButtonGSharp = Button(self._Frame26,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonGSharp_command,foreground='#CCFFDE'
            ,text='G#',width='1')
        self._ButtonGSharp.pack(expand='yes',fill='both',side='left')
        self._Frame12 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame12.pack(expand='yes',fill='both',side='left')
        self._Frame16 = Frame(self._Frame10)
        self._Frame16.pack(expand='yes',fill='both',side='left')
        self._ButtonASharp = Button(self._Frame16,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonASharp_command,foreground='#CCFFDE'
            ,text='A#',width='1')
        self._ButtonASharp.pack(expand='yes',fill='both',side='left')
        self._Frame30 = Frame(self._Frame10,background='#016678',width='30')
        self._Frame30.pack(expand='yes',fill='both',side='left')
        self._Frame21 = Frame(self._Frame19,background='#016678',width='20')
        self._Frame21.pack(expand='yes',fill='both',side='left')
        self._ButtonC = Button(self._Frame21,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonC_command,height='12',text='C',width='2')
        self._ButtonC.pack(expand='yes',fill='both',side='left')
        self._Frame25 = Frame(self._Frame19)
        self._Frame25.pack(expand='yes',fill='both',side='left')
        self._ButtonD = Button(self._Frame25,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonD_command,text='D',width='2')
        self._ButtonD.pack(expand='yes',fill='both',side='left')
        self._Frame20 = Frame(self._Frame19)
        self._Frame20.pack(expand='yes',fill='both',side='left')
        self._ButtonE = Button(self._Frame20,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonE_command,text='E',width='2')
        self._ButtonE.pack(expand='yes',fill='both',side='right')
        self._Frame1 = Frame(self._Frame19)
        self._Frame1.pack(expand='yes',fill='both',side='left')
        self._ButtonF = Button(self._Frame1,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonF_command,text='F',width='2')
        self._ButtonF.pack(expand='yes',fill='both',side='right')
        self._Frame27 = Frame(self._Frame19)
        self._Frame27.pack(expand='yes',fill='both',side='left')
        self._ButtonG = Button(self._Frame27,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonG_command,text='G',width='2')
        self._ButtonG.pack(expand='yes',fill='both',side='left')
        self._Frame2 = Frame(self._Frame19)
        self._Frame2.pack(expand='yes',fill='both',side='left')
        self._ButtonA = Button(self._Frame2,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonA_command,text='A',width='2')
        self._ButtonA.pack(expand='yes',fill='both',side='right')
        self._Frame6 = Frame(self._Frame19)
        self._Frame6.pack(expand='yes',fill='both',side='left')
        self._ButtonB = Button(self._Frame6,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonB_command,text='B',width='2')
        self._ButtonB.pack(expand='yes',fill='both',side='left')
        self._Frame5 = Frame(self._Frame19,background='#016678')
        self._Frame5.pack(expand='yes',fill='both',side='left')
        self._Frame23 = Frame(self._Frame18,background='#016678')
        self._Frame23.pack(expand='yes',fill='both',side='left')
        self._ScaleTrans = Scale(self._Frame23,background='#016678'
            ,bigincrement=1,borderwidth='0',command=self._on__ScaleTrans_command
            ,foreground='#2b3633',from_=-12,highlightbackground='#3b3c3c'
            ,highlightcolor='#3b3c3c',highlightthickness='0'
            ,label='Transpose(cents)',orient='horizontal',resolution=1
            ,sliderlength='50',tickinterval=0,to=12)
        self._ScaleTrans.pack(expand='yes',fill='x',side='left')
        self._Frame9 = Frame(self._Frame18,background='#016678')
        self._Frame9.pack(expand='yes',fill='both',side='left')
        self._ButtonAutoMode = Button(self._Frame9,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD',text='Magic Mode!')
        self._ButtonAutoMode.pack(expand='yes',side='bottom')
        self._Frame34 = Frame(self._Frame18,background='#016678')
        self._Frame34.pack(expand='yes',fill='both',side='left')
        self._ButtonQuit = Button(self._Frame34,activebackground='#BB1167'
            ,background='#CD0045',command=self._on__ButtonQuit_command
            ,text='Quit')
        self._ButtonQuit.pack(expand='yes',side='left')
        ############### GUI ###############
    
        self._MenuInput.menu  =  Menu(self._MenuInput, tearoff = 0 );
        self._MenuInput["menu"]  =  self._MenuInput.menu;
            
        self._MenuOutput.menu  =  Menu(self._MenuOutput, tearoff = 0 );
        self._MenuOutput["menu"]  =  self._MenuOutput.menu;
    
        self.midi_in = rtmidi.MidiIn();
        self.midi_out = rtmidi.MidiOut();
        
        self.midi_vir = rtmidi.MidiIn();
        self.midi_vir.open_virtual_port("TEST");
        
        self.midi_in.callback = self.midi_callback
        
        self._ButtonAutoMode.config(command=self.process_auto_mode_change);

        self.showMessage("Loading...");
        for note in self.utils.getNotes():
            self._ListboxNote.insert(END, note);
            
        for scale in self.utils.getAvailableScales():
            self._ListboxScale.insert(END, scale);
        self.showMessage("Ready to work, sir!");
        
        self.current_note = ();
        self.current_scale = ();   
        self.poll_lists(); # start polling the list
        
    def process_auto_mode_change(self):
        if self.auto_mode:
            self.auto_mode = False;
        else:
            self.auto_mode = True;
            self.showMessage("Magic Mode!");
        
    def check_midi_ports(self):
        self.midi_out.close_port();
        self.midi_out.close_port();
        
        self.midi_in = rtmidi.MidiIn();
        self.midi_out = rtmidi.MidiOut();
        
        ports_in = self.midi_in.ports;
        ports_out = self.midi_out.ports;
        
        self._MenuInput.menu.delete(0,END);
        self._MenuOutput.menu.delete(0,END);
                
        if len(ports_in) == 0:
            self._MenuInput.config(text="No input devices");
        else:
            for port_index in range(0, len(ports_in)):
                self._MenuInput.menu.add_command(label=ports_in[port_index], command=lambda port_index=port_index: self.midi_in_device_select_callback(port_index));
                
        if len(ports_out) == 0:
            self._MenuInput.config(text="No output devices");
        else:
            for port_index in range(0, len(ports_out)):
                self._MenuOutput.menu.add_command(label=ports_out[port_index], command=lambda port_index=port_index: self.midi_out_device_select_callback(port_index));
                
    def midi_out_device_select_callback(self, port_index):
        self.midi_out.close_port();
        self.midi_out.open_port(port_index);
        self.updateMenuTitle(port_index, self._MenuOutput, self._MenuOutput.menu);
        
    def midi_in_device_select_callback(self, port_index):
        self.midi_in.close_port();
        self.midi_in.open_port(port_index);
        self.updateMenuTitle(port_index, self._MenuInput, self._MenuInput.menu);
    
    def updateMenuTitle(self, index, menu_button, menu):
        menu_button.config(text=menu.entrycget(index, "label"));
        
    def poll_lists(self):
        now_note = self._ListboxNote.curselection();
        now_scale = self._ListboxScale.curselection();
        if len(now_note) != 0 and now_note != self.current_note:
            self.process_note_change(now_note)
            self.current_note = now_note
        if len(now_scale) != 0 and now_scale != self.current_scale:
            self.process_scale_change(now_scale)
            self.current_scale = now_scale
        self.after(250, self.poll_lists)
        
    def midi_callback(self, message, time_stamp):
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
        
    def _on__ButtonScanMidi_command(self,Event=None):
        self.check_midi_ports();

    def process_note_change(self, note):
        if len(note) != 0 and len(self.current_scale) != 0:
            note_name = notes.int_to_note(note[0]);
            scale_name = self.utils.getAvailableScales()[self.current_scale[0]];
            self.scale_to_map = self.mapper.getScaleToMap(note_name, scale_name);
            mapped_scale = self.cache.getScaleFromCache(note_name, scale_name);
            self.show_scale_to_buttons();
            self.auto_mode = False;
            self.showMessage(note_name + " - " + scale_name);
     
    def process_scale_change(self, scale):
        if len(scale) != 0 and len(self.current_note) != 0:
            note_name = notes.int_to_note(self.current_note[0]);
            scale_name = self.utils.getAvailableScales()[scale[0]];
            self.scale_to_map = self.mapper.getScaleToMap(note_name, scale_name);
            self.mapped_scale = self.cache.getScaleFromCache(note_name, scale_name);
            self.show_scale_to_buttons();
            self.auto_mode = False;
            self.showMessage(note_name + " - " + scale_name);
            
    def show_scale_to_buttons(self):
        for note in self.utils.getNotes():
            button_name = note.replace('#','Sharp');
            button_name = "self._Button" + button_name;
            
            if note in self.scale_to_map:
                self.button_state_map[note] = True 
                if '#' in note:
                    button_color = self.button_color_state_map_black[True];
                else:
                    button_color = self.button_color_state_map_white[True];
            else:
                self.button_state_map[note] = False
                if '#' in note:
                    button_color = self.button_color_state_map_black[False];
                else:
                    button_color = self.button_color_state_map_white[False];
            eval(button_name + ".configure(bg = '" + button_color + "')");

    def load_init_button_states(self):
        for note in self.utils.getNotes():
            self.button_state_map[note] = False;
            
    def process_button_change(self, note):
        new_state = self.update_scale_to_map(note);
        self.button_state_map[note] = new_state;
        self.set_new_mapped_scale();
        self.auto_mode = False;
        return new_state;
            
    def update_scale_to_map(self, note):
        if self.button_state_map[note] is True:
            self.scale_to_map.remove(note);
            return False;
        else:
            self.scale_to_map.append(note);
            return True;
            
    def set_new_mapped_scale(self):
        if len(self.scale_to_map) != 0:
            self.mapped_scale = self.mapper.getCustomMap(self.scale_to_map);
            self.showMessage("Cutom scale: \n");
            
    def showMessage(self, message):
        self._LabelStatus.config(text = message);

    def _on__ButtonASharp_command(self,Event=None):
        new_state = self.process_button_change('A#');
        self._ButtonASharp.configure(bg = self.button_color_state_map_black[new_state]);

    def _on__ButtonA_command(self,Event=None):
        new_state = self.process_button_change('A');
        self._ButtonA.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonB_command(self,Event=None):
        new_state = self.process_button_change('B');
        self._ButtonB.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonCSharp_command(self,Event=None):
        new_state = self.process_button_change('C#');
        self._ButtonCSharp.configure(bg = self.button_color_state_map_black[new_state]);

    def _on__ButtonC_command(self,Event=None):
        new_state = self.process_button_change('C');
        self._ButtonC.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonDSharp_command(self,Event=None):
        new_state = self.process_button_change('D#');
        self._ButtonDSharp.configure(bg = self.button_color_state_map_black[new_state]);

    def _on__ButtonD_command(self,Event=None):
        new_state = self.process_button_change('D');
        self._ButtonD.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonE_command(self,Event=None):
        new_state = self.process_button_change('E');
        self._ButtonE.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonFSharp_command(self,Event=None):
        new_state = self.process_button_change('F#');
        self._ButtonFSharp.configure(bg = self.button_color_state_map_black[new_state]);

    def _on__ButtonF_command(self,Event=None):
        new_state = self.process_button_change('F');
        self._ButtonF.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonGSharp_command(self,Event=None):
        new_state = self.process_button_change('G#');
        self._ButtonGSharp.configure(bg = self.button_color_state_map_black[new_state]);

    def _on__ButtonG_command(self,Event=None):
        new_state = self.process_button_change('G');
        self._ButtonG.configure(bg = self.button_color_state_map_white[new_state]);

    def _on__ButtonMap_command(self,Event=None):
        pass

    def _on__ButtonQuit_command(self,Event=None):
        self.midi_in.close_port();
        self.midi_out.close_port();
        exit(0);

    def _on__ScaleTrans_command(self,Event=None):
        self.transpose = self._ScaleTrans.get();
        


