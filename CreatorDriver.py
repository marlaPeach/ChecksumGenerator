#Driver for checksum manifest maker.

import UI_Win
import UI_Mac
import GeneratorWin
import GeneratorMac
import sys
import platform
import os
from tkinter import messagebox

#main
def main():
    if sys.platform.startswith('darwin'):
    	print(os.name)
    	print(sys.platform)
    	UI=UI_Mac.Window()
    elif sys.platform.startswith('cygwin'):
    	print(os.name)
    	print(sys.platform)
    	UI=UI_Win.Window()
    elif sys.platform.startswith('win32'):
    	print(os.name)
    	print(sys.platform)
    	UI=UI_Win.Window()
    else:
    	messagebox.showerror('Utility Message', 'Cannot detect operating system.')

if __name__ == '__main__':
    main()