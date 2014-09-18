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

class Gui(Frame):
    
    transpose = 0;
    scale_to_map = [];
    mapped_scale = {};
    
    button_state_map = {};
    
    button_color_state_map_black = {True:'#00CCA9',False:'#2b3633'};
    button_color_state_map_white = {True:'#00CCA9',False:'#FFFFCD'};
    
    def __init__(self,Master=None,*pos,**kw):
        self.utils = Utils();
        self.cache = ScaleCache();
        self.mapper = Mapper();
        self.load_init_button_states();
        
        apply(Frame.__init__,(self,Master),kw)

        self._Frame4 = Frame(self)
        self._Frame4.pack(expand='yes',fill='both',side='left')
        self._Frame3 = Frame(self,background='#016678')
        self._Frame3.pack(expand='yes',fill='both',side='left')
        self._Frame29 = Frame(self._Frame4,background='#016678')
        self._Frame29.pack(expand='yes',fill='both',side='top')
        self._ListboxNote = Listbox(self._Frame29,background='#014455'
            ,foreground='#CCFFDE',highlightthickness='0',selectmode='single'
            ,width='15')
        self._ListboxNote.pack(expand='yes',fill='both',side='left')
        self._Frame28 = Frame(self._Frame4,background='#016678')
        self._Frame28.pack(expand='yes',fill='both',side='top')
        self._ListboxScale = Listbox(self._Frame28,background='#014455'
            ,foreground='#CCFFDE',highlightthickness='0',selectmode='single'
            ,width='15')
        self._ListboxScale.pack(expand='yes',fill='both',side='left')
        self._Frame11 = Frame(self._Frame3,background='#016678')
        self._Frame11.pack(expand='yes',fill='both',side='top')
        self._LabelStatus = Label(self._Frame11,background='#FFFFCD'
            ,relief='groove',state='disabled',text='This is test text.')
        self._LabelStatus.pack(expand='yes',fill='both',side='top')
        self._Frame10 = Frame(self._Frame3,background='#016678')
        self._Frame10.pack(side='top')
        self._Frame19 = Frame(self._Frame3)
        self._Frame19.pack(side='top')
        self._Frame18 = Frame(self._Frame3)
        self._Frame18.pack(expand='yes',fill='both',side='top')
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
        self._Frame5 = Frame(self._Frame19)
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
        self._Frame17 = Frame(self._Frame18,background='#016678')
        self._Frame17.pack(expand='yes',fill='both',side='left')
        self._ButtonMap = Button(self._Frame17,activebackground='#ffffff'
            ,activeforeground='#2b3633',background='#FFFFCD'
            ,command=self._on__ButtonMap_command,text='Map')
        self._ButtonMap.pack(expand='yes',side='top')
        self._Frame9 = Frame(self._Frame18,background='#016678')
        self._Frame9.pack(expand='yes',fill='both',side='left')
        self._ButtonQuit = Button(self._Frame9,activebackground='#BB1167'
            ,background='#CD0045',command=self._on__ButtonQuit_command
            ,text='Quit')
        self._ButtonQuit.pack(expand='yes',side='left')

        for note in self.utils.getNotes():
            self._ListboxNote.insert(END, note);
            
        for scale in self.utils.getAvailableScales():
            self._ListboxScale.insert(END, scale);
        
        self.current_note = ()
        self.current_scale = ()   
        self.poll() # start polling the list

    def poll(self):
        now_note = self._ListboxNote.curselection();
        now_scale = self._ListboxScale.curselection();
        if len(now_note) != 0 and now_note != self.current_note:
            self.process_note_change(now_note)
            self.current_note = now_note
        if len(now_scale) != 0 and now_scale != self.current_scale:
            self.process_scale_change(now_scale)
            self.current_scale = now_scale
        self.after(250, self.poll)

    def process_note_change(self, note):
        print note
        print self.current_scale
        if len(note) != 0 and len(self.current_scale) != 0:
            note_name = notes.int_to_note(note[0]);
            scale_name = self.utils.getAvailableScales()[self.current_scale[0]];
            self.scale_to_map = self.mapper.getScaleToMap(note_name, scale_name);
            mapped_scale = self.mapper.getMap(note_name, scale_name);
            self.show_scale_to_buttons();
     
    def process_scale_change(self, scale):
        if len(scale) != 0 and len(self.current_note) != 0:
            note_name = notes.int_to_note(self.current_note[0]);
            scale_name = self.utils.getAvailableScales()[scale[0]];
            self.scale_to_map = self.mapper.getScaleToMap(note_name, scale_name);
            self.mapped_scale = self.mapper.getMap(note_name, scale_name);
            self.show_scale_to_buttons();
            
    def show_scale_to_buttons(self):
        for note in self.utils.getNotes():
            button_name = note.replace('#','Sharp');
            button_name = "self._Button" + button_name;
            
            if note in self.scale_to_map:
                if '#' in note:
                    button_color = self.button_color_state_map_black[True];
                else:
                    button_color = self.button_color_state_map_white[True];
            else:
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
        exit(0);

    def _on__ScaleTrans_command(self,Event=None):
        self.transpose = self._ScaleTrans.get();


