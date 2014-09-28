#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

from ui_mainform import Ui_MainWindow
from utils import Utils
from cache import ScaleCache
from mapper import Mapper

import rtmidi_python as rtmidi

class MainForm(QtGui.QMainWindow):
    
    NOTE_OFF = 0x80
    NOTE_ON = 0x90

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        
        self.utils = Utils();
        self.cache = ScaleCache();
        self.mapper = Mapper();
        
        self.scale_to_map = [];
        self.mapped_scale = {};
        self.transpose = 0;
        self.autoScale = False;

        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);
        
        self.loadAvailableScales();
        self.loadInitScale();
        
        self.midi_in = None;
        self.midi_out = None;
        self.check_midi_ports();

        self.ui.statusBar.showMessage("Ready for rock'N'roll!",1000*5);
    
        
    def loadAvailableScales(self):
        for scale in self.utils.getAvailableScales():
            self.ui.listWidgetScales.addItem(scale);
            
    def loadInitScale(self):
        self.ui.listWidgetNotes.setCurrentRow(0);
        self.ui.listWidgetScales.setCurrentRow(0);
        result = self.cache.getScaleFromCache(str(self.ui.listWidgetNotes.item(0).text()),str(self.ui.listWidgetScales.item(0).text()));
        self.setNewScale(result);
    
                    
    @QtCore.pyqtSlot(str)
    def on_listWidgetScales_currentTextChanged(self, scale):
        currNote = self.ui.listWidgetNotes.currentItem();
        if currNote is not None:
            result = self.cache.getScaleFromCache(str(currNote.text()), str(scale));
            self.setNewScale(result);
            self.ui.statusBar.showMessage("Mapped scale: %s-%s"%(str(currNote.text()),str(scale)), 1000 * 5);

        
    @QtCore.pyqtSlot(str)
    def on_listWidgetNotes_currentTextChanged(self, note):
        currScale = self.ui.listWidgetScales.currentItem();
        if currScale is not None:
            result = self.cache.getScaleFromCache(str(note), str(currScale.text()));
            self.setNewScale(result);    
            self.autoScale = False;
            self.ui.pushButtonMagic.setChecked(False);
            self.ui.statusBar.showMessage("Mapped scale: %s-%s"%(str(note),str(currScale.text())), 1000 * 5);

            
    def setNewScale(self, scales):
        self.scale_to_map = scales['scale_to_map'];
        self.mapped_scale = scales['mapped_scale'];
        self.showOnKeys();
        
    def showOnKeys(self):
        for key in self.utils.getNotes():
            replacedKey = key.replace('#','S');
            if key in self.scale_to_map:
                new_state = True;               
            else:
                new_state = False;
            eval('self.ui.pushButton' + replacedKey + ".setChecked(" + str(new_state) + ")");
            
    def setNewKeyState(self, key, state):
        if state:
            self.scale_to_map.append(key);
            self.mapped_scale = self.mapper.getMap(self.scale_to_map);
        else:
            if key in self.scale_to_map:
                self.scale_to_map.remove(key);
                if len(self.scale_to_map) != 0:
                    self.mapped_scale = self.mapper.getMap(self.scale_to_map);
        
        self.autoScale = False;
        self.ui.pushButtonMagic.setChecked(False);
        self.ui.statusBar.showMessage("Custom scale: " + str(self.scale_to_map), 1000 * 5);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonC_clicked(self, status):
        self.setNewKeyState('C', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonCS_clicked(self, status):
        self.setNewKeyState('C#', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonD_clicked(self, status):
        self.setNewKeyState('D', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonDS_clicked(self, status):
        self.setNewKeyState('D#', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonE_clicked(self, status):
        self.setNewKeyState('E', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonF_clicked(self, status):
        self.setNewKeyState('F', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonFS_clicked(self, status):
        self.setNewKeyState('F#', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonG_clicked(self, status):
        self.setNewKeyState('G', status);
    
    @QtCore.pyqtSlot(bool)
    def on_pushButtonGS_clicked(self, status):
        self.setNewKeyState('G#', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonA_clicked(self, status):
        self.setNewKeyState('A', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonAS_clicked(self, status):
        self.setNewKeyState('A#', status);
        
    @QtCore.pyqtSlot(bool)
    def on_pushButtonB_clicked(self, status):
        self.setNewKeyState('B', status);
        
    @QtCore.pyqtSlot(int)
    def on_spinBoxTranspose_valueChanged(self, value):
        self.transpose = value;
        
    @QtCore.pyqtSlot()
    def on_pushButtonScan_clicked(self):
        self.check_midi_ports();
        
    def check_midi_ports(self):
        if self.midi_in is not None:
            self.midi_in.close_port();
        if self.midi_out is not None:
            self.midi_out.close_port();
        
        self.midi_in = rtmidi.MidiIn();
        self.midi_out = rtmidi.MidiOut();
        
        ports_in = self.midi_in.ports;
        ports_out = self.midi_out.ports;
        
        self.ui.listWidgetInput.clear();
        self.ui.listWidgetOutput.clear();
                
        if len(ports_in) == 0:
            self.ui.listWidgetScales.addItem("No input devices");
        else:
            for port_index in range(0, len(ports_in)):
                self.ui.listWidgetInput.addItem(ports_in[port_index]);
            self.on_listWidgetInput_currentRowChanged(0);
               
        if len(ports_out) == 0:
            self._MenuInput.config(text="No output devices");
        else:
            for port_index in range(0, len(ports_out)):
                self.ui.listWidgetOutput.addItem(ports_out[port_index]);
            self.on_listWidgetOutput_currentRowChanged(0);
            
        self.ui.statusBar.showMessage("Scan completed!",1000*5);
            
    @QtCore.pyqtSlot(bool)
    def on_pushButtonMagic_clicked(self, state):
        self.autoScale = state;
        self.ui.statusBar.showMessage("Magic mode: %s"%(state),1000*5);
            
    @QtCore.pyqtSlot(int)
    def on_listWidgetInput_currentRowChanged(self, port):
        self.midi_in.close_port();
        self.midi_in.open_port(port);
        self.midi_in.callback = self.midi_callback
        self.ui.statusBar.showMessage("%s port opened!"%(self.ui.listWidgetInput.item(port).text()),1000*5);
            
    @QtCore.pyqtSlot(int)
    def on_listWidgetOutput_currentRowChanged(self, port):
        self.midi_out.close_port();
        self.midi_out.open_port(port);
        self.ui.statusBar.showMessage("%s port opened!"%(self.ui.listWidgetOutput.item(port).text()),1000*5);

        
    def midi_callback(self, message, time_stamp):
        event_types = (self.NOTE_ON, self.NOTE_OFF)
        if (message[0] & 0xF0) in event_types:
            if self.autoScale:
                if(message[1] < 60):
                    note_scale = self.utils.getNoteAndOctave(message[1]);
                    scale = str(self.ui.listWidgetScales.currentItem().text());
                    
                    result = self.cache.getScaleFromCache(note_scale[0], scale);
                    self.scale_to_map = result['scale_to_map'];
                    self.mapped_scale = result['mapped_scale'];
                
                    #self.ui.statusBar.showMessage("Magic mode scale:%s-%s"%(note_scale[0],scale),1000*5);
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
    
    @QtCore.pyqtSlot()
    def on_pushButtonExit_clicked(self):
        self.closeOpenPorts();
        self.close();
        
    def closeOpenPorts(self):
        if self.midi_in is not None:
            self.midi_in.close_port();
        if self.midi_out is not None:
            self.midi_out.close_port();
            
    def __exit__(self):
        self.closeOpenPorts();
        
if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv);
    displayReso = QtGui.QDesktopWidget().screenGeometry();
    if displayReso.width() == 320 and displayReso.height() == 240:    
        app.setStyle(QtGui.QStyleFactory.create("plastique"));
        mainForm = MainForm();
        mainForm.showFullScreen();
    else:
        mainForm = MainForm();
        mainForm.show();
    
    sys.exit(app.exec_())
