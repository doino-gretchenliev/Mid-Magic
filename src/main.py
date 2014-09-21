#!/usr/bin/python
#coding=utf8

from Tkinter import *
import sys
from ui import Gui
    
if __name__ == '__main__':
    Root = Tk()
    App = Gui(Root)
    App.pack(expand='yes',fill='both')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    Root.overrideredirect(1)
    Root.geometry("%dx%d+0+0" % (w, h))
    Root.focus_set() # <-- move focus to this widget
    Root.bind("<Escape>", lambda e: e.widget.quit())
    Root.title('Mid!Magic')
    Root.mainloop()