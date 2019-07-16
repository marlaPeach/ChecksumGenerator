#Driver for checksum manifest maker.

import UI_Mac
from tkinter import messagebox

#main
def main():
    try:
    	UI=UI_Mac.Window()
    except:
        messagebox.showerror('Utility Message.', 'This program has encountered a fatal error.')
if __name__ == '__main__':
    main()