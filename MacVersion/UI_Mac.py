#Create a simple user interface.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import GeneratorMac
import time
import os
import webbrowser
import sys
import platform

class Window(Frame):

	def __init__(self, master=None):
		self.master = master
		self.master.title("Checksum Manifest Creator")
		# Create file and edit menus.
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file = Menu(menu, tearoff=False)
		
		file.add_command(label="Exit", command=self.close_window)
		menu.add_cascade(label="File", menu=file)
		edit = Menu(menu, tearoff=False)
		edit.add_command(label="Clear", command=self.clear_fields)
		menu.add_cascade(label="Edit", menu=edit)
		info = Menu(menu, tearoff=False)
		info.add_command(label="CSV Layout Infomation", command=self.open_csv_help)
		info.add_command(label="I/O Path Information", command=self.open_io_help)
		menu.add_cascade(label="Help", menu=info)


		#Heading Label:
		heading = Label(self.master, text="Checksum Creator", font=('Times', 14))
		heading.grid(row=2, column=1, columnspan=3, sticky=W+E+N+S, pady=5)
		sub_heading = Label(self.master, text="Please enter the details of your transaction below to continue.", font=('Times', 12))
		sub_heading.grid(row=3, column=1, columnspan=3, sticky=W+E+N+S, pady=5)
		
		#User input area. Labels and entries.
		Label(self.master, text="Input File Path:", font=('Times', 12)).grid(row=4, column=1, padx=25, pady=5)
		self.input = Entry(self.master, width=70)
		self.input.grid(row=4, column=2, columnspan=2, padx=10, pady=5)
		Label(self.master, text="Output File Path:", font=('Times', 12)).grid(row=5, column=1, padx=25, pady=5)
		self.output = Entry(self.master, width=70)
		self.output.grid(row=5, column=2, columnspan=2, padx=10, pady=5)
		Label(self.master, text="Log File Path:", font=('Times', 12)).grid(row=7, column=1, padx=25, pady=5)
		self.log = Entry(self.master, width=70)
		self.log.grid(row=7, column=2, columnspan=2, padx=10, pady=5)

		#Display message for ease of use.

		message_text = 'Please note that when entering input, output, and log paths you will need to include file names. Please be sure that file names for output and log are not already in use within that directory, or those files may be overwritten. See Help files for further details on program specifics.'
		Label(self.master, text=message_text, bg='alice blue', font=('Times', 12), wraplength=500, bd=4, relief=SUNKEN).grid(row=8, column=0, columnspan=4, padx=20, pady=10, ipadx=10, ipady=10, sticky=W+E+N+S)

		#Buttons for quit, clear fields, and start.
		#Clear Fields button.
		clear_button = Button(self.master, text="Clear Fields", command=self.clear_fields)
		clear_button.grid(row=10, column=1, sticky=W+E+N+S, padx=25, pady=10, ipadx=10)

		#Start Button
		start_button = Button(self.master, text="Begin Transaction", command=self.process_transaction)
		start_button.grid(row=10, column=2, sticky=W+E+N+S, padx=10, pady=10)

		#Quit button.
		quit_button = Button(self.master, text="Quit", command=self.close_window)
		quit_button.grid(row=10, column=3, sticky=W+E+N+S, padx=25, pady=10)
		
	#Clear entry boxes of path values.
	def clear_fields(self):
		self.input.delete(0, 'end')
		self.output.delete(0, 'end')
		self.log.delete(0, 'end')

	#Use values and checksum generator to process files.
	def process_transaction(self):
		display_running(self)
		generator = GeneratorMac.ChecksumGenerator()
		generator.set_input(self.input.get().encode('utf-8').strip())
		generator.set_output(self.output.get().encode('utf-8').strip())
		generator.set_log(self.log.get().encode('utf-8').strip())
		generator.csv_io()

	#Open csv help file.
	def open_csv_help(self):
		#help_file = ('TextEdit.exe csv_layout.txt')
		#os.system(help_file)
		help_file1 = 'csv_layout.txt'
		os.system("open " + help_file1)

	#Open IO help file.
	def open_io_help(self):
		help_file2 = ('io_info.txt')
		os.system("open " + help_file2)

	#Close the UI window.
	def close_window(self):
		exit()

	#Get the value of the in_path entry box.
	def get_in_path(self):
		return self.input.get()

	#Get the value of the out_path entry box.
	def get_out_path(self):
		return self.output.get()

	#Get the value of the log_path entry box.
	def get_log_path(self):
		return self.log.get()

#Displays message that program is running properly.
def display_running(self):
	messagebox.showinfo('Utility Message', 'Checksum utility has begun working. Please wait.')


root = Tk()
root.geometry("850x375")
app = Window(root)
root.mainloop()