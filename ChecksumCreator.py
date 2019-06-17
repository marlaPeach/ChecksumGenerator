#This script will take in a csv file and create a SHA256 hash checksum for each file based on the asset path.
#Precondition: program assumes that the dialect of csv will be microsoft excel.
#This script takes in a csv, creates a checksum of each file in the manifest based on the path given, and outputs a csv with four fields.
#Creates a log to hold a record of each file's successful completion or error, also gives notification of finished manifest processing.
#Ingested file will need to have File Number, Path, and Piction UMO fields. (Last is conditioned upon and returned if present.)

#author: Tiffany Schmidt
import hashlib
import sys
import csv
import io
import datetime

#variables and constants
in_path = ''
out_path = ''
log_path = ''
rowlib = []
file_counter = 0
header_lib = ['File Number', 'Path', 'SHA256 Checksum', 'Piction UMO']
ENCODING = 'ascii'
BLOCK_SIZE = 16384

#ingest csv and create path library
def csv_io(infile, outfile, log):
    try:
        with open(infile, 'r+', newline= '') as f:
            newreader = csv.reader(f)
            write_headers(outfile, header_lib, log)
            file_counter=0
            for row in newreader:
                file_counter = row[0]
                line = row[1].strip()
                line.strip('\n')
                line.strip("'")
                newline = line.replace('\\', '\\\\')
                rowlib = [file_counter, line, 0]
                checksum = create_checksum(newline, log)
                writeto_log('File processed successfully: ' + file_counter, log)
                rowlib[2]=checksum
                rowlib.append(UMO_check(row))
                writeto_csv(outfile, rowlib, log)
        writeto_log('Manifest processed successfully.', log)
        writeto_log('Checksum manifest at: ' + outfile, log)
        writeto_log('Log found at: ' + log, log)
    except(FileNotFoundError):
        writeto_log('Error: File Not Found. Possible path input error.', log)
    except(IsADirectoryError):
        writeto_log('Please check that file number: ' + file_counter + ' is a file, and not a directory.', log)
    except(IOError):
        writeto_log('Error: I/O Error: File read error.', log)
        writeto_log('Please check file number: ' + file_counter + '.', log)
    except(PermissionError):
        writeto_log('Error: Access not permitted for this operation. (Read permissions.)', log)


def UMO_check(row):
    if(len(row)<2):
        return 'No UMO'
    else:
        return row[2]


#create checksums and add to row
def create_checksum(path, log):
    sha256 = hashlib.sha256()
    try:
        with open(path, 'rb') as data:
            for item in iter(lambda: data.read(BLOCK_SIZE), b''):
                sha256.update(item)
        return sha256.hexdigest()
    except(TimeoutError):
        writeto_log('Error: Timeout Error. (Checksum generation.)', log)
    except(IsADirectoryError):
        writeto_log('Error: File operation cannot be performed on a directory.', log)


#create csv with path, if UMO, and calculated checksum
def writeto_csv(fname, library, log):
    try:
        with open(fname, 'a', encoding=ENCODING, newline='\n') as out:
            writer = csv.writer(out, dialect='excel')
            writer.writerow(library)
    except(IOError):
        writeto_log('Error: I/O Error: File write error.', log)
    except(PermissionError):
        writeto_log('Error: Access not permitted for this operation. (Write permissions.)', log)

#write headers
def write_headers(fname, headers, log):
    try:
        with open(fname, 'a', encoding=ENCODING, newline='\n') as out:
            header_writer = csv.writer(out, dialect='excel')
            header_writer.writerow(headers)
    except(IOError):
        writeto_log('Error: I/O Error: File write error.', log)
    except(PermissionError):
        writeto_log('Error: Access not permitted for this operation. (Write permissions.)', log)

#create .txt log of files.
def writeto_log(result, log):
    date = str(datetime.date.today())
    path = log.replace('\\', '\\\\')
    fname = path + '\\manifestlog_' + date + '.txt'
    try:
        with open(fname, 'a') as log:
            log.write(result + '\n')
    except(IOError):
        print('I/O Error: Cannot write to log.')
        print('Process ended at file number: ' + file_counter)

#main
def main():
    for t in sys.argv[3]:
        in_path = sys.argv[1]
        out_path = sys.argv[2]
        log_path = sys.argv[3]
    csv_io(in_path, out_path, log_path)

if __name__ == '__main__':
    main()