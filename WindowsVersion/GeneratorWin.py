#The class creates an object that will generate checksums from a given csv file and return a new csv with an added checksum field.
#File must be a csv and all path field variables must point to a file object, not a folder.
#
#Author: Tiffany Schmidt
#Date Created: 6/26/19

import hashlib
import sys
import csv
import io
import datetime
from tkinter import messagebox

# variables and constants
in_path = ''
out_path = ''
log_path = ''
rowlib = []
header_lib = []
file_counter = 0
ENCODING = 'ascii'
BLOCK_SIZE = 16384

class ChecksumGenerator():

    # ingest csv and output information and checksums to new csv.
    def csv_io(self):
        try:
            with open(self.in_path, 'r+', newline='') as f:
                new_reader = csv.reader(f)
                headers_input(new_reader)
                write_headers(self.out_path, header_lib)
                file_counter = 0
                for row in new_reader:
                    file_counter = row[0]
                    line = row[1].strip()
                    line.strip('\n')
                    line.strip("'")
                    newline = line.replace('\\', '\\\\')
                    if(line == ''):
                        writeto_log(file_counter, 'Cannot find file. Blank path value.', self.log_path)
                        rowlib = create_row(row, '-Error-')
                    elif(line[-1]=='\\'):
                        writeto_log(file_counter, 'This is a directory path, not a file path. ', self.log_path)
                        rowlib = create_row(row, '-Error-')
                    else:
                        checksum = create_checksum(newline)
                        rowlib = create_row(row, checksum)
                    writeto_csv(self.out_path, rowlib)
                    del rowlib[:]
            del header_lib[:]
            messagebox.showinfo('Utility Message', 'File complete.')
        except(PermissionError):
            messagebox.showerror('Utility Message','Critical Error: Access not permitted for this operation. (Read permissions.)')
        except(IOError):
            messagebox.showerror('Utility Message','Critical Error: I/O Error: File read error.')
        except(FileNotFoundError):
            messagebox.showerror('Utility Message','Critical Error: File Not Found. Possible path input error.')

    def set_input(self, inpath):
        self.in_path = inpath

    def set_output(self, output):
        self.out_path = output

    def set_log(self, log):
        self.log_path = log

#create .txt log
def writeto_log(filenum,result, path):
    try:
        with open(path, 'a') as log:
            log.write(str(filenum))
            log.write(' ' + result + '\n')
    except(IOError):
        messagebox.showerror('Utility Message',' Critical Error: Cannot write to log.')

#create checksum from path.
def create_checksum(path):
    sha256 = hashlib.sha256()
    with open(path, 'rb') as data:
        for item in iter(lambda: data.read(BLOCK_SIZE), b''):
            sha256.update(item)
    return sha256.hexdigest()

#Takes in first row of csv as headers.
def headers_input(reader):
    line = reader.__next__()
    for i in line:
        header_lib.append(i)
    header_lib.append('Checksum')
    return header_lib

#Creates the new row that includes the checksum value.
def create_row(row, checksum):
    for i in row:
        rowlib.append(i)
    rowlib.append(checksum)
    return rowlib

#create csv with path, if UMO, and calculated checksum
def writeto_csv(fname, library):
    try:
        with open(fname, 'a', encoding=ENCODING, newline='\n') as out:
            writer = csv.writer(out, dialect='excel')
            writer.writerow(library)
    except(IOError):
        messagebox.showerror('Utility Message','Critical Error: I/O Error: File write error.')
    except(PermissionError):
        messagebox.showerror('Utility Message','Critical Error: Access not permitted for this operation. (Writing to csv.)')

#write headers
def write_headers(fname, headers):
    try:
        with open(fname, 'a', encoding=ENCODING, newline='\n') as out:
            header_writer = csv.writer(out, dialect='excel')
            header_writer.writerow(headers)
    except(IOError):
        messagebox.showerror('Utility Message','Critical Error: I/O Error: File write error.')
    except(PermissionError):
        messagebox.showerror('Utility Message','Critical Error: Access not permitted for this operation. (Writing headers to csv.)')

