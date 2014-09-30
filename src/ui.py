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
    
    event_types = (NOTE_ON, NOTE_OFF);
    
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
            ,foreground='#CCFFDE',height='4',highlightthickness='0'
            ,selectborderwidth='5',selectmode='extended',width='6')
        self._ListboxNote.pack(expand='yes',fill='both',side='left')
        self._Frame28 = Frame(self._Frame4,background='#016678')
        self._Frame28.pack(expand='yes',fill='both',side='top')
        self._ListboxScale = Listbox(self._Frame28,background='#014455'
            ,foreground='#CCFFDE',height='5',highlightthickness='0'
            ,selectmode='extended',width='6')
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
            ,text='Input',width='10')
        self._MenuInput.pack(expand='yes',fill='both',side='top')
        self._Frame33 = Frame(self._Frame11,background='#016678')
        self._Frame33.pack(expand='yes',fill='x',side='left')
        self._ButtonScanMidi = Button(self._Frame33,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonScanMidi_command,foreground='#CCFFDE'
            ,text='Scan')
        self._ButtonScanMidi.pack(expand='yes',fill='x',side='top')
        self._Frame31 = Frame(self._Frame11,background='#016678')
        self._Frame31.pack(expand='yes',fill='both',side='left')
        self._MenuOutput = Menubutton(self._Frame31,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#FFFFCD',text='Output'
            ,width='10')
        self._MenuOutput.pack(expand='yes',fill='x',side='top')
        self._Frame22 = Frame(self._Frame10,background='#016678',width='1')
        self._Frame22.pack(expand='yes',fill='both',side='left')
        self._Frame24 = Frame(self._Frame10,background='#016678'
            ,highlightbackground='Black',width='20')
        self._Frame24.pack(expand='yes',fill='both',side='left')
        self._ButtonCSharp = Button(self._Frame24,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonCSharp_command,foreground='#CCFFDE'
            ,height='2',relief='flat',text='C#',width='1')
        self._ButtonCSharp.pack(expand='yes',side='left')
        self._Frame13 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame13.pack(expand='yes',fill='both',side='left')
        self._Frame14 = Frame(self._Frame10)
        self._Frame14.pack(expand='yes',fill='both',side='left')
        self._ButtonDSharp = Button(self._Frame14,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonDSharp_command,foreground='#CCFFDE'
            ,height='2',text='D#',width='1')
        self._ButtonDSharp.pack(expand='yes',fill='both',side='left')
        self._Frame7 = Frame(self._Frame10,background='#016678',width='50')
        self._Frame7.pack(expand='yes',fill='both',side='left')
        self._Frame8 = Frame(self._Frame10,background='#016678')
        self._Frame8.pack(expand='yes',fill='both',side='left')
        self._ButtonFSharp = Button(self._Frame8,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonFSharp_command,foreground='#CCFFDE'
            ,height='2',text='F#',width='1')
        self._ButtonFSharp.pack(expand='yes',fill='both',side='left')
        self._Frame15 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame15.pack(expand='yes',fill='both',side='left')
        self._Frame26 = Frame(self._Frame10)
        self._Frame26.pack(expand='yes',fill='both',side='left')
        self._ButtonGSharp = Button(self._Frame26,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonGSharp_command,foreground='#CCFFDE'
            ,height='2',text='G#',width='1')
        self._ButtonGSharp.pack(expand='yes',fill='both',side='left')
        self._Frame12 = Frame(self._Frame10,background='#016678',width='10')
        self._Frame12.pack(expand='yes',fill='both',side='left')
        self._Frame16 = Frame(self._Frame10)
        self._Frame16.pack(expand='yes',fill='both',side='left')
        self._ButtonASharp = Button(self._Frame16,activebackground='#3b3c3c'
            ,activeforeground='#CCFFDE',background='#2b3633'
            ,command=self._on__ButtonASharp_command,foreground='#CCFFDE'
            ,height='2',text='A#',width='1')
        self._ButtonASharp.pack(expand='yes',fill='both',side='left')
        self._Frame30 = Frame(self._Frame10,background='#016678')
        self._Frame30.pack(expand='yes',fill='both',side='left')
        self._Frame21 = Frame(self._Frame19,background='#016678',width='20')
        self._Frame21.pack(expand='yes',fill='both',side='left')
        self._ButtonC = Button(self._Frame21,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD',borderwidth='3'
            ,command=self._on__ButtonC_command,height='2',text='C')
        self._ButtonC.pack(expand='yes',fill='both',side='left')
        self._Frame25 = Frame(self._Frame19)
        self._Frame25.pack(expand='yes',fill='both',side='left')
        self._ButtonD = Button(self._Frame25,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonD_command,text='D')
        self._ButtonD.pack(expand='yes',fill='both',side='left')
        self._Frame20 = Frame(self._Frame19)
        self._Frame20.pack(expand='yes',fill='both',side='left')
        self._ButtonE = Button(self._Frame20,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonE_command,text='E')
        self._ButtonE.pack(expand='yes',fill='both',side='right')
        self._Frame1 = Frame(self._Frame19)
        self._Frame1.pack(expand='yes',fill='both',side='left')
        self._ButtonF = Button(self._Frame1,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonF_command,text='F')
        self._ButtonF.pack(expand='yes',fill='both',side='right')
        self._Frame27 = Frame(self._Frame19)
        self._Frame27.pack(expand='yes',fill='both',side='left')
        self._ButtonG = Button(self._Frame27,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonG_command,text='G')
        self._ButtonG.pack(expand='yes',fill='both',side='left')
        self._Frame2 = Frame(self._Frame19)
        self._Frame2.pack(expand='yes',fill='both',side='left')
        self._ButtonA = Button(self._Frame2,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonA_command,text='A')
        self._ButtonA.pack(expand='yes',fill='both',side='right')
        self._Frame6 = Frame(self._Frame19)
        self._Frame6.pack(expand='yes',fill='both',side='left')
        self._ButtonB = Button(self._Frame6,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonB_command,text='B')
        self._ButtonB.pack(expand='yes',fill='both',side='right')
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
            ,activeforeground='#2b3633',background='#FFFFCD',text='Magic mode'
            ,width='7')
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
    
        self.midi_in = None;
        self.midi_out = None;
        self.check_midi_ports();
        
        self._ButtonAutoMode.config(command=self.process_auto_mode_change);

        self.showMessage("Loading...");
        for note in self.utils.getNotes():
            self._ListboxNote.insert(END, note);
            
        for scale in self.utils.getAvailableScales():
            self._ListboxScale.insert(END, scale);
            
        self.current_scale = [10];
        self.current_note = [0];
        self.process_note_change(self.current_note);
        
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
        if self.midi_in is not None:
            self.midi_in.close_port();
        if self.midi_out is not None:
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
            self.midi_in_device_select_callback(0);
               
        if len(ports_out) == 0:
            self._MenuInput.config(text="No output devices");
        else:
            for port_index in range(0, len(ports_out)):
                self._MenuOutput.menu.add_command(label=ports_out[port_index], command=lambda port_index=port_index: self.midi_out_device_select_callback(port_index));
            self.midi_out_device_select_callback(0);
            
    def midi_out_device_select_callback(self, port_index):
        self.midi_out.close_port();
        self.midi_out.open_port(port_index);
        self.updateMenuTitle(port_index, self._MenuOutput, self._MenuOutput.menu);
        
    def midi_in_device_select_callback(self, port_index):
        self.midi_in.close_port();
        self.midi_in.open_port(port_index);
        self.midi_in.callback = self.midi_callback
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
        if (message[0] & 0xF0) in event_types:
            self.showCurrentNote(message);
            if self.auto_mode:
                if(message[1] < 60):
                    note_scale = self.utils.getNoteAndOctave(message[1]);
                    if len(self._ListboxScale.curselection()) == 0:
                        self.showMessage("Select scale first!");
                    else:
                        scale = self.utils.getAvailableScales()[self._ListboxScale.curselection()[0]];
                        self.mapped_scale = self.cache.getScaleFromCache(note_scale[0],scale);
                        self.showMessage("Magic mode scale:%s-%s"%(note_scale[0],scale));
                        self.midi_out.send_message(message);
                else:
                    self.send_modif_massage(message);
            else:
                self.send_modif_massage(message);
        else:
            self.midi_out.send_message(message);
            
    def send_modif_massage(self, message):
        note_octave = self.utils.getNoteAndOctave(message[1]);
        message[1] = self.utils.getMidiNumber(self.mapped_scale[note_octave[0]], note_octave[1]);
        message[1] += self.transpose;
        self.midi_out.send_message(message);
        
    
    def showCurrentNote(self, message):
        note_octave = self.utils.getNoteAndOctave(message[1]);
        note_name = note_octave[0];
        octave = note_octave[1];
        if (message[0] & 0xF0) in self.event_types:
            self.showMessage("Note: %s, Octave: %s, Vel: %s"%(note_name,octave,message[2]));
            
    def _on__ButtonScanMidi_command(self,Event=None):
        self.check_midi_ports();

    def process_note_change(self, note):
        if len(note) != 0 and len(self.current_scale) != 0:
            note_name = notes.int_to_note(note[0]);
            scale_name = self.utils.getAvailableScales()[self.current_scale[0]];
            self.scale_to_map = self.mapper.getScaleToMap(note_name, scale_name);
            self.mapped_scale = self.cache.getScaleFromCache(note_name, scale_name);
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
        self.set_custom_mapped_scale();
        #self.searchForScale(self.scale_to_map)
        self.auto_mode = False;
        return new_state;
    
    def searchForScale(self, scale_to_search):
        for note in self.utils.getNotes():
            for scale in self.utils.getAvailableScales():
                if set(scale_to_search) == set(self.mapper.getScaleToMap(note, scale)):
                    print note,scale;
                    print hash(set(scale_to_search))
                    print hash(set(self.mapper.getScaleToMap(note, scale)))
            
    def update_scale_to_map(self, note):
        if self.button_state_map[note] is True:
            self.scale_to_map.remove(note);
            return False;
        else:
            self.scale_to_map.append(note);
            return True;

    def set_custom_mapped_scale(self):
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

    def _on__ButtonQuit_command(self,Event=None):
        if self.midi_in is not None:
            self.midi_in.close_port();
        if self.midi_out is not None:
            self.midi_out.close_port();
        exit(0);

    def _on__ScaleTrans_command(self,Event=None):
        self.transpose = self._ScaleTrans.get();
        