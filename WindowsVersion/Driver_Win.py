#Driver for checksum manifest maker.

import UI_Win
from tkinter import messagebox

#main
def main():
    try:
    	UI=UI_Win.Window()
    except:
        messagebox.showerror('Utility Message.', 'This program has encountered a fatal error.')

if __name__ == '__main__':
    main()