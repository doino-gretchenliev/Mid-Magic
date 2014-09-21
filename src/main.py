#!/usr/bin/python
#coding=utf8

from Tkinter import *
import sys
from ui import Gui
    
if __name__ == '__main__':
    Root = Tk()
    App = Gui(Root)
    App.pack(expand='yes',fill='both')
    Root.geometry('320x240+10+10')
    Root.title('Mid!Magic')
    Root.mainloop()